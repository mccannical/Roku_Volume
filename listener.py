from flask import Flask
from roku import Roku
app = Flask(__name__)

roku = Roku('192.168.1.2') # change to the IP address of your Roku TV

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/up")
def volup():
    for lvls in range(5):
        roku.volup()
    return "louder!"

@app.route("/down")
def voldn():
    for lvls in range(5):
        roku.voldn()
    return "Shhh..."

@app.route("/power")
def power_tog():
    roku.power()
    return "power"
