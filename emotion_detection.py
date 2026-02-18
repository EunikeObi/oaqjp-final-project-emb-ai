import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)
    formatted_text = json.loads(response.text)

    #store all emotion scores
    anger_score = formatted_text["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_text["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_text["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_text["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_text["emotionPredictions"][0]["emotion"]["sadness"]

    #find the dominant emotion
    emotions = {anger_score: "anger", disgust_score:"disgust", 
    fear_score: "fear", joy_score: "joy", sadness_score: "sadness"}
    max_score = 0
    dominant_emotion = ""
    for emotion in emotions:
        if emotion > max_score:
            max_score = emotion
            dominant_emotion = emotions[emotion]
    
    #return the result
    result = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
    return result


