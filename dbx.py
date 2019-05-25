import turtle
##python中的图形库

num = int(input("Please input the num of the polygon: "))
####color = input("Please input the color of the fillcolor:")
###turtle.fillcolor(color)
angle = 180 - (num -2) * 180 / num
turtle.begin_fill()
for i in range(num):
    turtle.forward(100)
    turtle.right(angle)
turtle.end_fill()
turtle.done()
