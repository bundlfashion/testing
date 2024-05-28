from flask import flask
import os

app = flask(__name__)
@app.route('/')

def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get(port, '8080'))

