import time

from opentelemetry import metrics


from opentelemetry.exporter.otlp.metrics_exporter import OTLPMetricsExporter

from opentelemetry.sdk.metrics import Counter, MeterProvider
from opentelemetry.sdk.metrics.export import MetricsExportResult
from opentelemetry.sdk.metrics.export.aggregate import CounterAggregator
from opentelemetry.sdk.resources import Resource

# Настройка метрик и экспортера
metrics.set_meter_provider(MeterProvider())
metrics.get_meter_provider().start_pipeline(
    meter_exporter=OTLPMetricsExporter(
        endpoint="http://tempo-url:9411",
        insecure=True,
    ),
    label_encoder=None,
    resource=Resource.create({}),
)

# Создание метрик
meter = metrics.get_meter(__name__)
counter = meter.create_counter(
    name="my_counter",
    description="A simple counter",
    unit="1",
)

# Периодическая отправка метрик
while True:
    counter.add(1)
    time.sleep(10)  # Ожидание 60 секунд перед отправкой следующей метрики
