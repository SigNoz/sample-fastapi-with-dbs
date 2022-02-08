# sample-fastapi-with-dbs

### Simple Fast API app with MongoDB and Redis


To show how you can see metrics for External calls and DB calls in FastAPI app, we have created a sample app which uses a database (MongoDB) so that the example is more realistic

## Run using docker-compose
- Git clone this repo
```

git clone https://github.com/SigNoz/sample-fastapi-with-dbs.git

```
Change `OTEL_EXPORTER_OTLP_ENDPOINT` env variable in [docker-compose.yaml](https://github.com/SigNoz/sample-fastapi-with-dbs/blob/main/docker-compose.yaml#L13) file to send data to SigNoz.
```
- OTEL_EXPORTER_OTLP_ENDPOINT=<IP of SigNoz>:4317
```


and then run:
```
docker-compose up -d
```

Application would be available at [http://localhost:5000/](http://localhost:5000/). Browse and generate some data.

Or just run the following command from the terminal of your VM a few times to make some API calls to the sample app. This should return `Hello World` 


```
 curl http://localhost:5000  
```

## Run sample app without docker

#### Install Mongo

If you already have Mongo daemon running, you can skip the following step to install Mongo

Download MongoDB for:
- Mac from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
- Linux from https://docs.mongodb.com/manual/administration/install-on-linux/
- Ubuntu from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

#### Install Redis

You need to install redis server. For example if you are on Ubuntu, you can use the following
```
sudo apt-get install redis-server
```

### Set up instructions

```
pip3 install -r requirements.txt
```

```
opentelemetry-bootstrap --action=install
```

### Run the sample app

```
OTEL_METRICS_EXPORTER=none OTEL_RESOURCE_ATTRIBUTES=service.name=fastAPI OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument uvicorn app.main:app --port 5000 --host 0.0.0.0
```

## Send load to application

```
pip3 install locust
```
```
locust -f locust.py --headless --users 10 --spawn-rate 1 -H http://localhost:5000
```
