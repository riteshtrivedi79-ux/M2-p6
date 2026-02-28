import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(400,600)
t=turtle.Turtle()
t.penup()
t.goto(-50,0)
t.pendown()
t.color("red")
for i in range(4):

    t.forward(100)
    t.left(90)
    
turtle.done()