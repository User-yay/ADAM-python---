from turtle import *
import turtle
class smile:
    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize = "exrta extra extra large"

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.goHome()
        pensize(5)
        speed(0)
        self.drawOutLine()
        self.drawEye(135)
        self.drawEye(45)
        self.drawNose()
        self.drawMouth()
        pensize(5)

    def goHome(self):
            penup()
            goto(self.coord)

            setheading(0)

    def drawOutLine(self):
            forward(self.size)
            left(90)
            pendown()
            circle(self.size)
            self.goHome()
    def drawEye(self, turn):
            penup()
            left(turn)
            forward(self.size/2)
            pendown()
            dot(self.size/10)
            self.goHome()

    def drawMouth(self):
          penup()
          right(135)
          forward(self.size/1.7)
          left(90)
          pendown()
          circle(self.size/1.7, 90)
          self.goHome()

    def drawNose(self):
          if self.noseSize == "extra extra extra large":
                dot(self.size/5)
          elif self.noseSize == "extra extra extra extra large":
            dot(self.size/6)
          else:
            dot(self.size/245)
          self.goHome()

    

f1 = smile(xpos=0, ypos=0)
f1.draw()

turtle.forward(200)

showturtle()
done()