from moviepy.editor import VideoFileClip
from glob import glob
from random import sample


def get_filename():
    """ """
    return sample(glob('video/**/*.mp4'), k=1)[0]

def play(filename, screen):
    """ """
    W, H = screen.get_size()
    video = VideoFileClip(filename, target_resolution=(H, W))
    video.preview(fullscreen=True)

def play_random(screen):
    """ """
    filename = get_filename()
    play(filename, screen)