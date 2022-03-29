
from flask import Flask,request,render_template,redirect,url_for
import sqlite3
app = Flask(__name__)



def shorten(url:str):
    '''shorten the url by saving it to the database'''
    if url[:7] != "http://" and url[:8] != "https://":
        url = "http://" + url
    con = sqlite3.connect('example.db')
    con.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, url TEXT)")
    con.execute("INSERT INTO urls (url) VALUES (?)",(url,))
    con.commit()
    return con.execute("SELECT id FROM urls WHERE url=?",(url,)).fetchone()[0]

def expand(id:int):
    '''expand the url by retrieving it from the database'''
    con = sqlite3.connect('example.db')
    return con.execute("SELECT url FROM urls WHERE id=?",(id,)).fetchone()[0]

@app.route("/",methods=['GET','POST'])
def index():    
    '''index page'''
    if request.method == 'POST':
        long=request.form['long']
        return render_template('index.html',long=long,short=url_for('shortL',short=shorten(long),_external=True))
    else :
        return render_template('index.html')

@app.route("/ln/<string:short>")
def shortL(short):
    '''redirect to the long url'''
    try:
        return redirect(expand(int(short)))
    except ValueError:
        return "Invalid URL"
    