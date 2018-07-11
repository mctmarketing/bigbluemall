
from flask import Flask, request
import json
import requests

global LINE_API
LINE_API = 'https://api.line.me/v2/bot/message/reply'
global headers
headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': 'Bearer UFeWGQdl10Yt2J4OeMgG2Hgejm+IPHzcvmX9ahwnFQ3q8B1Sg3YJE/BXh7GS8qrF2qOuMFs7A8Csig9QgITZQUVbewVPEjRcG2freADCDg8ZMAs6g46um2RTCK8PPDBto7hDdexbEKPVTKHxnSUTtwdB04t89/1O/w1cDnyilFU='
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
  elif mytext == 'ดู':
    sendCarousel(user)
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
      "latitude": 13.6271373,
      "longitude": 100.2878033
    }]
  })
  r = requests.post(LINE_API, headers=headers, data=data)
  
def sendCarousel(user):
  data = json.dumps({
  "replyToken":user,
  "messages":[{
      "type": "imagemap",
      "baseUrl": "http://mgroup.dyndns.org/crm/mystorage/Pic1.jpg",
      "altText": "This is an imagemap",
      "baseSize": {
        "width": 1040,
        "height": 1040
      },
      "actions": []
    
  }]
  '''"messages":[
    {
      "type": "template",
      "altText": "MCT template",
      "template": {
        "type": "carousel",
        "actions": [],
        "columns": [
          {
            "thumbnailImageUrl": "http://mgroup.dyndns.org/crm/mystorage/Pic1.jpg",
            "title": "เว็บสินค้า",
            "text": "มีสินค้ามากมาย",
            "actions": [
              {
                "type": "message",
                "label": "กดเพื่อดูวิธีการ",
                "text": "Action 1"
              }
            ]
          },
          {
            "thumbnailImageUrl": "http://mgroup.dyndns.org/crm/mystorage/Pic2.jpg",
            "title": "CRM MCT",
            "text": "CRM ",
            "actions": [
              {
                "type": "message",
                "label": "กดเพื่อดูเกร็ดน่ารู้",
                "text": "Action 1"
              }
            ]
          }
        ]
      }
    }]'''
  })
  r = requests.post(LINE_API, headers=headers, data=data)
  
  
if __name__ == '__main__':
  app.run(debug=True)
