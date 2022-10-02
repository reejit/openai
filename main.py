from flask import Flask, request, render_template, redirect
import requests
#from nekobin import NekoBin, errors
#import asyncio
import time
from app import write
#
#print(r)
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
async def home():
 if request.method == "POST":
    print(request.form["query"])
    r = write(query=request.form["query"]).encode('utf-8')
    print(r)
    resp = requests.post("https://paste.rs/", r)
    r = resp.text
    print(r)
    time.sleep(2)
    return f"<h1><center><a href=\"{r}\">Your Answer</a></center></h1>"

    
    
     
 return render_template('index.html')

app.run()
