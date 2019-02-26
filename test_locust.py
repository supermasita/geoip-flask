# Requires FAKER
#   pip install faker

from locust import HttpLocust, TaskSet, task
from faker import Faker

ok_status_codes = [200, 400]

class WebsiteTasks(TaskSet):

    @task(10)
    def ipv4_json(self):
        fake = Faker()
        with self.client.get('/api/v1.0/ip/%s' % (fake.ipv4()),
                             catch_response=True) as response:
            if response.status_code in ok_status_codes :
                response.success()

    @task(10)
    def ipv4(self):
        fake = Faker()
        with self.client.get('/%s' % (fake.ipv4()),
                             catch_response=True) as response:
            if response.status_code in ok_status_codes :
                response.success()

    @task(2)
    def ipv6(self):
        fake = Faker()
        with self.client.get('/%s' % (fake.ipv6()),
                             catch_response=True) as response:
            if response.status_code in ok_status_codes :
                response.success()

    @task(2)
    def ipv6_json(self):
        fake = Faker()
        with self.client.get('/api/v1.0/ip/%s' % (fake.ipv6()),
                             catch_response=True) as response:
            if response.status_code in ok_status_codes :
                response.success()


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 1
    max_wait = 10
