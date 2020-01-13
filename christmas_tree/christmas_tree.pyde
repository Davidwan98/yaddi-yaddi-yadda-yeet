import random

def draw_sparkle():
    fill(255)
    rect(-10, -10, 20, 20)

def setup():
    size(300, 400)

def tree():
    fill(0, 64, 0)
    triangle(width / 2, 30, 20, height - 30, width - 20, height - 30)

def draw():
    col1 = -1676032
    col2 = -3355444
    tree()
    for i in range(100):
        pushMatrix()
        # something special here to translate
        # at random
        x = map(random.random(), 0, 1, 50, 250)
        y = map(random.random(), 0, 1, 50, 350)
        if get(int(x), int(y)) == col2:
            continue
        translate(x, y)
        rotate(PI / 4)
        sz = map(random.random(), 0, 1, 0.5, 1)
        scale(sz, sz)
        draw_sparkle()
        popMatrix()
        
    noLoop()    
