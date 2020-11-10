import unittest
import sys
sys.path.append("C:\\Users\\nana-\\data_engineer_pjt")

from src.process_and_predict import process_and_predict

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.positive_sentence="I love this incredible cookie !"
        self.neutral_sentence="I am going to school"
        self.negative_sentence="I hate studies"

    def tearDown(self):
        pass

    def test_classifier(self):
        positive_classifier=process_and_predict.classifier(self.positive_sentence)
        neutral_classifier=process_and_predict.classifier(self.neutral_sentence)
        negative_classifier=process_and_predict.classifier(self.negative_sentence)

        self.assertEqual(positive_classifier,'positive')
        self.assertEqual(neutral_classifier,'neutral')
        self.assertEqual(negative_classifier,'negative')

    def test_predict(self):

        positive_predict=process_and_predict.predict(self.positive_sentence)
        neutral_predict=process_and_predict.predict(self.neutral_sentence)
        negative_predict=process_and_predict.predict(self.negative_sentence)

        self.assertEqual(positive_predict,'positive')
        self.assertEqual(neutral_predict,'neutral')
        self.assertEqual(negative_predict,'negative')



if __name__=='__main__':
    print('function test')
    unittest.main()
