import os, asyncio
from fastapi import FastAPI
import requests
from mongoengine import connect, disconnect
import redislite
import models


import random
random.seed(54321)


app = FastAPI()
mongoConnection = None
redisConnection = None

DATABASE_NAME = "testDB"
DATABASE_URL = None

def createDatabaseUrl():
    global DATABASE_URL
    db_host = os.getenv('DB_HOST', "127.0.0.1")
    db_url = "mongodb://{}:27017/{}".format(db_host, DATABASE_NAME)
    print("Connecting to DB: ", db_url)
    DATABASE_URL = db_url

@app.on_event("startup")
async def create_db_client():
    # start client here and reuse in future requests
    global mongoConnection
    mongoConnection = connect(host=createDatabaseUrl())


@app.on_event("shutdown")
async def shutdown_db_client():
    # stop your client here
    print("Disconnecting from DB: ", DATABASE_URL)
    disconnect(mongoConnection)


@app.get("/")
async def read_root():
    s1=models.Student(studentid='A001', name='Tara', age=20)
    s1.save()

    r = redislite.StrictRedis()
    r.set('foo', 'bar')
    r.get('foo')

    return {"Hello": "World"}


@app.get("/ping")
async def health_check():
    return "pong"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if item_id % 2 == 0:
        # mock io - wait for x seconds
        seconds = random.uniform(0, 3)
        await asyncio.sleep(seconds)
    return {"item_id": item_id, "q": q}


@app.get("/invalid")
async def invalid():
    raise ValueError("Invalid ")


@app.get("/external-api")
def external_api():
    seconds = random.uniform(0, 3)
    response = requests.get(f"https://httpbin.org/delay/{seconds}")
    response.close()
    return "ok"


