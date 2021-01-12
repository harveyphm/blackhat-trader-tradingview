from flask import request, jsonify, render_template 
import json

from ..app import app 
from .tradingview import TradingviewConfig

SITENAME = "Blackhat Trader"

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Harvey'}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html',
							sitename = SITENAME,
							title='Home', 
							user=user, 
							posts = posts)

@app.route('/tradingview', methods = ['POST'])
def tradingview_callback():
    data = json.loads(request.data)

    if data['passphrase'] != TradingviewConfig.WEBHOOK_PASSPHRASE:
        return {
        "code" : "444",
        "message": "invalid passphrase"
        }
    
    return data