from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import Client

class test_account_module(TestCase):
    sample_user = {'username': 'Jan123',
                  'password': 'baba1234',
                  'first_name': 'John',
                  'last_name': 'Smith',
                  'email': 'john@smith.org',
                       }
    
    def setUp(self):
        User.objects.create(username=self.sample_user['username'],
                            password=self.sample_user['password'])
        user = User.objects.get(username=self.sample_user['username'])
        user.first_name = self.sample_user['first_name']
        user.last_name = self.sample_user['last_name']
        user.email = self.sample_user['email']
        user.save()
        self.client = Client()
        
        
    def tearDown(self):
        pass


    def test_sample_user_exist(self):
        user = User.objects.get(username=self.sample_user['username'])
        self.assertEqual(user.username, self.sample_user['username'])
        self.assertEqual(user.last_name, self.sample_user['last_name'])
        self.assertEqual(user.first_name, self.sample_user['first_name'])


    def test_view_register_resolves(self):
        resolver = resolve('/account/register/')
        self.assertEqual(resolver.view_name, 'register')


    def test_response_for_account_register_url(self):
        response = self.client.get('/account/register/')
        self.assertEqual(response.status_code, 200)


    def test_response_for_account_edit_url(self):
        response = self.client.get('/account/edit/')
        self.assertEqual(response.status_code, 302)


    def test_response_for_account_login_url(self):
        response = self.client.get('/account/login/')
        self.assertEqual(response.status_code, 200)


    def test_register_reverse(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)


    def test_login_reverse(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


    def test_login_content(self):
        response = self.client.get(reverse('login'))
        self.assertIn(b'Login', response.content)
        