
from flask import Flask, request
import json
import requests

LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer UFeWGQdl10Yt2J4OeMgG2Hgejm+IPHzcvmX9ahwnFQ3q8B1Sg3YJE/BXh7GS8qrF2qOuMFs7A8Csig9QgITZQUVbewVPEjRcG2freADCDg8ZMAs6g46um2RTCK8PPDBto7hDdexbEKPVTKHxnSUTtwdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
  headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization':Authorization
  }


app = Flask(__name__)
@app.route('/')
def index():
  return "Hello World!"

# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST'])
def callback():
  json_line = request.get_json()
  json_line = json.dumps(json_line)
  decoded = json.loads(json_line)
  user = decoded["events"][0]['replyToken']
  #id=[d['replyToken'] for d in user][0]
  #print(json_line)
  #print("ผู้ใช้：",user)
  mytext = decoded["events"][0]['message']['text']
  
  if mytext == 'บาย':
    sendSticker(user,'1','408')
  elif mytext == 'ดี':
    sendText(user,'ดีจ้าาาาา') # ส่งข้อความ งง
  elif mytext == 'พิกัด':
    sendlocation(user)
  else :
    sendText(user,'ผมไม่เข้าใจ')
 
  #sendText(user,mytext)
  return '',200


def sendText(user, text):
  data = json.dumps({
  "replyToken":user,
  "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
  
def sendSticker(user, pkid,sid):
  data = json.dumps({
  "replyToken":user,
  "messages":[{"type":"sticker","packageId": pkid,"stickerId": sid}]
  })
  r = requests.post(LINE_API, headers=headers, data=data)
  
def sendlocation(user):
  data = json.dumps({
  "replyToken":user,
  "messages":[
  {
    #"id": "325708",
    "type": "location",
    "title": "บ.มหาโชคมหาชัย เทรดดิ้ง",
    "address": "หมู่ 6 5/9 ซอยวัดคลองมะเดื่อ 17 เศรษฐกิจ 1 ตำบล คลองมะเดื่อ อำเภอ กระทุ่มแบน สมุทรสาคร 74110",
    "latitude": 35.65910807942215,
    "longitude": 13.6271373
  }]

if __name__ == '__main__':
  app.run(debug=True)