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


