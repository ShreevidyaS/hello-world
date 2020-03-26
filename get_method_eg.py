from flask import Flask, redirect, url_for
app = Flask(__name__)

#statis route
@app.route("/welcome")
def hellow():
    return "Hello world!"

#dynamic route
@app.route("/<name>")
def printname(name):
    return f"hello {name}!"

#redirect to another page if opened a page that is not for the user(say)
@app.route("/admin")
def admin():
    return redirect(url_for("printname", name="Admin!"))

if(__name__=='__main__'):
    app.run(debug=True, host="localhost", port= 3000)
