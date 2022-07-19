import pygame as pg
from glob import glob
from random import sample

pg.mixer.init(11025)  

def play(filename, wait=False):
    """ """
    channel = pg.mixer.Sound(filename)
    channel.play()
    while wait:
        if not channel.get_busy():
            pg.time.wait()

typing_sound_list = glob('audio/key*.wav')

def keyboard(wait=False):
    """ """
    filename = sample(typing_sound_list, 1)[0]
    play(filename, wait)

def warn(wait=False):
    """ """
    play('audio/warn.wav', wait)

def passit(wait=False):
    """ """
    play('audio/pass.wav')

def success(wait=False):
    """ """
    play('audio/success.wav')

def fail(wait=False):
    """ """
    play('audio/fail.wav')