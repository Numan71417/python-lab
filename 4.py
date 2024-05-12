import turtle

sides = int(input("Enter no of sides: "))
side_len = int(input("Enter length of sides: "))
anngle = 360/sides

pen_colr = input("Enter the pen color: ")
fill_colr = input("Enter the fill color: ")

t = turtle.Turtle()

t.color(pen_colr)
t.fillcolor(fill_colr)

t.begin_fill()

for i in range(sides):
    t.forward(side_len)
    t.right(anngle)

t.end_fill()
turtle.done()


