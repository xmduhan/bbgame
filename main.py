# import the pygame module, so you can use it
import pygame as pg
 
# define a main function
def main():
     
    # initialize the pygame module
    pg.init()
    # load and set the logo
    pg.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pg.display.set_mode((800,600))
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pg.event.get():
            # only do something if the event is of type QUIT
            if event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                print(event.dict['unicode'])
                # print(pg.key.name(event.key), event.) 
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()