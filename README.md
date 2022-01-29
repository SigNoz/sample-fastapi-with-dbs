# sample-fastapi-with-dbs

```
pip3 install -r requirements.txt
```

```
opentelemetry-bootstrap --action=install
```

```
OTEL_METRICS_EXPORTER=none OTEL_RESOURCE_ATTRIBUTES=service.name=fastAPI OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument uvicorn app.main:app --port 5000 --host 0.0.0.0
```

### Notes:
redislite version with MacOSX is different than Linux, the given version at requirements.txt throws error in installation but if installed with version `redislite==1.0.210` it gets installed but throws below error on using redis inside application
```
No such file or directory: 'build/bdist.macosx-11-arm64/wheel/redislite/bin/redis-server'
```
