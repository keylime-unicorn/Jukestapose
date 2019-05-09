#!/usr/bin/python3

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from pydub import AudioSegment
import pyglet
import os

app = Flask(__name__)

player = pyglet.media.Player()

@app.route('/', methods=['GET', 'POST'])
def home():

  player.play() 
  print(player.playing)

  if request.method == 'POST':
    f = request.files['file']

    name = secure_filename(f.filename)
    name = os.path.basename(name)
    mp3_name = "./Music/" + name + ".mp3"
    wav_name = "./Music/" + name + ".wav"

    f.save(mp3_name)

    print("creating audiosegment :P")

    wav = AudioSegment.from_mp3(mp3_name)
    wav.export(wav_name, format="wav")

    print("wave exported :)")

    os.remove(mp3_name)

    music = pyglet.media.load(wav_name)
    
    print("media loaded")

    player.queue(music)

    print("song queued")

    return ""

  if request.method == 'GET':
    return render_template('index.html', name='index')
