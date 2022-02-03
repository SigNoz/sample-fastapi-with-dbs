# sample-fastapi-with-dbs

### Simple Fast API app with MongoDB and Redislite

To show how you can see metrics for External calls and DB calls in FastAPI app, we have created a sample app which uses a database (MongoDB) so that the example is more realistic

If you already have Mongo daemon running, you can skip the following step to install Mongo

Download MongoDB for:
- Mac from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
- Linux from https://docs.mongodb.com/manual/administration/install-on-linux/
- Ubuntu from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

### Set up instructions

```
pip3 install -r requirements.txt
```

```
opentelemetry-bootstrap --action=install
```

### Run the sample app

```
OTEL_METRICS_EXPORTER=none OTEL_RESOURCE_ATTRIBUTES=service.name=fastAPI OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument uvicorn app.main:app --port 5001 --host 0.0.0.0
```
