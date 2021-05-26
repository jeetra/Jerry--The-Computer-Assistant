import time
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
s.screensize(1920, 1080)
s.setup(width=1.0, height=1.0, startx=None, starty=None)
#turtle.screensize(canvwidth=6000, canvheight=6000,bg="black")
#t.pencolor('white')
a=0
b=0
t.speed(-1)
t.penup()
t.goto(0,200)
t.pendown()
t.width(5)
#print(turtle.screensize())

while True:
    for colours in ['red','blue','cyan','green','yellow']:
        t.pencolor(colours)
        t.forward(a)
        t.right(b)
        a+=3
        b+=1
    if b ==220:
        break
        turtle.hideturtle()

time.sleep(8)
#turtle.done()
t.hideturtle()
#time.sleep(5)
#t.getscreen().bye()
#tk.mainloop()
#turtle.mainloop()
#t.exitonclick()
#t.screen().bye()
