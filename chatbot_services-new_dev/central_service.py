from tools.keyword_extractor import keyword_extractor
from tools.task1_classifier import task1_classifier
from tools.cumulative_summary import cumulative_summary
import asyncio,json
from random import randint
from flask import Flask, request, jsonify
from flask_restful import reqparse
from flask.views import MethodView
from flask_cors import CORS
from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)
CORS(app)

jaeger_exporter = JaegerExporter(
    agent_host_name="18.234.222.4",
    agent_port=6831,
)
trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "central_service"})))
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))
FlaskInstrumentor().instrument_app(app)
tracer = trace.get_tracer(__name__)

with open("config.json") as config_file:
    config = json.load(config_file)

convo_link = config["convo"]
global_link = config["global"]
bonds_link = config["bonds"]

class CentralService:
    def __init__(self, convo_dao, global_dao):
        with tracer.start_as_current_span("central_init") as span:
            self.convo_dao = convo_dao
            self.global_dao = global_dao
    

    async def update_summary(self, delay, session_id, question, id_hits, response, csum_bot, csum_user):
        with tracer.start_as_current_span("update_summary") as span:
            result = cumulative_summary(session_id, question, response, csum_bot, csum_user)
            status = result["status"]
            if status == "working":
                new_summaries = result
                if new_summaries["new_cum_sum_user"] != "" and new_summaries["new_cum_sum_bot"] != "":
                    new_cum_sum_user = new_summaries["new_cum_sum_user"]
                    new_cum_sum_bot = new_summaries["new_cum_sum_bot"]
                    self.convo_dao.update_summary(session_id, question, id_hits, new_cum_sum_user, new_cum_sum_bot)
            else:
                print("Convo database could not be updated")
            return

  

    async def summary_runner(self, session_id, question, id_hits, response, csum_bot, csum_user):
        with tracer.start_as_current_span("summarry_runner") as span:
            task1 = asyncio.create_task(
            self.update_summary(1, session_id, question, id_hits, response, csum_bot, csum_user)
            )
            await task1
            return

    
    def process_request(self):
        with tracer.start_as_current_span("process_request") as span:
            data = request.json
            question = data["query"]
            session_id = data["session_id"]
            csum_bot = ""
            csum_user = ""

            data = self.convo_dao.mask_session(session_id)
            if session_id == "":
                session_id = data["unique_id"]
            else:
                csum_user = data["cum_sum_user"]
                csum_bot = data["cum_sum_bot"]

            if question != "":
                keywords = keyword_extractor(question)
                keyword_string = ",".join(keywords)
                responses = self.global_dao.get_keyword_hits(keyword_string)
                sentences = ' '.join([d['response'] for d in responses])
                ids = [str(d['id']) for d in responses]
                id_hits = ",".join(ids)

                cs = task1_classifier(question, bonds_link, sentences, csum_bot, csum_user)
                if cs["api_status"] == "working":
                    typer = cs["api_status"]
                    response = cs["result"]

                    if response[:10] == 'Rate Limit':
                        print("Cannot update convo database because of rate limitation")
                    else:
                        print("Running convo database updater")
                        asyncio.run(self.summary_runner(session_id, question, id_hits, response, csum_bot, csum_user))

                    output = {
                        "session_id": session_id,
                        "status": typer,
                        "response": response
                    }
                    return output
                else:
                    output = {
                        "session_id": session_id,
                        "status": cs["api_status"],
                        "response": cs["status"]
                    }
                    return output

            output = {
                "session_id": session_id,
                "status": "GlobalDB Error",
                "response": "We are facing an issue. Please wait."
            }
            return output


class FeedbackService:

    async def update_feedback(self, delay, status, hits):
        with tracer.start_as_current_span("Feedback_updation") as span:
            output = self.global_dao.get_feedback(status, hits)
            return

    async def feedback_runner(self,status, hits):
        with tracer.start_as_current_span("Feedback_runner") as span:
            task1 = asyncio.create_task(
                self.update_feedback(1, status, hits)
            )
            await task1
            return


    def __init__(self, convo_dao, global_dao):
        with tracer.start_as_current_span("feedback_init") as span:
            self.convo_dao = convo_dao
            self.global_dao = global_dao

    def process_feedback(self):
        with tracer.start_as_current_span("feedback_process") as span:
            data = request.json
            session_id = data["session_id"]
            timeout = data["timeout"]
            clicked = data["clicked"]


            data = self.convo_dao.mask_session(session_id)
            hits = data["global_hits"]
            status = ""

            if timeout:
                isClosed = True
                isResolved = False

                data = self.convo_dao.update_status(session_id, isResolved, isClosed)
                return data
            else:
                if clicked:
                    isResolved = True
                    isClosed = True
                    status = "positive"
                else:
                    isResolved = False
                    isClosed = False
                    status = "negative"


                asyncio.run(self.feedback_runner(status, hits))
                return {
                    "updated" : True
                }
