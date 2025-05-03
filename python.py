import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(3)

# Start drawing the heart shape
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# Hide the turtle after drawing
pen.hideturtle()

# Finish
turtle.done()
