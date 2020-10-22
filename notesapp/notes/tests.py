from django.test import TestCase

import datetime
from django.utils import timezone
from .models import User, Bin, Note
from django.urls import reverse


class UserModelTest(TestCase):

    def test_with_username_and_password(self):
        '''  will work normally'''
        user=User(username="jkl",password="jkl")
        self.assertEquals(str(user),"jkl")


class IndexViewTest(TestCase):
    def test_with_integer_params(self):
        user=User.objects.create(username='abc',password='123')
        response=self.client.get(reverse('notes:index' , args=[user.id]))
        self.assertEquals(response.status_code,200)

        









# Create your tests here.
