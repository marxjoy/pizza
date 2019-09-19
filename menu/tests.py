from django.test import TestCase

class MenuPageTest(TestCase):
    
    def setUp(self):
        self.response = self.client.get('/')
        self.response_decode = self.response.content.decode()
    
    def test_is_page_valid(self):
        self.assertTrue(self.response_decode.startswith('<!DOCTYPE html>'))
        self.assertTrue(self.response_decode.endswith('</html>'))

    def test_menu_title(self):
        self.assertIn('<title>Pizzeria Menu</title>', self.response_decode )
        
    
    def test_menu_template(self):
        self.assertTemplateUsed(self.response, 'meal/list.html')