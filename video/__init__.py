from moviepy.editor import VideoFileClip
from glob import glob


def get_filename():
    """ """
    return glob('video/**/*.mp4')[0]

def play(filename, screen):
    """ """
    W, H = screen.get_size()
    video = VideoFileClip(filename, target_resolution=(H, W))
    video.preview(fullscreen=True)
    # video.preview(fullscreen=False)

def play_random(screen):
    """ """
    filename = get_filename()
    play(filename, screen)