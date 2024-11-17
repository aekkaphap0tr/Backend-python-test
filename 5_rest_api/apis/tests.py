from django.test import TestCase
from django.urls import reverse
from apis.models import School

class SchoolAPITests(TestCase):

    def setUp(self):
        self.school_data = {
            'name': 'School_0',
            'initials': 'TS',
            'address': 'Bangkok',
        }
        self.school = School.objects.create(**self.school_data)
        self.list_url = reverse('school-list')  
        self.detail_url = reverse('school-detail', args=[self.school.id])  

    def create_school(self):
        data = {
            'name': 'School_1',
            'initials': 'NS',
            'address': 'NAN',
        }
        response = self.client.post(self.list_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(School.objects.filter(name='School_1').exists())

    def school_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.school_data['name'])

    def update_school(self):
        updated_data = {
            'name': 'School_2',
            'initials': 'H',
            'address': 'BANGNA',
        }
        response = self.client.put(self.detail_url, updated_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.school.refresh_from_db() 
        self.assertEqual(self.school.name, 'Updated School')

    def delete_school(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(School.objects.filter(id=self.school.id).exists())
