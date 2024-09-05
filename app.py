from flask import Flask, render_template_string, render_template
from werkzeug.serving import run_simple
import sqlite3

app = Flask(__name__,template_folder='.')

def get_db_connection():
    conn = sqlite3.connect(r'/Users/paritapatel/Documents/DAB111\ \(PYTHON\)/Project/final\ project\ /Database/covid_19.db ')
    conn.row_factory = sqlite3.Row
    return conn
    
@app.route('/')
def index():
    conn = sqlite3.connect(r'/Users/paritapatel/Documents/DAB111\ \(PYTHON\)/Project/final\ project\ /Database/covid_19.db ')
    data = conn.execute("SELECT * FROM covid_19").fetchall()
    conn.close()
    data_html = data.to_html(index=False) 

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>COVID 19 Data</h1>
            <h2>This data about COVID 19 Cases, Recoveries, and Deaths by Country</h2>
            
        {{data|safe}}
        </body>
        </html>
    ''', data = data)

@app.route('/about')
def about():
    return render_template('about.html')

run_simple('localhost',4000, app, use_reloader=False, use_debugger=False)