"""
Flask server for Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def main():
    """Analyze text and return detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    if dominant is None:
        return_text = "Invalid text! Please try again!"
    else:
        return_text = (f"For the given statement, the system response is 'anger': {anger},"
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}."
        f" The dominant emotion is {dominant}")
    return return_text

@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
