import unittest
import requests
import os

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

         
        result =b'<HTML>\n    <BODY bgcolor="green">\n    <form method="POST" action="">\n        <center>\n        <H1 title="result">prediction : __label__2 </H1> <br>\n        \n        </center>\n    </form>\n    </BODY>\n    </HTML>\n    '
    

        htmlresponse = requests.post('http://localhost:5000/',data=payload)

        #tree = html.fromstring(htmlresponse.content)

        #prediction = tree.xpath('//h1[@title="result"]/text()')
        self.assertEqual(htmlresponse.status_code,200)
        #self.assertEqual((''.join(prediction)).encode(),result.encode())
        self.assertEqual(htmlresponse.content,result)


if __name__=='__main__':
    print('integration test')
    unittest.main()