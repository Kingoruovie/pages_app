from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    """Making simple test to check webpage response"""

    def test_for_response_of_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_for_response_of_aboutpage(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)