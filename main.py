import pygame as pg
import pygame_menu as pgm
import typing_game


 
def main():
     
    pg.init()
    pg.mixer.init(11025)  # raises exception on fail
    pg.display.set_caption("打字练习")
     
    # Screen display mode
    # screen = pg.display.set_mode((800,600))
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    # typing_game.play(screen)
    menu = pgm.Menu('Welcome', 400, 300, theme=pgm.themes.THEME_BLUE)
    menu.add.button('Typing', lambda : typing_game.main(screen))
    menu.add.button('Quit', pgm.events.EXIT)
    menu.mainloop(screen)


if __name__=="__main__":
    main()