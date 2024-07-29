import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome', result.data)

    def test_get_products(self):
        result = self.app.get('/products')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Laptop', result.data)

    def test_get_product(self):
        result = self.app.get('/products/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Laptop', result.data)

    def test_404(self):
        result = self.app.get('/non-existent')
        self.assertEqual(result.status_code, 404)

if __name__ == "__main__":
    unittest.main()

