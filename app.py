import requests
import json
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

DEVELOPER_KEY = "AIzaSyCcdzClrKE6FrsDce4FrnXroYcHohB1zMc" 


@app.route('/')
def get_data():
    site = 'https://www.googleapis.com/youtube/v3/search?'
    key = 'key='+'AIzaSyCcdzClrKE6FrsDce4FrnXroYcHohB1zMc'
    channelId = '&channelId='+'UCvS6-K6Ydmb4gH-kim3AmjA'
    part = '&part=snippet,id&order=date'
    nextPageToken = '&pageToken='
    r = requests.get(site+key+channelId+part)
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )

@app.route('/prueba', methods=['GET','POST'])
def jsonf():
    return jsonify({"key":[0,1,2,3]})

