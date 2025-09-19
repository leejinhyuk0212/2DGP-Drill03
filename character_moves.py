from pico2d import *
import math

open_canvas()

g = load_image('grass.png')
ch = load_image('character.png')

x = 400
y = 90

state = 0  # 사각형 방향 상태 0~3, 삼각형 방향 상태 0~2
mode = 0   # 0: 사각형, 1: 원, 2: 삼각형
deg = 0

triangle_points = [(400, 90), (700, 500), (100, 500)]  # 삼각형 꼭짓점 미리 선언

while True:
    clear_canvas_now()
    g.draw_now(400, 30)
    ch.draw_now(x, y)

    if mode == 0:  # 사각형 운동
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

    elif mode == 1:  # 원 운동
        x = 400 + 210 * math.cos(math.radians(deg) - math.pi/2)
        y = 300 + 210 * math.sin(math.radians(deg) - math.pi/2)
        deg -= 1
        if deg < -360:
            deg = 0
            mode = 2
            state = 0


    elif mode == 2:  # 삼각 운동
        tx, ty = triangle_points[(state + 1) % 3]

        dx = tx - x
        dy = ty - y
        dist = math.sqrt(dx * dx + dy * dy)

        if dist < 5:
            state = (state + 1) % 3
            if state == 0:
                mode = 0
        else:
            x += dx / dist * 5
            y += dy / dist * 5

    delay(0.01)
    get_events()
