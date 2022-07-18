import pygame as pg
 
def main():
     
    pg.init()
    pg.display.set_caption("打字练习")
     
    # Screen display mode
    # screen = pg.display.set_mode((800,600))
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
     
    running = True
    while running:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                print(event.dict['unicode'])
     
     
if __name__=="__main__":
    main()