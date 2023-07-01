from re import S
import pandas as pd
import pygame as pg
import ui
import pygame_menu as pgm
from glob import glob
from random import sample, randint
import string
import audio
import video

THEME = pgm.themes.Theme(
    background_color=(40, 41, 35),
    cursor_color=(255, 255, 255),
    cursor_selection_color=(80, 80, 80, 120),
    scrollbar_color=(39, 41, 42),
    scrollbar_slider_color=(65, 66, 67),
    scrollbar_slider_hover_color=(90, 89, 88),
    selection_color=(255, 255, 255),
    title_background_color=(47, 48, 51),
    title_font_color=(215, 215, 215),
    widget_font_color=(200, 200, 200),
    title_font='font/kaiti.ttf',
    widget_font='font/kaiti.ttf',
    widget_font_size=100,
)

def get_font_size(screen, text):
    """ """
    W, _ = screen.get_size()
    # print(f'{W=}')
    font_size = W

    while True:
        font_size = int(font_size)
        font = pg.font.Font('font/kaiti.ttf', font_size)
        size = font.size(text)

        if size[0] > W * .61:
            font_size *= .9
            continue

        if size[0] < W * .59:
            font_size *= 1.1
            continue

        break
    return font_size


def play(screen, title, text):
    """ """
    W, H = screen.get_size()

    fg = 250, 240, 230
    bg = 5, 5, 5
    font_size = get_font_size(screen, text)
    # font = pg.font.Font(None, font_size)
    font = pg.font.Font('font/kaiti.ttf', font_size)
    size = font.size(text)
    w, h = size

    title_font = pg.font.Font('font/kaiti.ttf', 50)

    result_string = ''
    cursor = 0
    while True:
        screen.fill(bg)
        horizontal = (W - w) // 2
        vertical = (H - h) // 2
        surface = font.render(f'{text}', 0, fg, bg)
        screen.blit(surface, (horizontal, vertical))

        hint = f'{title}'
        surface = title_font.render(hint, 0, fg, bg)
        screen.blit(surface, (0, 0))

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return 0

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 0

                if event.key in (pg.K_j, pg.K_DOWN):
                    return 1

                if event.key in (pg.K_k, pg.K_UP):
                    return -1

        pg.display.flip()

books = [ '一年级上册', '一年级下册', '二年级上册', '二年级下册']

def play_menu(screen, book):
    """ """
    error = 0
    playing = True

    df = pd.read_excel('data/chinese.xlsx')
    texts = list(df[book].dropna())
    if not texts: return

    i = 0
    while True:
        title = f'{book}: ({i+1}/{len(texts)})'
        res = play(screen, title, texts[i])
        if res == 0: return
        if 0 <= i + res < len(texts):
            i += res

def main(screen=None):
    """ """
    if screen is None:
        pg.init()
        pg.mixer.init(11025)
        pg.display.set_caption("汉字学习")
        screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    W, H = screen.get_size()

    menu = pgm.Menu(
        '汉字学习', int(W * 1), int(H * 1), theme=THEME,
        columns=1, rows=5, onclose=pgm.events.CLOSE,
    )
    menu.add.button(books[0], lambda : play_menu(screen, books[0]))
    menu.add.button(books[1], lambda : play_menu(screen, books[1]))
    menu.add.button(books[2], lambda : play_menu(screen, books[2]))
    menu.add.button(books[3], lambda : play_menu(screen, books[3]))
    menu.add.button('退出', pgm.events.CLOSE)
    menu.mainloop(screen)


if __name__=="__main__":
    main()
