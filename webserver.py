#!/usr/bin/python

from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
from pydub import AudioSegment
import pyglet
import os

app = Flask(__name__)

player = pyglet.media.Player()

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    f = request.files['file']
    name = secure_filename(f.filename)
    f.save(os.path.join('./Music/', name))
    song = AudioSegment.from_mp3(os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/Music/', name))
    song.export(os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/Music/', name + '.wav'), format="wav")
    music = pyglet.media.load(os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/Music/', name + '.wav'))
    add_to_queue(music)
    player.play()
    return "AHHHH"
  if request.method == 'GET':
    return render_template('index.html', name='index')
def main():
  while player.queue:
    player.play()
def add_to_queue(name):
  player.queue(name)
