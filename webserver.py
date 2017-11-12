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

  player.play()

  if request.method == 'POST':
    f = request.files['file']
    name = secure_filename(f.filename)
    mp3 = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/Music/', name)
    wav = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/Music/', name + '.wav')
    f.save(os.path.join('./Music/', name))
    song = AudioSegment.from_mp3(mp3)
    song.export(wav, format="wav")
    music = pyglet.media.load(wav)
    player.queue(music)
    os.remove(mp3)
    return "AHHHH"

  if request.method == 'GET':
    return render_template('index.html', name='index')
