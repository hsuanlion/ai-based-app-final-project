'''
    docstring
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detect():
    '''
    docstring
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = f"""For the given statement, the system response is 'anger' \
        : {anger}, 'disgust' : {disgust}, 'fear' : {fear}, 'joy' : {joy} \
        and 'sadness' : {sadness}. The dominant emotion is {dominant_emotion}."""

    return render_template('index', system_response = response_text)


if __name__ == '__main__':
    app.run(host = "localhost", post = 5000)
