from flask import Flask, Response
import sys


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return Response(
    f"It works!\n\nPython {sys.version.split()[0]}\n",
    mimetype="text/plain"
  )

if __name__ == "__main__":
  app.run()
