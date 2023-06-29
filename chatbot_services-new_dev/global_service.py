from random import randint
from flask import Flask, request, jsonify
from flask_restful import reqparse
from flask.views import MethodView
from flask_cors import CORS
from global_dao import GlobalDAO
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
trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "global_service"})))
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))
FlaskInstrumentor().instrument_app(app)
tracer = trace.get_tracer(__name__)

class GlobalService:
    def __init__(self):
        with tracer.start_as_current_span("global_init") as span:
            self.dao = GlobalDAO()

    def extract_responses(self):
        with tracer.start_as_current_span("extract_response") as span:
            keywords = request.json['keywords']
            return self.dao.extract_responses(keywords)

    def positive_feedback(self):
        with tracer.start_as_current_span("positive_feedback") as span:
            data = request.json
            ids = data["id"]
            threshold = 0.1
            return self.dao.update_positive_feedback(ids, threshold)
    
    def negative_feedback(self):
        with tracer.start_as_current_span("negative_feedback") as span:
            data = request.json
            ids = data["id"]
            threshold = 0.1
            return self.dao.update_negative_feedback(ids, threshold)
