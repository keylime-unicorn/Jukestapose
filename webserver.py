#!/usr/bin/python

from flask import Flask
from flask import request
from flask import render_template
import pyglet

app = Flask(__name__)

queue = []

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    f = request.files['the_file']
    f.save('/Music/' + secure_filename(f.filename))
    add_to_queue(secure_filename(f.filename))
  if request.method == 'GET':
    return render_template('index.html', name='index')
@app.route('/')
def main():
  while queue:
    song = queue.pop(0)
    play_song(song)
def add_to_queue(name):
  queue.append(name)
  print queue
def play_song(name):
  music = pyglet.resource.media(name)
  music.play()
  pyglet.app.run() 
