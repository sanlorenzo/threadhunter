from flask import Flask, request
import requests
import os

app = Flask(__name__)

SLACK_CLIENT_ID = os.environ.get("SLACK_CLIENT_ID")
SLACK_CLIENT_SECRET = os.environ.get("SLACK_CLIENT_SECRET")

@app.route('/')
def home():
    return 'ThreadHunter online.'

@app.route('/slack/oauth/callback')
def oauth_callback():
    code = request.args.get('code')
    if not code:
        return 'No code provided.'

    response = requests.post("https://slack.com/api/oauth.v2.access", data={
        "client_id": SLACK_CLIENT_ID,
        "client_secret": SLACK_CLIENT_SECRET,
        "code": code
    })

    return f"Slack OAuth response: {response.json()}"

