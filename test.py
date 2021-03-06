from flask import Flask, request
import json
import requests

global LINE_API
LINE_API = 'https://api.line.me/v2/bot/message/reply'
global headers
headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': 'Bearer UFeWGQdl10Yt2J4OeMgG2Hgejm+IPHzcvmX9ahwnFQ3q8B1Sg3YJE/BXh7GS8qrF2qOuMFs7A8Csig9QgITZQUVbewVPEjRcG2freADCDg8ZMAs6g46um2RTCK8PPDBto7hDdexbEKPVTKHxnSUTtwdB04t89/1O/w1cDnyilFU='
  #inputChannel access token (long-lived)  
          }

app = Flask(__name__)
@app.route('/')
def index():
  #showDisplay
  return "Welcome to MCT"

#callbackWebhook
@app.route('/callback', methods=['POST'])
def callback():
  json_line = request.get_json()
  json_line = json.dumps(json_line)
  decoded = json.loads(json_line)
  user = decoded["events"][0]['replyToken']
  #id=[d['replyToken'] for d in user][0]
  #print(json_line)
  #print("ผู้ใช้：",user)
  
  condition = decoded["events"][0]['message']['text']
  
  if condition == 'สวัสดี':
    sendSticker(user,'3','242')
  elif mytext == 'ดี':
    sendText(user,'ดีจ้าาาาา')
  elif mytext == 'No':
    sendText(user,'ขอบคุณค่ะ')
  elif mytext == 'พิกัด':
    sendlocation(user)
  elif mytext == 'ดู':
    sendCarousel(user)
  elif mytext == 'รูป':
    sendimgMap(user,'https://www.picz.in.th/images/2018/07/14/NDd6fN.jpg')
  elif mytext in "ติดต่อ":
    sendConfirm(user)
  else :
    sendText(user)
 
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
    
def sendimgMap(user,pic):
    data = json.dumps({
    "replyToken":user,
    "messages": [{
            "type": "imagemap",
            "baseUrl": pic,
            "altText": "This is an imagemap",
            "baseSize": {
              "width": 1040,
              "height": 1040
            },
            "actions": [
            {
                  "type": "uri",
                  "linkUri": "http://www.m-group.in.th/main/",
                  "area":{  
                      "x":0,
                      "y":0,
                      "width":1040,
                      "height":1040
                      }

            }
          ]
      }]

    })
    r = requests.post(LINE_API, headers=headers, data=data)
  
def sendConfirm (user):
  data = json.dumps({
  "replyToken":user,
  "messages":[{
        "type": "template",
        "altText": "MCT Confirm",
        "template": {
          "type": "confirm",
          "actions": [
            {
              "type": "message",
              "label": "No",
              "text": "No"
            },
            {
              "type": "uri",
              "label": "Call",
              "uri": "tel:034878366"
            }
          ],
          "text": "Are you sure?"
        }
      }]
  })
  r = requests.post(LINE_API, headers=headers, data=data)
  
def sendCarousel(user):
  data = json.dumps({
  "replyToken":user,
  "messages":[{
        "type": "template",
        "altText": "this is a carousel template",
        "template": {
            "type": "carousel",
            "columns": [
                {
                  "thumbnailImageUrl": "https://www.picz.in.th/images/2018/07/13/NlREUJ.png",
                  "imageBackgroundColor": "#FFFFFF",
                  "title": "เว็บ m-group",
                  "text": "เว็บ m-group description",
                  
                  "actions": [
                      {
                          "type": "postback",
                          "label": "Buy",
                          "data": "action=buy&itemid=111"
                      },
                      {
                          "type": "postback",
                          "label": "Add to cart",
                          "data": "action=add&itemid=111"
                      },
                      {
                          "type": "uri",
                          "label": "View detail",
                          "uri": "http://www.m-group.in.th"
                      }
                    
                  ]
                },
                {
                  "thumbnailImageUrl": "https://www.picz.in.th/images/2018/07/13/NlRn8I.png",
                  "imageBackgroundColor": "#000000",
                  "title": "เว็บ CRM",
                  "text": "เว็บ CRM description",
                  
                  "actions": [
                      {
                          "type": "postback",
                          "label": "Page Login",
                          "data": "action=add&itemid=222"
                      },
                      {
                          "type": "postback",
                          "label": "Add to cart",
                          "data": "action=add&itemid=222"
                      },
                      {
                          "type": "uri",
                          "label": "Call Now",
                          "uri": "tel:034878366"
                      }
                  ]
                }
            ],
            "imageAspectRatio": "rectangle",
            "imageSize": "cover"
        }
      }]
    
  })
  r = requests.post(LINE_API, headers=headers, data=data)
  
  
if __name__ == '__main__':
  app.run(debug=True)
