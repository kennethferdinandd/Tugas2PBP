from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class MyWatchListTest(TestCase):

        def test_url_html(self):
            self.client = Client()
            response = self.client.get(reverse('mywatchlist:show_mywatchlist'))
            self.assertEqual(response.status_code, 200)

        def test_url_xml(self):
            self.client = Client()
            response = self.client.get(reverse('mywatchlist:show_xml'))
            self.assertEqual(response.status_code, 200)

        def test_url_json(self):
            self.client = Client()
            response = self.client.get(reverse('mywatchlist:show_json'))
            self.assertEqual(response.status_code, 200)