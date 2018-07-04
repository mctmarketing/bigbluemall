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
    replyStack = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    mytext = msg_in_json["events"][0]['message']['text']
    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    #replyStack.append('นี่คือรูปแบบข้อความที่รับส่ง')
    sendtext = 'งง'
    #Trainning Bot
    '''if mytext == 'ดี':
       sendtext = 'ดีจ้า'
     
    if mytext == 'ดีค่ะ':
       sendtext = 'สวัสดีค่ะ'
     
    if mytext == 'ดีครับ':
        sendtext = 'สวัสดีครับ'
      
     if mytext == 'hello':
        sendtext = 'Hi!..'
      '''
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    replyStack.append(msg_in_string)
    reply(replyToken, sendtext)
    
    return 'OK',200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    '''msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })'''
    data = json.dumps({
        "replyToken":replyToken,
        "messages":[{"type":"text","text":textList}]
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()
