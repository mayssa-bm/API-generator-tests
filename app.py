from flask import Flask, render_template
from random import randrange
import requests
import json

from requests import api

app = Flask(__name__)

@app.route('/')
def get_beer():
    r = requests.get('https://api.publicapis.org/entries')
    rjson = r.json()
    rand = randrange(940)
    ap = {
        'API': rjson['entries'][rand]['API'],
        'Description': rjson['entries'][rand]['Description'],
        'Link': rjson['entries'][rand]['Link'],
        'Category': rjson['entries'][rand]['Category'],
    }
   
    return render_template('index.html', ap=ap)