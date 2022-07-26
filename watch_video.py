import pygame as pg
import pygame_menu as pgm
from glob import glob
import video
import ui
import os
from more_itertools import chunked
import database as db


def play(screen, filename):
    """ """
    count = round(video.get_duration(filename) / 60)
    result = ui.comfirm(screen, '请确认', f'看这个视频会耗费{count}个金币, 确定要继续吗?')
    if result:
        cnt = db.get_gold_count() 
        if cnt < count:
            ui.show_message(screen, '出错啦', '您的金币不够啊! 去做些练习赚金币吧! :-)')
            return
        video.play(screen, filename)


def browse(screen, path):
    """ """
    # Read filelist
    filename_list = glob(path + '/*')
    _filename_list = []
    for filename in filename_list:
        fn = filename.split('/')[-1]
        if os.path.isdir(filename) and not fn.startswith('__'):
            _filename_list.append(filename)
        else: 
            if fn.endswith('.mp4'):
                _filename_list.append(filename)
    filename_list = sorted(_filename_list)

    # Change order 
    count = len(filename_list)
    columns = 5
    rows = count // columns if count % columns == 0 else round(count / columns + .5)

    # print(f'{columns=}, {rows=}')
    # _filename_list = []
    # for i in range(columns):
    #     for j in range(rows):
    #         print(j, end=':')
    #         idx = j * columns + i
    #         print(idx, end=' ')
    #         if idx < count:
    #             _filename_list.append(filename_list[idx])
    #     print()
    # print(filename_list)
    # print(_filename_list)
    # filename_list = _filename_list

    W, H = screen.get_size()
    menu = pgm.Menu(
        path, int(W * 1), int(H * 1), 
        theme=ui.DEFAULT_THEME, onclose=pgm.events.CLOSE,
        columns=columns, rows=rows,
    )
    for filename in filename_list:
        fn = filename.split('/')[-1]
        if os.path.isdir(filename):
            menu.add.button(fn, lambda x=filename: browse(screen, x))
        else:
            menu.add.button(fn[:-4], lambda x=filename: play(screen, x))
    menu.mainloop(screen)


def main(screen=None):
    """ """
    if screen is None:
        pg.init()
        pg.mixer.init(11025)  
        pg.display.set_caption("打字练习")
        screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    browse(screen, 'video')


if __name__=="__main__":
    main()