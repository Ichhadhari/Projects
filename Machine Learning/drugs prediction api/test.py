import requests
import json 


#predict =  requests.post("http://127.0.0.1:8000/drugs/?age=68&gender=0&bp=2&cholesterol=2&salt=27")
predict =  requests.post("http://54.238.11.99/?age=68&gender=0&bp=2&cholesterol=2&salt=27")

'''url = "http://54.238.11.99/"

data = {
    "age": 68,
    "gender": 0,
    "bp": 2,
    "cholesterol":2,
    "salt":27,
}

predict=requests.post(url, json=data) #response 500'''
print(predict)
print("predict status code: ", predict.status_code)

if predict.status_code == 200:
    print("predict : ", predict.content)
    messages=json.loads(predict.text)
    print(type(messages))
    out=messages['Predicted_drug'][0]
    print(out)
    
