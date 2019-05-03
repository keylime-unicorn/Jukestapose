#!/usr/bin/python3

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
  #print(player.playing)
  #print(player.source)

  if request.method == 'POST':
    #f = request.files['file']
    #name = secure_filename(f.filename)
    #f.save(os.path.join('./Music/', name))
    #music = pyglet.media.load("./Music/" + name)
    #player.queue(music)

    name = "./Music/bensound-cute.mp3"
    music = pyglet.media.load(name)
    player.queue(music)
    return "AHHHH"

  if request.method == 'GET':
    return render_template('index.html', name='index')
