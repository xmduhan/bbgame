import pygame as pg
from glob import glob
from random import sample, choices

def get_font_size(screen, text):
    """ """
    W, _ = screen.get_size()
    # print(f'{W=}')
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

def play_with(screen, text, success):
    """ """
    W, H = screen.get_size()
    typing_sound_list = glob('audio/key*.wav')

    fg0 = 250, 240, 230
    fg1 = 255, 0, 0  
    bg = 5, 5, 5

    font_size = get_font_size(screen, text)
    font = pg.font.Font(None, font_size)
    size = font.size(text)
    w, h = size

    success_font = pg.font.Font(None, 80)

    cursor = 0
    while cursor <= len(text):
        screen.fill(bg)
        horizontal = (W - w) // 2 
        vertical = (H - h) // 2 
        for i, ch in enumerate(text):
            size = font.size(ch)
            fg = fg1 if cursor > i else fg0
            surface = font.render(ch, 0, fg, bg)
            screen.blit(surface, (horizontal, vertical))
            horizontal += size[0]

        success_text = f'Success: {success}'
        surface = success_font.render(success_text, 0, fg0, bg)
        screen.blit(surface, (0, 0))
        
        if cursor == len(text):
            pg.display.flip()
            break

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return False
                
                if event.dict['unicode'] == text[cursor]:
                    cursor += 1
                    audio_filename = sample(typing_sound_list, 1)[0]
                    pg.mixer.Sound(audio_filename).play()
                    break
                
                if event.dict['unicode'] != '':
                    audio_filename = 'audio/warning.wav'
                    pg.mixer.Sound(audio_filename).play()
                    break
                    
        pg.display.flip()

    audio_filename = 'audio/success2.wav'
    channel = pg.mixer.Sound(audio_filename).play()
    while channel.get_busy(): 
        pg.time.wait(100)

    return True

keys = 'asdfghjkl'

def play(screen):
    """ """
    success = 0
    playing = True
    while playing:
        text = ''.join(choices(keys, k=10))
        playing = play_with(screen, text, success=success)
        success += 1