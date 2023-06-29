from random import randint
from flask import Flask, request, jsonify
from flask_restful import reqparse
from flask.views import MethodView
from flask_cors import CORS
from convo_dao import ConvoDAO
import json
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
trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "convo_service"})))
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))
FlaskInstrumentor().instrument_app(app)
tracer = trace.get_tracer(__name__)

class ConvoService:
    def __init__(self):
        with tracer.start_as_current_span("convo_services_init") as span:
            self.dao = ConvoDAO()

    def update_status(self):
        with tracer.start_as_current_span("convo_update") as span:
            data = request.json
            unique_id = data['unique_ID']
            is_resolved = data['isResolved']
            is_closed = data['isClosed']
            return self.dao.update_status(unique_id, is_resolved, is_closed)

    def mask_session(self):
        with tracer.start_as_current_span("masking_session") as span:
            data = request.json
            unique_id = data['unique_ID']
            return self.dao.mask_session(unique_id)

    def update_summary(self):
        with tracer.start_as_current_span("summary_update") as span:
            data = request.json
            unique_id = data['unique_ID']
            new_cum_sum_user = data['new_cum_sum_user']
            new_cum_sum_bot = data['new_cum_sum_bot']
            global_hits = data['global_hits']
            return self.dao.update_summary(unique_id, new_cum_sum_user, new_cum_sum_bot, global_hits)
