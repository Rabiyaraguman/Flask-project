from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return  "<h1>welcome to online calculator</h1>"

@app.route("/add/<num1>/<num2>")
def add(num1,num2):
    res = int(num1) + int(num2)
    return jsonify({"add" : res})

@app.route("/sub/<num1>/<num2>")
def sub(num1,num2):
    res = int(num1) - int(num2)
    return jsonify({"sub" : res})

@app.route("/mul/<num1>/<num2>")
def mul(num1,num2):
    res = int(num1) * int(num2)
    return jsonify({"mul" : res})

@app.route("/div/<num1>/<num2>")
def div(num1,num2):
    res = int(num1) / int(num2)
    return jsonify({"div" : res})
    
app.run(debug=True)