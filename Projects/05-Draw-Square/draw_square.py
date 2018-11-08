import turtle
# Why the fuck is this called turtle?
# https://docs.python.org/2/library/turtle.html

# Functions

def drawSquare(some_turtle, raio):
    # @param some_turtle: object
    # @param raio: Raio que sera criado na circunferencia
    for i in range(4):
        some_turtle.forward(raio)
        some_turtle.right(90)

def drawCrazySquareCircle(some_turtle, loopDistance, circleAmount, raio):
    # @param some_turtle: object
    # @param loopDistance: Distance from one shape to another
    # @param circleAmount: Raio que sera criado na circunferencia
    # @param raio: Raio que sera criado na circunferencia
    for i in range(circleAmount):
        drawSquare(some_turtle, raio)
        some_turtle.right(loopDistance)

def drawTriangle(some_turtle, raio):
    for i in range(3):
        some_turtle.forward(raio)
        some_turtle.right(120)

def drawCrazyFlower(some_turtle, loopDistance, circleAmount, raio):
    for i in range(circleAmount):
        drawTriangle(some_turtle, raio)
        some_turtle.right(loopDistance)

def drawInitials(some_turtle):
    some_turtle.penup()
    some_turtle.setpos(- 150, 0)
    some_turtle.pendown()
    
    some_turtle.left(90)
    some_turtle.forward(150)

    some_turtle.right(90+45)
    some_turtle.forward(200)

    some_turtle.left(90+45)
    some_turtle.forward(150)

    xNow = some_turtle.xcor()
    yNow = some_turtle.ycor()

    some_turtle.penup()
    some_turtle.setpos(xNow + 50, yNow)
    some_turtle.pendown()

    some_turtle.right(180)
    some_turtle.forward(150)

    some_turtle.left(90)
    some_turtle.forward(150)


def draw_shape():
    # Function Start
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle() # brad Instance of Turtle Class created and initialized
    brad.shape("turtle") # https://docs.python.org/2/library/turtle.html#turtle.shape
    brad.color("white") # https://docs.python.org/2/library/turtle.html#turtle.color
    brad.speed(1000) # https://docs.python.org/2/library/turtle.html#turtle.speed
    brad.pensize(2)
    
    angie = turtle.Turtle() # angie Instance of Turtle Class
    angie.shape("arrow")
    angie.color("green")
    angie.pensize(5)
    #angie.circle(100)

    zelda = turtle.Turtle() # zelda Instance of Turtle Class
    zelda.shape("arrow")
    zelda.color("white")
    zelda.pensize(7)
    zelda.speed(1)

    # object; Distance from each shape ; Amount of Shapes; Size Sides Forward Shape(Raio)
    drawCrazySquareCircle(brad, 5, 72, 100)
    drawCrazySquareCircle(brad, 10, 36, 200)
    brad.reset()

    brad = turtle.Turtle() # brad Instance of Turtle Class created and initialized
    brad.shape("turtle") # https://docs.python.org/2/library/turtle.html#turtle.shape
    brad.color("white") # https://docs.python.org/2/library/turtle.html#turtle.color
    brad.speed(50000) # https://docs.python.org/2/library/turtle.html#turtle.speed
    brad.pensize(1)

    drawCrazyFlower(brad, 25, 72, 100)
    brad.pensize(2)
    drawCrazyFlower(brad, 75, 36, 300)
    brad.reset()

    brad = turtle.Turtle() # brad Instance of Turtle Class created and initialized
    brad.shape("turtle") # https://docs.python.org/2/library/turtle.html#turtle.shape
    brad.color("white") # https://docs.python.org/2/library/turtle.html#turtle.color
    brad.speed(5) # https://docs.python.org/2/library/turtle.html#turtle.speed
    brad.pensize(2)
 
    for i in range(50):
        drawInitials(brad)
        brad.speed(5+i) # https://docs.python.org/2/library/turtle.html#turtle.speed
        brad.pensize(3+i)
    
    brad.reset()






    #for i in range(3):
        #zelda.left(120)  
        #zelda.forward(100)
        

    window.exitonclick()
    # Function End





draw_shape()