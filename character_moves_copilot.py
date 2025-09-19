from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 운동 관련 상수 및 변수
rect_points = [(20, 90), (780, 90), (780, 550), (20, 550)]
triangle_points = [(400, 90), (700, 500), (100, 500)]

speed = 5
speed_deg = 1

# 초기 상태
x, y = 400, 90
state = 0    # 사각형/삼각형 상태(방향 또는 꼭짓점 인덱스)
mode = 0     # 0=사각형, 1=원, 2=삼각형
deg = 0      # 원 궤도 각도

def rectangle_move(x, y, speed, state):
    if state == 0:  # 오른쪽
        x = min(x + speed, rect_points[1][0])
        if x >= rect_points[1][0]:
            state = 1
    elif state == 1:  # 위
        y = min(y + speed, rect_points[2][1])
        if y >= rect_points[2][1]:
            state = 2
    elif state == 2:  # 왼쪽
        x = max(x - speed, rect_points[3][0])
        if x <= rect_points[3][0]:
            state = 3
    else:  # 아래
        y = max(y - speed, rect_points[0][1])
        if y <= rect_points[0][1]:
            state = 0
    return x, y, state

def circle_move(center_x, center_y, radius, deg, speed_deg):
    deg = (deg - speed_deg) % 360
    rad = math.radians(deg) - math.pi / 2
    x = center_x + radius * math.cos(rad)
    y = center_y + radius * math.sin(rad)
    return x, y, deg

def triangle_move(x, y, speed, state):
    start = triangle_points[state]
    end = triangle_points[(state + 1) % 3]

    dx = end[0] - x
    dy = end[1] - y
    dist = math.hypot(dx, dy)

    if dist <= speed:
        x, y = end
        state = (state + 1) % 3
    else:
        x += dx / dist * speed
        y += dy / dist * speed
    return x, y, state

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(int(x), int(y))

    if mode == 0:  # 사각형 운동
        x, y, state = rectangle_move(x, y, speed, state)
        # 사각형 궤도 1바퀴 돌면 원 운동으로 전환
        if state == 0 and x == (rect_points[0][0] + rect_points[1][0]) / 2 and y == rect_points[0][1]:
            mode = 1
            deg = 0

    elif mode == 1:  # 원 운동
        x, y, deg = circle_move(400, 300, 210, deg, speed_deg)
        # 한 바퀴 돌았으면 삼각형 운동으로 전환
        if deg == 0:
            mode = 2
            state = 0

    else:  # 삼각형 운동
        x, y, state = triangle_move(x, y, speed, state)
        # 삼각형 한 바퀴 돌면 사각형 운동으로 전환
        if state == 0 and (x, y) == triangle_points[0]:
            mode = 0
            state = 0

    delay(0.01)
    get_events()
