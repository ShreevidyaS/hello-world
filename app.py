from flask import Flask
app = Flask(__name__)
@app.route("/hw")
def hellow():
    return "Hello world!"

@app.route("/name")
def printname():
    return "shree"

if(__name__=='__main__'):
    app.run(debug=True, host="localhost", port= 3000)
