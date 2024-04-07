import logging

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter,
)
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import (
    OTLPMetricExporter,
)
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.metrics import (
    get_meter_provider,
    set_meter_provider,
)
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def instrument_api(app: FastAPI):
    FastAPIInstrumentor().instrument_app(app)


def setup_otel():
    resource = Resource.create(
        {
            SERVICE_NAME: "shoppingcart",
        }
    )

    # logging
    logger_provider = LoggerProvider(
        resource=resource,
    )
    set_logger_provider(logger_provider)
    exporter = OTLPLogExporter(insecure=True, endpoint="http://localhost:4317")
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
    handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
    logging.basicConfig(level=logging.INFO, handlers=[handler])

    # traces
    trace_provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(OTLPSpanExporter(insecure=True, endpoint="http://localhost:4317"))
    trace_provider.add_span_processor(processor)
    trace.set_tracer_provider(trace_provider)

    # metrics
    metric_exporter = OTLPMetricExporter(insecure=True, endpoint="http://localhost:4317")
    metric_reader = PeriodicExportingMetricReader(metric_exporter)
    provider = MeterProvider(metric_readers=[metric_reader])
    set_meter_provider(provider)


def get_meter(name: str):
    return get_meter_provider().get_meter(name)


def get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.info(logger.handlers.__len__)
    return logger


def get_tracer():
    return trace.get_tracer()
