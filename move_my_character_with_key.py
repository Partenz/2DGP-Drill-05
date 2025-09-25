from pico2d import *

width, height = 1280, 1024

open_canvas(width,height)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('character.png')


def handle_event():
    global running
    global dirX, dirY
    events = get_events()

    for event in events:
        if (event.type == SDL_QUIT)
            running = False
        elif(event.type == SDL_KEYDOWN):
            if(event.key == SDLK_ESCAPE):
                running = False
            elif(event.key == SDLK_LEFT):
                pass
            elif(event.key == SDLK_RIGHT):
                pass
            elif(event.key == SDLK_UP):
                pass
            elif(event.key == SDLK_DOWN):
                pass

running = True

dirX = 0
dirY = 0

x = width // 2
y = height // 2

frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(width // 2, height // 2)

    update_canvas()
    handle_event()

close_canvas()