from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x= 0
y= 90

#move ractangle


while(1):
    
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

        while x < 600: #원의 시작점과 끝점이 (600,300)인 관계로 사각형의 x 좌표를 600까지 연장해줌 
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,90)
            x += 2
            delay(0.01)

        for i in range(720):
            clear_canvas_now()
            grass.draw_now(400,30)
    
            i * math.pi / 720
            x = 200*math.cos(i/720*2*math.pi) + 400
            y = 200*math.sin(i/720*2*math.pi) + 300
            character.draw_now(x,y)
            

# move circle   
close_canvas()
