from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นางสาวภคนันท์ จันทโกวิท เลขที่ 12ชั้น ม.4/2 "

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    userText = decoded["events"][0]['message']['text']
    if (userText == 'อีหยังว้ะ'):
    sendText(user,'หิวเมื่อไรก็เเวะมาเซเว่น')
    if (userText == 'เหงาหรอ'):
    sendText(user,'เหงามากๆ')
    if (userText  == 'เหงาก็ไปหาไรทำสิ'):
    sendText(user,'ขี้เกียจ') :
    if (userText == 'สวัสดี') :
    sendText(user,'เออดีด้วย')
    elif (userText == 'ไอ้บ้า') :
    sendText(user,'เอ็งซิบ้า')
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
