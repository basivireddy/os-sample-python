from flask import Flask
import time
application = Flask(__name__)

@application.route("/")
def hello():
    time.sleep(1)
    return "Hello World!"

if __name__ == "__main__":
    application.run()
