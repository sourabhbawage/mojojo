from flask import Flask,render_template,request,url_for
import json

app = Flask(__name__)

@app.route('/getSentiment')
def getSentiment():
   return "Negative : 1 Positive: 2 Neutral:0"

@app.route('/priceinfo/<exchange>')
def priceinfo(exchange):
    return render_template("datasales.json")

@app.route('/simulate')
def simulate():
    result = request.form
    return render_template("datasales.json")

@app.route('/dashboard')
def dashboard():
   return render_template("dashboard.html")

@app.route('/renderinfo')
def renderInfo():
   with open("./templates/datasales.json", "r") as read_file:
      x = json.load(read_file)
   return render_template("display.html",placeholder=x)

if __name__ == '__main__':
   app.run()