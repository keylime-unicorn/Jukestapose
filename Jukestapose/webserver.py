#!/usr/bin/python3

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
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
    f.save(os.path.join('./Music/', name))
    music = pyglet.media.load("./Music/" + name)
    player.queue(music)
    return ""

  if request.method == 'GET':
    return render_template('index.html', name='index')
