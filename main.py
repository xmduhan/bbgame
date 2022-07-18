import pygame as pg

def get_font_size(screen, text):
    """ """
    W, _ = screen.get_size()
    print(f'{W=}')
    font_size = W 

    while True:
        font_size = int(font_size)
        font = pg.font.Font(None, font_size)
        size = font.size(text)

        if size[0] > W * .91:
            font_size *= .9
            continue

        if size[0] < W * .89:
            font_size *= 1.1
            continue
        
        break
    return font_size


def play(screen, text):
    """ """
    W, H = screen.get_size()
    # print(f"{W=}, {H=}")

    fg0 = 250, 240, 230
    fg1 = 255, 0, 0  
    bg = 5, 5, 5

    font_size = get_font_size(screen, text)
    font = pg.font.Font(None, font_size)
    size = font.size(text)
    w, h = size
    # print(f'{h=}, {w=}')

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
    play(screen, 'abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

if __name__=="__main__":
    main()

     