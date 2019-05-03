#!/usr/bin/python3

from pyglet import media

player = media.Player()

def main():
    player.play()

    name = "./Music/bensound-littleidea.mp3"
    music = media.load(name)
    player.queue(music)

if __name__ == "__main__":
    main()
