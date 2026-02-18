import unittest
from EmotionDetection import emotion_detector

class TestEmotion(unittest.TestCase):
    def test_case(self):
        real_result = emotion_detector('I am glad this happened')
        expected_result = 'joy'
        self.assertEqual(real_result['dominant_emotion'], expected_result)

        real_result = emotion_detector('I am really mad about this')
        expected_result = 'anger'
        self.assertEqual(real_result['dominant_emotion'], expected_result)

        real_result = emotion_detector('I feel disgusted just hearing about this')
        expected_result = 'disgust'
        self.assertEqual(real_result['dominant_emotion'], expected_result)

        real_result = emotion_detector('I am so sad about this')
        expected_result = 'sadness'
        self.assertEqual(real_result['dominant_emotion'], expected_result)

        real_result = emotion_detector('I am really afraid that this will happen')
        expected_result = 'fear'
        self.assertEqual(real_result['dominant_emotion'], expected_result)

unittest.main()


