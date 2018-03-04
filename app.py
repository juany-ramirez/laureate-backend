import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

DEVELOPER_KEY = "AIzaSyCcdzClrKE6FrsDce4FrnXroYcHohB1zMc" 

@app.route('/')
def home():
    return 'Hello World'

@app.route('/prueba', methods=['GET','POST'])
def jsonf():
    return jsonify({"key":[0,1,2,3]})

@app.route('/items')
def get_data():
    site = 'https://www.googleapis.com/youtube/v3/search?'
    key = 'key='+'AIzaSyCcdzClrKE6FrsDce4FrnXroYcHohB1zMc'
    channelId = '&channelId='+'UCvS6-K6Ydmb4gH-kim3AmjA'
    part = '&part=snippet,id&order=date'
    nextPageToken = '&pageToken='
    r = requests.get(site+key+channelId+part)
    return r.text

