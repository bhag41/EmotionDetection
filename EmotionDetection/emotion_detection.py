import requests
import json

def emotion_detector(text_to_analyze):
    url1 = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    repsonse = requests.post(url1, json = input_json, headers = headers)
    data = repsonse.json()
    for dict1 in data['emotionPredictions'][0]:
        if dict1 == 'emotion':
            data_output = data['emotionPredictions'][0][dict1]
            # r = json.dumps(data_output)
            # loaded_r = json.loads(r)
            data_output_sorted = sorted(data_output.items(), key=lambda x:x[1], reverse=True)
            dict_output = dict(data_output_sorted)
            #print(json.dumps(loaded_r, indent =4))
            # print(json.dumps(dict_output, indent = 4))

    emotion_detector.dominant_emotion = next(iter(dict_output))
    #print(emotion_detector.dominant_emotion)
    dict_output["dominant_emotion"] = emotion_detector.dominant_emotion 
    #print(json.dumps(dict_output, indent = 4))
    return dict_output

if __name__ == "__main__":
    emotion_detector.run(debug=True)
