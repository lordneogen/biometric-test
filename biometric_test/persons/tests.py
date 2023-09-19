from django.test import TestCase
# from django.urls import reverse
from .models import Persons

class ArticleTestCase(TestCase):
    def setUp(self):
        self.person = Persons.objects.create(iin=111,name='Джон')
    def test_case_1(self):
        self.assertEqual(self.person.iin, 111)
        self.assertEqual(self.person.name, "Джон")
    def test_case_2(self):
        perseon_id = Persons.objects.get(iin=111)
        self.assertEqual(perseon_id.iin,111)
        self.assertEqual(perseon_id.name,'Джон')
    def test_case_3(self):
        response = self.client.get('/person/')
        self.assertEqual(response.status_code, 200)
    def test_case_4(self):
        response = self.client.get('/person/111/')
        self.assertEqual(response.status_code, 200)
    def test_case_5(self):
        response = self.client.get('/person/112/')
        self.assertEqual(response.status_code, 404)