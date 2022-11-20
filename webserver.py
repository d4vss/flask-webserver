import os, logging
from flask_cors import CORS
from threading import Thread

log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
  return 'https://github.com/d4vss'

def run():
  app.run(host="0.0.0.0", port=80)
  
def thread_start():
  Thread(target=run).start()

thread_start()