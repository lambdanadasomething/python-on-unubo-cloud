import os
import sys
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello():
    # return 'Welcome to Python on Unubo Cloud'
    print("Req: /")
    return render_template('index.html')

@app.route('/ver')
def ver():
    print("Req: /ver")
    return sys.version

@app.route('/ext')
def ext():
    user = request.args.get('user', default = 'guest', type = str)
    result = subprocess.run(["./extproc", user], capture_output=True, text=True, cwd=os.getcwd())
    return result.stdout

@app.route('/dirinfo')
def dirinfo():
    cur_dir = os.getcwd()
    dir_cont = os.listdir(os.getcwd())
    detail = ""
    with os.scandir(os.getcwd()) as it:
        for entry in it:
            detail = detail + str(entry.name) + ","
    return cur_dir + '|' + ','.join(dir_cont) + '|' + detail

if __name__ == '__main__':
    print("Starting up at port:" + str(port))
    os.chmod("./extproc", 0o755)
    app.run(host='0.0.0.0', port=port)
