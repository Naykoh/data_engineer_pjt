import unittest
import requests
import os
from lxml import html

class FlaskTest(unittest.TestCase):
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        self.data={
            'sentence':'I love this incredible cookie !'
        }

    def tearDown(self):
        pass

    
    def test_predict(self):
        payload = {
            'sentence':self.data['sentence'],
            'form_type':'predict',
        }

        result = "prediction : __label__2 "

        htmlresponse = requests.post('http://localhost:5000/',data=payload)

        tree = html.fromstring(htmlresponse.content)

        prediction = tree.xpath('//h1[@title="result"]/text()')

        self.assertEqual(htmlresponse.status_code,200)
        self.assertEqual((''.join(prediction)).encode(),result.encode())

if __name__=='__main__':
    unittest.main()