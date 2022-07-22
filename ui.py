import pygame_menu as pgm


def show_message(screen, title, content, font_size=80):
    """ """
    MESSAGE_BOX_THEME = pgm.themes.Theme(
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
        widget_font_size=font_size,
    )
    W, H = screen.get_size() 
    menu = pgm.Menu(
        title, int(W * .98), int(H * .5), theme=MESSAGE_BOX_THEME, 
        onclose=pgm.events.CLOSE,
    )
    menu.add.label(content)
    menu.add.label('')
    menu.add.button('确定', pgm.events.CLOSE)
    menu.mainloop(screen)

