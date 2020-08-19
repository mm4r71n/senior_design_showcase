from django.test import TestCase, Client
from django.urls import reverse

from .models import Listing

import json

class TestViews(TestCase):
    def test_view(self):
        client = Client()

        response = client.get(reverse('listings'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'Contruction_App/index.html')



