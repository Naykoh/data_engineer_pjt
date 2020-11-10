import unittest
import requests
import os

class FlaskTest(unittest.TestCase):
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        self.sentences={
                        'positive_sentence':'I love this incredible cookie !',
                        'neutral_sentence':'I am going to school',
                        'negative_sentence':'I hate studies'
                        }

    def tearDown(self):
        pass

    
    def test_predict(self):
        payload_positive = {
            'sentence':self.sentences['positive_sentence'],
            'form_type':'predict',
        }

        payload_neutral = {
            'sentence':self.sentences['neutral_sentence'],
            'form_type':'predict',
        }

        payload_negative = {
            'sentence':self.sentences['negative_sentence'],
            'form_type':'predict',
        }

        positive_result =b'<HTML>\n<BODY bgcolor="green">\n<form method="POST" action="">\n    <center>\n    <H1>Sentiment analysis </H1> <br>\n    Sentence <input type = "text" name = "sentence" /> <br>\n    <input type="hidden" name="form_type" value="predict"/>\n    <input type = "submit"><br>\n    <img name="sentiment-face" src="/static/sourire.png"> <br>\n    <H1 title="result">prediction : positive</H1> <br>\n    </center>\n</form>\n</BODY>\n</HTML>'

        neutral_result = b'<HTML>\n<BODY bgcolor="green">\n<form method="POST" action="">\n    <center>\n    <H1>Sentiment analysis </H1> <br>\n    Sentence <input type = "text" name = "sentence" /> <br>\n    <input type="hidden" name="form_type" value="predict"/>\n    <input type = "submit"><br>\n    <img name="sentiment-face" src="/static/neutral.png"> <br>\n    <H1 title="result">prediction : neutral</H1> <br>\n    </center>\n</form>\n</BODY>\n</HTML>'

        negative_result =b'<HTML>\n<BODY bgcolor="green">\n<form method="POST" action="">\n    <center>\n    <H1>Sentiment analysis </H1> <br>\n    Sentence <input type = "text" name = "sentence" /> <br>\n    <input type="hidden" name="form_type" value="predict"/>\n    <input type = "submit"><br>\n    <img name="sentiment-face" src="/static/triste.png"> <br>\n    <H1 title="result">prediction : negative</H1> <br>\n    </center>\n</form>\n</BODY>\n</HTML>'
    
        


        htmlresponse = requests.post('http://localhost:5000/',data=payload_positive)
        self.assertEqual(htmlresponse.status_code,200)
        self.assertEqual(htmlresponse.content,positive_result)

        htmlresponse = requests.post('http://localhost:5000/',data=payload_neutral)
        self.assertEqual(htmlresponse.status_code,200)
        self.assertEqual(htmlresponse.content,neutral_result)

        htmlresponse = requests.post('http://localhost:5000/',data=payload_negative)
        self.assertEqual(htmlresponse.status_code,200)
        self.assertEqual(htmlresponse.content,negative_result)


if __name__=='__main__':
    print('integration test')
    unittest.main()