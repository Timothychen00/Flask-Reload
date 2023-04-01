from flask import Flask
import requests
from werkzeug.serving import run_simple

app=Flask(__name__)
# requests.get('http://127.0.0.1:8000/shutdown')

@app.route('/')
def home():
    return "hello"

if __name__=='__main__':
    run_simple('0.0.0.0',8000,app,use_debugger=True,use_reloader=False)
    # app.run(host='0.0.0.0')
