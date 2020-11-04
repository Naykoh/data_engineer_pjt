import unittest
import os
import sys
sys.path.append("C:\\Users\\nana-\\data_engineer_pjt")
from src.process_and_predict import process_and_predict
import string



class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.sentence="I love this incredible cookie !"

    def tearDown(self):
        pass

    def test_process(self):
        result = "['love', 'incredible', 'cookie']"

        processed_sentence=process_and_predict.process(self.sentence)

        self.assertEqual(processed_sentence,result)

    def test_predict(self):
        #processed_sentence= "this product is nice"
        processed_sentence="['love', 'incredible', 'cookie']"
    
        prediction = process_and_predict.predict(processed_sentence)

        self.assertEqual(prediction,"__label__2 ")



if __name__=='__main__':
    unittest.main()