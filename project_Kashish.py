import turtle

def draw_benzene_ring(x, y, pen):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

    for _ in range(100):
        pen.pencolor(colors[_ % 6])
        pen.width(_ // 100 + 1)
        pen.forward(_)
        pen.left(59)

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor('black')

# Create multiple turtles for drawing at different positions
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(0)  # Set the speed to 3

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.speed(0)  # Set the speed to 3

turtle3 = turtle.Turtle()
turtle3.shape("turtle")
turtle3.speed(0)  # Set the speed to 3

turtle4 = turtle.Turtle()
turtle4.shape("turtle")
turtle4.speed(0)  # Set the speed to 3

turtle5 = turtle.Turtle()
turtle5.shape("turtle")
turtle5.speed(0)  # Set the speed to 3

# Draw the benzene rings at different positions to the left
def call_benzene_ring():
    draw_benzene_ring(-400, 200, turtle1)
    draw_benzene_ring(-50, 0, turtle2)
    draw_benzene_ring(-350, -200, turtle3)
    draw_benzene_ring(300, 300, turtle4)
    draw_benzene_ring(200, -250, turtle5)

call_benzene_ring()

# Keep the window open
turtle.done()
