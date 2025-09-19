from pico2d import *
import math

open_canvas()

g = load_image('grass.png')
ch = load_image('character.png')

x = 400
y = 90

state = 0  # 사각형 방향 상태 0~3
mode = 0   # 0: 사각형, 1: 원
deg = 0

while True:
    clear_canvas_now()
    g.draw_now(400, 30)
    ch.draw_now(x, y)

    if mode == 0:
        if state == 0:
            x += 5
            if x > 780:
                x = 780
                state = 1
            # 원운동 시작 조건 (위치 맞춤 없음)
            if x == 400 and y == 90:
                mode = 1
                deg = 0

        elif state == 1:
            y += 5
            if y > 550:
                y = 550
                state = 2

        elif state == 2:
            x -= 5
            if x < 20:
                x = 20
                state = 3

        elif state == 3:
            y -= 5
            if y < 90:
                y = 90
                state = 0
                # 위치 맞춤 삭제 (아무것도 안 함)

    elif mode == 1:
        x = 400 + 210 * math.cos(math.radians(deg) - math.pi/2)
        y = 300 + 210 * math.sin(math.radians(deg) - math.pi/2)
        deg += 1
        if deg > 360:
            deg = 0
            mode = 0
            # 초기 위치도 그대로 둠
            state = 0

    delay(0.01)
    get_events()
