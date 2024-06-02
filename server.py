from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None:
        return "Invalid text! Please try again!."
    else:
        response = emotion_detector(text_to_analyze)
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']
        if dominant_emotion is None:
            return "Invalid text! Please try again!."
        else: 
            return (f"For the given statement, the system response is 'anger':"
                f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " 
                f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port = 5000)