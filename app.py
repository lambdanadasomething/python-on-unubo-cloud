import os
import sys
from flask import Flask, render_template

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

if __name__ == '__main__':
    print("Starting up at port:" + str(port))
    app.run(host='0.0.0.0', port=port)
