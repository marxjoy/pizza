import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\komputer\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
        
    def tearDown(self):
        self.browser.quit()

        
    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Pizzeria', self.browser.title)
        
        
        
    
if __name__ == '__main__':
    unittest.main()