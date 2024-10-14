import turtle

#variable cases

#interraction

#grille
t = turtle.Turtle()

size = 3

cell_size = 30

for i in range(size):
    for j in range(size):
        for _ in range(4):
            t.forward(cell_size)
            t.right(90)
        t.forward(cell_size)

    t.backward(cell_size * size)
    t.right(90)
    t.forward(cell_size)
    t.left(90)

turtle.done()


# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
my_turtle = turtle.Turtle()

# Draw a square
for i in range(4):
    my_turtle.forward(100)  # move forward by 100 units
    my_turtle.right(90)     # turn right by 90 degrees

# Keep the window open until the user closes it
turtle.done()
input("nom")
#verification victoire

