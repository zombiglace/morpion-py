import turtle

# Création de la fenêtre turtle
win = turtle.Screen()
win.setup(800, 800)

# Création de la tortue
t = turtle.Turtle()
t.speed(3)

# Définition de la taille de la grille
size = 3
cell_size = 100

# Fonction pour dessiner la grille
def draw_grid(size, cell_size):
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

# Dessin de la grille
draw_grid(size, cell_size)

# Demande de la case
case = win.textinput("Demande de case", "Entrez la case (ligne, colonne) : ")


if case:
    try:
        ligne, colonne = map(int, case.split(','))
        if 1 <= ligne <= size and 1 <= colonne <= size:
            # Dessin de la case sélectionnée
            t.penup()
            t.goto((colonne - 1) * cell_size, (ligne - 1) * cell_size)
            t.pendown()
            t.fillcolor('red')
            t.begin_fill()
            for _ in range(4):
                t.forward(cell_size)
                t.right(90)
            t.end_fill()
        else:
            print("Case invalide")
    except ValueError:
        print("Erreur de saisie")


if case == 1:
	print('caca')
# Fermeture de la fenêtre turtle
turtle.done()



