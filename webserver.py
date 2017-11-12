#!/usr/bin/python

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    f = request.files['the_file']
    f.save('/Music/' + secure_filename(f.filename))
  if request.method == 'GET':
    return render_template('index.html', name='index')
