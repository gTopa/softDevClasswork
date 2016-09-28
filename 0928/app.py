from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def disp_loginpage():
    print "\n\n\n"
    print ":::DIAG::: this Flask obj"
    print app
    print ":::DIAG::: this request obj"
    print request
    print ":::DIAG::: this request.headers obj"
    print request.headers
    print ":::DIAG::: this request.method obj"
    print request.method
    print ":::DIAG::: this request.args obj"
    print request.args
    print ":::DIAG::: this request.form obj"
    print request.form
    return render_template("input.html")

@app.route("/auth")
def disp_auth():
    print "\n\n\n"
    print ":::DIAG::: this Flask obj"
    print app
    print ":::DIAG::: this request obj"
    print request
    print ":::DIAG::: this request.headers obj"
    print request.headers
    print ":::DIAG::: this request.method obj"
    print request.method
    print ":::DIAG::: this request.args obj"
    print request.args
    print ":::DIAG::: this request.form obj"
    print request.form
    return "WOOOOOOOOOO"

if __name__ == "__main__":
    app.debug = True
    app.run()
