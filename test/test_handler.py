import unittest
from src import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        event={'Country':'USA'}
        result = index.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello from '+event['Country'], result['body'])
        event={'Country':'INDIA'}
        result = index.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello from '+event['Country'], result['body'])


if __name__ == '__main__':
    unittest.main()
