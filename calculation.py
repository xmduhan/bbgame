import pygame as pg
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

THEME1 = pgm.themes.Theme(
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
    widget_font_size=80,
)

def get_font_size(screen, text):
    """ """
    W, _ = screen.get_size()
    # print(f'{W=}')
    font_size = W 

    while True:
        font_size = int(font_size)
        font = pg.font.Font(None, font_size)
        size = font.size(text)

        if size[0] > W * .61:
            font_size *= .9
            continue

        if size[0] < W * .59:
            font_size *= 1.1
            continue
        
        break
    return font_size

def get_formula(max_value):
    while True:
        symbol = sample(['+', '-'], 1)[0]
        t = randint(0, max_value)
        a = randint(0, t)
        b = t - a
        if a * b in (a, b):
            if randint(0, 10) > 1:
                continue
        if a == b and symbol == '-':
            if randint(0, 10) > 1:
                continue
        if symbol == '+':
            return f'{a} {symbol} {b}', t
        else:
            return f'{t} {symbol} {a}', b

def play(screen, formula, result, title, error=0):
    """ """
    W, H = screen.get_size()

    fg = 250, 240, 230
    bg = 5, 5, 5

    text = f'{formula} = {result}  '
    font_size = get_font_size(screen, text)
    font = pg.font.Font(None, font_size)
    size = font.size(text)
    w, h = size

    title_font = pg.font.Font('font/kaiti.ttf', 50)

    result_string = ''
    cursor = 0
    while True:
        screen.fill(bg)
        horizontal = (W - w) // 2 
        vertical = (H - h) // 2 
        surface = font.render(f'{formula} = ', 0, fg, bg)
        screen.blit(surface, (horizontal, vertical))
        horizontal += font.size(f'{formula} = ')[0]
        surface = font.render(f'{result_string}', 0, fg, bg)
        screen.blit(surface, (horizontal, vertical))

        hint = f'{title}  错误: {error}' 
        surface = title_font.render(hint, 0, fg, bg)
        screen.blit(surface, (0, 0))

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False, error

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return False, error

                if event.key == pg.K_BACKSPACE:
                    if len(result_string) > 0:
                        result_string = result_string[:-1]
                        audio.keyboard()
                        continue
                    audio.warn()

                if event.key == pg.K_RETURN:
                    if len(result_string) == 0:
                        audio.warn()
                        continue
                    if eval(formula) == int(result_string):
                        audio.passit()
                    else:
                        audio.warn()
                        error += 1
                    return True, error
                
                ch = event.dict['unicode']
                if ch in string.digits:
                    if len(result_string) < 3:
                        result_string += ch
                        audio.keyboard()
                        continue
                audio.warn()
                    
        pg.display.flip()


menu2lambda = {
    '10以内加减法': lambda : get_formula(10),
    '15以内加减法': lambda : get_formula(15),
    '20以内加减法': lambda : get_formula(20),
    '30以内加减法': lambda : get_formula(30),
    '50以内加减法': lambda : get_formula(50),
    '100以内加减法': lambda : get_formula(100),
}

def play_menu(screen, menu_text, times=10):
    """ """
    error = 0
    get_formula = menu2lambda.get(menu_text)
    playing = True
    formula_list = []
    for i in range(1, times+1):
        while True:
            formula, result = get_formula()
            if formula not in formula_list:
                break
            if randint(0, 10) > 1:
                break
        title = f'关卡: {menu_text}({i}/{times})'
        playing, error = play(screen, formula, result, title, error)
        formula_list.append(formula)
        if not playing:
            return

    pct = (1 - error / times) * 100
    success = pct >= 90
    if success:
        audio.success()
        message = f'恭喜您闯关成功! 您的正确率为: {pct:.0f}%, 很棒哦! :-)'
    else:
        # audio.fail()
        message = f'您出错多了点, 不过不要气馁请继续努力! 当前正确率: {pct:.0f}%'
    
    W, H = screen.get_size()
    menu = pgm.Menu(
        f'关卡: {menu_text}', int(W * .98), int(H * .5), theme=THEME1, 
        onclose=pgm.events.CLOSE,
    )
    menu.add.label(message)
    menu.add.label('')
    menu.add.button('确定', pgm.events.CLOSE)
    menu.mainloop(screen)
    if success:
        video.play_random(screen)
            

def main(screen=None):
    """ """
    if screen is None:
        pg.init()
        pg.mixer.init(11025)  
        pg.display.set_caption("口算练习")
        screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        
    W, H = screen.get_size()

    menu = pgm.Menu(
        '口算练习', int(W * 1), int(H * 1), theme=THEME, 
        columns=2, rows=7, onclose=pgm.events.CLOSE,
    )
    menu.add.button('10以内加减法', lambda : play_menu(screen, '10以内加减法'))
    menu.add.button('15以内加减法', lambda : play_menu(screen, '15以内加减法'))
    menu.add.button('20以内加减法', lambda : play_menu(screen, '20以内加减法'))
    menu.add.button('30以内加减法', lambda : play_menu(screen, '30以内加减法'))
    menu.add.button('50以内加减法', lambda : play_menu(screen, '50以内加减法'))
    menu.add.button('100以内加减法', lambda : play_menu(screen, '100以内加减法'))
    # menu.add.button('小游戏', lambda : play_with(screen))
    menu.add.label('')

    menu.add.label('')
    menu.add.label('')
    menu.add.label('')
    menu.add.label('')
    menu.add.label('')
    menu.add.label('')
    menu.add.button('退出', pgm.events.CLOSE)
    menu.mainloop(screen)


if __name__=="__main__":
    main()