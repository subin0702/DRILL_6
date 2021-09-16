from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
#move ractangle

while x < 750: #캐릭터가 반으로 잘려서 범위 줄였습니다.
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x += 2
    delay(0.01)

while y < 500: #잘 보이지 않아 500으로 범위 줄였습니다.
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(750,y)
    y += 2
    delay(0.01)

while x > 0:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,500)
    x -= 2
    delay(0.01)

while y > 90:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(0,y)
    y -= 2
    delay(0.01)
    
close_canvas()
