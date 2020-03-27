from flask import Flask, url_for, redirect, request, render_template, make_response
app = Flask(__name__)

@app.route("/success/<nname>")
def success(nname):
    return f"Welcome {nname}"

@app.route("/login", methods= ["POST"])
def login():
    if request.method == 'POST':
        # to create header
        # my_res = make_response (">>>from make_response....")
        # my_res.headers['My Header'] = 'header text!!!!!!!'
        # my_res.status_code = 403
        # my_res.mimetype = 'video/mp4'
        # return my_res

        # to set status code
        # return redirect("http://google.com"), 302
        
        uname = request.form['name']
        return redirect(url_for('success', nname = uname))
             

@app.route("/")
def home():
    return render_template("post_method_eg.html")

if(__name__=='__main__'):
    app.run(debug=True)
