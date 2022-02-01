import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(4)
    def hello_world(self):
        self.client.get("/", name="/home")

    @task
    def invalid(self):
        self.client.get("/invalid", name="/invalid")

    @task(2)
    def view_items(self):
        for item_id in range(5):
            self.client.get(f"/items/{item_id}", name="/items")


    @task(2)
    def make_external_api_calls(self):
        for item_id in range(5):
            self.client.get("/external-api", name="/external-api")

