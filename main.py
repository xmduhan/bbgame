from locale import currency
import pygame as pg



def play(screen, text):
    """ """
    W, H = screen.get_size()
    print(f"{W=}, {H=}")

    fg0 = 250, 240, 230
    fg1 = 255, 0, 0  
    bg = 5, 5, 5

    font = pg.font.Font(None, 500)
    size = font.size(text)
    w, h = size
    print(f'{h=}, {w=}')

    cursor = 0
    running = True

    while running and cursor < len(text):
        screen.fill(bg)
        horizontal = (W - w) // 2 
        vertical = (H - h) // 2 
        # print(f'{horizontal=}, {vertical=}')
        for i, ch in enumerate(text):
            size = font.size(ch)
            fg = fg1 if cursor > i else fg0
            surface = font.render(ch, 0, fg, bg)
            screen.blit(surface, (horizontal, vertical))
            horizontal += size[0]

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                
                if event.dict['unicode'] == text[cursor]:
                    cursor += 1
        pg.display.flip()



 
def main():
     
    pg.init()
    pg.display.set_caption("打字练习")
     
    # Screen display mode
    # screen = pg.display.set_mode((800,600))
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

    play(screen, 'asdfgjkl')

if __name__=="__main__":
    main()

     