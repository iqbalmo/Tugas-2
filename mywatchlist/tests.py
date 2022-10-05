from django.test import TestCase
from django.test import Client

# Create your tests here.
class UnitTest(TestCase):

    def test_json_is_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def test_xml_is_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_html_is_exist(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)