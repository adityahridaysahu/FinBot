from random import randint
from flask import Flask, request, jsonify
from flask_restful import reqparse
from flask.views import MethodView
from flask_cors import CORS
from bond_dao import BondDAO
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
trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "bond_service"})))
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))
FlaskInstrumentor().instrument_app(app)
tracer = trace.get_tracer(__name__)

class BondService:
    def __init__(self):
        with tracer.start_as_current_span("bond_init") as span:
            self.dao = BondDAO()

    def process_bond_api_request(self):
        with tracer.start_as_current_span("bond_api_request") as span:
            data = request.json
            query = data['sql_query']
            result = self.dao.execute_query(query)
            return jsonify(result)
            # return "hello"
