from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    ticket = request.form['ticket']
    # Trigger n8n webhook
    requests.post("http://n8n:5678/webhook/ticket", json={"ticket": ticket})
    return "Ticket submitted!"