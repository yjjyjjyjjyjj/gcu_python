import random
import turtle

def drawTree(branch,t):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        drawTree(branch-random.randint(1,50), t)
        t.left(40)
        drawTree(branch-random.randint(1,50), t)
        t.right(20)
        t.backward(branch)

def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("blue")
    drawTree(100, t)
    window.exitonclick()

main()