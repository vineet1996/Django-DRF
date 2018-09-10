import json
from django.test import TestCase

from ..models import Puppy
from rest_framework.reverse import reverse
from ..serializers import PuppySerializer
from rest_framework import status
from django.test import TestCase, Client
# from test_views import client
client = Client()

# GET
class GetAllPuppiesTest(TestCase):

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog',color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')
        Puppy.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
        Puppy.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')


    def test_get_all_puppies(self):
        # API response
        client = Client()
        response = client.get(reverse('get_post_puppies'))
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')
        self.rambo = Puppy.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
        self.ricky = Puppy.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_valid_single_puppy(self):
        response = client.get(reverse('get_delete_update_puppy',kwargs={'pk':self.rambo.pk}))
        puppy = Puppy.objects.get(pk=self.rambo.pk)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        response = client.get(reverse('get_delete_update_puppy',kwargs={'pk':30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# POST
class CreateNewPuppyTest(TestCase):
    def setUp(self):
        self.valid_payload={
            'name':'Muffin',
            'age':4,
            'breed':'Pamerion',
            'color':'White'
            }
        self.invalid_payload={
            'name':'',
            'age':4,
            'breed':'Pamerion',
            'color':'White'
        }

    def test_create_valid_puppy(self):
        response = client.post(reverse('get_post_puppies'),data=json.dumps(self.valid_payload),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response= client.post(reverse('get_post_puppies'),data=json.dumps(self.invalid_payload),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

# PUT
class UpdateSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = Puppy.objects.create(name='Casper',age=3,breed='Bull Dog',color='Black')
        self.muffin = Puppy.objects.create(name='Muffy',age=1,breed='Gradane',color='Brown')
        self.valid_payload = {
            'name':'Muffy',
            'age':2,
            'breed':'Labrador',
            'color':'Black'
        }
        self.invalid_payload = {
            'name':'',
            'age':4,
            'breed':'Pamerion',
            'color':'White'
        }

    def test_valid_update_puppy(self):
        response = client.put(reverse('get_delete_update_puppy',kwargs={'pk':self.muffin.pk}),data=json.dumps(self.valid_payload),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_invalid_update_puppy(self):
        response = client.put(reverse('get_delete_update_puppy',kwargs={'pk':self.muffin.pk}),data=json.dumps(self.invalid_payload),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

# DELETE
class DeleteSinglePuppyTest(TestCase):
    def setUp(self):
        self.casper = Puppy.objects.create(name='Casper',age=3,breed='Bull Dog',color='Black')
        self.muffin = Puppy.objects.create(name='Muffy',age=1,breed='Gradane',color='Brown')

    def test_valid_delete_puppy(self):
        response = client.delete(reverse('get_delete_update_puppy',kwargs={'pk':self.muffin.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(reverse('get_delete_update_puppy',kwargs={'pk':30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
