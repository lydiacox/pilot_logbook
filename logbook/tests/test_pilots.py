import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"] = "testing"

class TestPilots(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_pilot_index(self):
        response = self.client.get("/pilots/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_create_bad_pilot(self):
        response = self.client.post("/pilots/new/", json={"pilot_name": ""})
        self.assertEqual(response.status_code, 400)

    def test_create_good_pilots(self):
        response = self.client.post("/pilots/new/", json={"pilot_name": "testpilot"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["pilot_name"], "testpilot")
        self.client.delete(f"/pilots/{response.get_json()['pilot_id']}/")
    
    def test_delete_pilot(self):
        response1 = self.client.post("/pilots/new/", json={"pilot_name": "testpilot"})
        id = response1.get_json()["pilot_id"]
        response2 = self.client.delete(f"/pilots/{id}/")
        self.assertEqual(response2.status_code, 200)

    def test_update_pilot(self):
        response1 = self.client.post("/pilots/new/", json={"pilot_name": "testpilot"})
        id = response1.get_json()["pilot_id"]
        response2 = self.client.put(f"/pilots/{id}/", json={"pilot_name": "newtestpilot"})
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.get_json()["pilot_name"], "newtestpilot")
        self.client.delete(f"/pilots/{id}/")