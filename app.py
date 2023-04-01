from flask import Flask,request
import os,sys
from werkzeug.serving import run_simple

app=Flask(__name__)

def refresh():
    with open(__file__,'w') as fo:
        with open('target.py','r') as f2:
            fo.writelines(f2.readlines())
    with open(__file__) as fo:
        source_code = fo.read()
        byte_code = compile(source_code, __file__, "exec")
        # exec(byte_code)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        exit()

@app.route('/')
def home():
    return '1'

@app.route('/add')
def add():
    refresh()
    return '12'

@app.route('/shutdown')
def shutdown():
    shutdown_func=request.environ.get('werkzeug.server.shutdown')
    shutdown_func()
    raise RuntimeError


        

if __name__=='__main__':
    run_simple('0.0.0.0',8000,app,use_debugger=True,use_reloader=False)
    # app.run(host='0.0.0.0')
