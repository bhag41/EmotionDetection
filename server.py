"""server side code to deploy emotion detection app + server side error handling."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_server():
    """
    function to retrieve input text, call emotion detector function and return results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == '':
        return "Invalid text! Please try again!."

    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    emotion_ratings_1 = f"'anger': {anger}, 'disgust': {disgust}, "
    emotion_ratings_2 = f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}."
    result_text_1 = "For the given statement, the system response is "
    result_text_2 = f"{emotion_ratings_1} {emotion_ratings_2}"
    result_text_3 = f"The dominant emotion is {dominant_emotion}."
    result_text = result_text_1 + result_text_2 + result_text_3
    return result_text

@app.route("/")
def render_index_page():
    """ render index plage """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port = 5000)
