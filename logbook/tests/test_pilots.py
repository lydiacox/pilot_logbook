import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"] = "testing"

class TestFlights(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_flight_index(self):
        response = self.client.get("/flights/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Flight Index</h1>', response.data)

    def test_create_bad_flight(self):
        response = self.client.post("/flights/", data={"flight_no": ""})
        self.assertEqual(response.status_code, 400)

    def test_create_good_flights(self):
        response = self.client.post("/flights/", data={"flight_no": "testflight"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["flight_no"], "testflight")
        self.client.delete(f"/flights/{response.get_json()['flight_id']}/")
    
    def test_delete_flight(self):
        response1 = self.client.post("/flights/", data={"flight_no": "testflight"})
        id = response1.get_json()["flight_id"]
        response2 = self.client.delete(f"/flights/{id}/")
        self.assertEqual(response2.status_code, 200)

    def test_update_flight(self):
        response1 = self.client.post("/flights/", data={"flight_no": "testflight"})
        id = response1.get_json()["flight_id"]
        response2 = self.client.put(f"/flights/{id}/", json={"flight_no": "newtestflight"})
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.get_json()["flight_no"], "newtestflight")
        self.client.delete(f"/flights/{id}/")