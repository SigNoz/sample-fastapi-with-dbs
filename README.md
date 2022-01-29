# sample-fastapi-with-dbs

```
pip3 install -r requirements.txt
```

```
opentelemetry-bootstrap --action=install
```

```
OTEL_METRICS_EXPORTER=none OTEL_RESOURCE_ATTRIBUTES=service.name=fastAPI OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument uvicorn app.main:app --port 5000
```