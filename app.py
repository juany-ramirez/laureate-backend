import os

import requests
import json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DEVELOPER_KEY = "AIzaSyCcdzClrKE6FrsDce4FrnXroYcHohB1zMc" 


@app.route('/')
def get_data():
    site = 'https://www.googleapis.com/youtube/v3/search?'
    key = 'key='+'AIzaSyCcdzClrKE6FrsDce4FrnXroYcHohB1zMc'
    channelId = '&channelId='+'UCvS6-K6Ydmb4gH-kim3AmjA'
    part = '&part=snippet,id&order=date'
    r = requests.get(site+key+channelId+part)
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )

@app.route('/<pageToken>')
def profile(pageToken):
    site = 'https://www.googleapis.com/youtube/v3/search?'
    key = 'key='+'AIzaSyCcdzClrKE6FrsDce4FrnXroYcHohB1zMc'
    channelId = '&channelId='+'UCvS6-K6Ydmb4gH-kim3AmjA'
    part = '&part=snippet,id&order=date'
    nextPageToken = '&pageToken='+pageToken
    r = requests.get(site+key+channelId+part+nextPageToken)
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )


@app.route('/prueba', methods=['GET','POST'])
def jsonf():
    return jsonify({"key":[0,1,2,3]})


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port, debug=True)