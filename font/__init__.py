import pygame as pg

def get_font_filename():
    """ """
    return 'font/kaiti.ttf'

def get_font(size):
    """ """
    return pg.font.Font(get_font_filename(), size)

def get_suitable_size(text, width):
    """ """
