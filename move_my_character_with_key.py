from pico2d import *

width, height = 1280, 1024

open_canvas(width,height)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_event():
    global running
    global dirX, dirY
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1

running = True

dirX = 0
dirY = 0

x = width // 2
y = height // 2

frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(width // 2, height // 2)

    if dirX == 0 and dirY == 0: # IDLE 상태
        character.clip_draw(frame * 100, 300, 100,100,x,y)
    else:
        if dirX != 0 and dirY != 0:
            if dirX == 1:
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
                x += 10
            elif dirX == -1:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
                x -= 10
            if dirY == 1:
                y += 10
            elif dirY == -1:
                y -= 10
        elif dirX != 0 and dirY == 0:
            if dirX == 1:
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
                x += 10
            elif dirX == -1:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
                x -= 10
        elif dirX == 0 and dirY != 0:
            if dirY == 1:
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
                y += 10
            elif dirY == -1:
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
                y -= 10


    update_canvas()
    handle_event()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()