import pygame as pg
import typing_game


 
def main():
     
    pg.init()
    pg.mixer.init(11025)  # raises exception on fail
    pg.display.set_caption("打字练习")
     
    # Screen display mode
    # screen = pg.display.set_mode((800,600))
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    typing_game.play(screen)


if __name__=="__main__":
    main()