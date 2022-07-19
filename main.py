import pygame as pg
import pygame_menu as pgm
import typing_game


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
    widget_font_size=40,
)
 
def main():
     
    pg.init()
    pg.mixer.init(11025)  # raises exception on fail
    pg.display.set_caption("打字练习")
     
    # Screen display mode
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    W, H = screen.get_size()

    menu = pgm.Menu('宝宝小游戏', int(W * .6), int(H * .6), theme=THEME)
    menu.add.button('打字练习', lambda : typing_game.main(screen))
    menu.add.button('退出', pgm.events.EXIT)
    menu.mainloop(screen)

if __name__=="__main__":
    main()