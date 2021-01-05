import simple_draw as sd


sd.resolution = (1200, 650)


def bubble(point, step):
    radius = 30
    for _ in range(5):
        radius += step
        sd.circle(point, radius)


for x in range(100, 501, 100):
    for y in range(100, 1101, 100):
        point = sd.get_point(y, x)
        bubble(point, 5)

sd.pause()

