from flask import Flask,request,url_for,redirect,render_template
import time
import json


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upcase")
def upcase():
    data = request.args.get("text")
    print data
    
    time.sleep(5)
    
    result = {'original':data,
              'result':data.upper()
    }
    
    return json.dumps(result)




if __name__=="__main__":
   app.debug=True
   app.run()
