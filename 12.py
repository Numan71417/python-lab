import turtle

def sierpinski(t, x, y, size, depth):
    if depth == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, x, y, size/2, depth-1)
        sierpinski(t, x+size/2, y, size/2, depth-1)
        sierpinski(t, x+size/4, y+(size/2)*(3*0.5)/2, size/2, depth-1)

        if depth == change_depth:
            t.fillcolor('magenta')
            t.begin_fill()
            sierpinski(t, x+size/4, y+((size/2)*(3*0.5)/2), size/2, 0)
            t.end_fill()

            t.fillcolor('red')
            t.begin_fill()
            sierpinski(t, x, y, size/2, 0)
            t.end_fill()

            t.fillcolor('blue')
            t.begin_fill()
            sierpinski(t, x+size/2, y, size/2, 0)
            t.end_fill()

t = turtle.Turtle()
t.speed(0)

change_depth = 4
sierpinski(t,-200,-200,400,change_depth)

turtle.done()