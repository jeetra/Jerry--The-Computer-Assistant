from speak1 import speak
import turtle
import os
import pyttsx3
engine = pyttsx3.init('sapi5')  # microsoft Speech api
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 210)
engine.setProperty('volume', 1.0)

# turtle object
pen = turtle.Turtle()
s=turtle.Screen()
#s.bgcolor('black')
s.screensize(1920, 1080)
s.setup(width=1.0, height=1.0, startx=None, starty=None)


# function for creation of eye
def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()


# draw face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

# draw eyes
pen.goto(-40, 120)
eye('white', 15)
pen.goto(-37, 125)
eye('black', 5)
pen.goto(40, 120)
eye('white', 15)
pen.goto(40, 125)
eye('black', 5)

# draw nose
pen.goto(0, 75)
eye('black', 8)

# draw mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()

# draw tongue
pen.goto(-10, 45)
pen.down()
pen.right(180)
pen.fillcolor('red')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()
turtle.setpos(0,-40)
arg="Sorry , you can't go further.!:)"
turtle.write(arg,move=True,align = 'left',font=("Arial", 16, "normal"))
speak("Sorry , you can't go further.!:)")
speak("Will see you again, if Jeet sir permits....")
speak("Till then , Bye bye!!!")
#turtle.write("Will see you again, if Jeet sir permits....")
os.system('python wait_2_sec.py')
pen.hideturtle()