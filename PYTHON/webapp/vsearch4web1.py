from flask import Flask, render_template, request, escape
from PYTHON.modul.vsearch import search4letters


app = Flask(__name__)


@app.route('/')
def hello():
    return "czesc"



if __name__ == '__main__':
    app.run(debug=True)
