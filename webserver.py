#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'home page'

@app.route('/upload')
def upload():
  return 'upload page'
def get_file():
  return 'getting file...'

