import math
import time

WIDTH = 40
HEIGHT = 20
chars = " .:-=+*#%@"

A = 0

while True:
    screen = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
    zbuf = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for theta in range(0, 360, 15):
        for phi in range(0, 360, 15):
            t = math.radians(theta)
            p = math.radians(phi)

            x = (math.cos(p) * (2 + math.cos(t)))
            y = (math.sin(p) * (2 + math.cos(t)))
            z = math.sin(t)

            sx = int(WIDTH / 2 + x * 6)
            sy = int(HEIGHT / 2 + y * 3)

            if 0 <= sx < WIDTH and 0 <= sy < HEIGHT:
                if z > zbuf[sy][sx]:
                    zbuf[sy][sx] = z
                    brightness = int((z + 1) * (len(chars)-1) / 2)
                    screen[sy][sx] = chars[brightness]

    print("\x1b[H")
    for row in screen:
        print("".join(row))

    A += 0.1
    time.sleep(0.1)
