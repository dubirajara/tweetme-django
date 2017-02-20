from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def test_get(self):
        """GET 'Home' must return status code 200"""
        response = self.client.get(r('home'))
        self.assertEqual(200, response.status_code)

    def test_html(self):
        """'Home' must use template index.html and base.html"""
        response = self.client.get(r('home'))
        self.assertTemplateUsed(response, 'index.html')