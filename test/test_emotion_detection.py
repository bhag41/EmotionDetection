import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestMyModule(unittest.TestCase):
    def test_emotions(self):
        test_input = 'I am glad this happened' 
        model_output = emotion_detector(test_input)
        expected_output = 'joy'
        self.assertEqual(model_output['dominant_emotion'], expected_output)
        
        test_input = 'I am really mad about this' 
        model_output = emotion_detector(test_input)
        expected_output = 'anger'
        self.assertEqual(emotion_detector.dominant_emotion, expected_output)

        test_input = 'I feel disgusted just hearing about this.' 
        model_output = emotion_detector(test_input)
        expected_output = 'disgust'
        self.assertEqual(model_output['dominant_emotion'], expected_output)

        test_input = 'I am so sad about this.' 
        model_output = emotion_detector(test_input)
        expected_output = 'sadness'
        self.assertEqual(model_output['dominant_emotion'], expected_output)

        test_input = 'I am really afraid that this will happen.' 
        model_output = emotion_detector(test_input)
        expected_output = 'fear'
        self.assertEqual(model_output['dominant_emotion'], expected_output)

if __name__ == '__main__':
    unittest.main()