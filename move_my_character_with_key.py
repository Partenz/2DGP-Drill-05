from pico2d import *

width, height = 1280, 1024

open_canvas(width,height)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('character.png')


running = True

frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(width // 2, height // 2)


    update_canvas()

close_canvas()