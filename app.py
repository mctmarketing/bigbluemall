from flask import Flask, request
import json
import requests

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
LINE_API_KEY = 'Bearer UFeWGQdl10Yt2J4OeMgG2Hgejm+IPHzcvmX9ahwnFQ3q8B1Sg3YJE/BXh7GS8qrF2qOuMFs7A8Csig9QgITZQUVbewVPEjRcG2freADCDg8ZMAs6g46um2RTCK8PPDBto7hDdexbEKPVTKHxnSUTtwdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Chatbot.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    #---replyStack = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    #---msg_in_string = json.dumps(msg_in_json)
    msg_in_json = json.dumps(msg_in_json)
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    #---
    replyToken = msg_in_json["events"][0]['replyToken']

    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    #replyStack.append('นี่คือรูปแบบข้อความที่รับส่ง')
    
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    #---replyStack.append(msg_in_string)
    #---reply(replyToken, replyStack[:5])
    reply(replyToken, 'งง')
    
    return 'OK',200
 
'''def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    msgs.append('สวัสดีจ้า')
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
            })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return
'''

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
  data = json.dumps({
  "replyToken":user,
  "messages":[{"type":"text","text":text}]})
  #print("ข้อมูล：",data)
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
  #print(r.text)
  
  
if __name__ == '__main__':
    app.run()
