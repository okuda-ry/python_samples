# Pythonで3D立方体をASCIIアートで描画するコード
import os
import math
import time

width, height = 80, 24
zbuffer = [0] * (width * height)
buffer = [" "] * (width * height)
K1 = 40
incrementSpeed = 1
cubeWidth = 10


# 投影計算関数
def calculateX(x, y, z):
    return x * math.cos(angle) - z * math.sin(angle)


def calculateY(x, y, z):
    return y


def calculateZ(x, y, z):
    return x * math.sin(angle) + z * math.cos(angle)


def calculateSurface(x, y, z, ch):
    X = calculateX(x, y, z)
    Y = calculateY(x, y, z)
    Z = calculateZ(x, y, z)
    ooz = 1 / Z
    xp = int(width / 2 + K1 * ooz * X * 2)
    yp = int(height / 2 + K1 * ooz * Y)
    idx = xp + yp * width
    if 0 <= idx < width * height and ooz > zbuffer[idx]:
        zbuffer[idx] = ooz
        buffer[idx] = ch


angle = 0
while True:
    buffer = [" "] * (width * height)
    zbuffer = [0] * (width * height)
    for cubeX in range(-cubeWidth, cubeWidth, int(incrementSpeed)):
        for cubeY in range(-cubeWidth, cubeWidth, int(incrementSpeed)):
            calculateSurface(cubeX, cubeY, cubeWidth, "#")
    os.system("clear")
    for k in range(width * height):
        print(buffer[k], end="") if k % width != 0 else print()
    angle += 0.1
    time.sleep(0.05)
