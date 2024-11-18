import turtle

turtle.hideturtle()

# Fonction pour dessiner la grille
def draw_grid(size, cell_size):
    for i in range(size):
        for j in range(size):
            for _ in range(4):
                turtle.forward(cell_size)
                turtle.right(90)
            turtle.forward(cell_size)
        turtle.backward(cell_size * size)
        turtle.right(90)
        turtle.forward(cell_size)
        turtle.left(90)

def write_number_in_cell(x, y, number):
    turtle.penup()
    turtle.setposition(x + 25, y - 35)  
    turtle.write(str(number), align="center", font=("Arial", 16, "normal"))
    turtle.pendown()  

size = 3 
cell_size = 60 

turtle.speed(-500)  
turtle.penup()
turtle.setposition(-cell_size * size / 2, cell_size * size / 2) 
turtle.pendown()

draw_grid(size, cell_size)

write_number_in_cell(-cell_size, cell_size, 1)  
write_number_in_cell(0, cell_size, 2)        
write_number_in_cell(cell_size, cell_size, 3)    
write_number_in_cell(-cell_size, 0, 4)     
write_number_in_cell(0, 0, 5)                 
write_number_in_cell(cell_size, 0, 6)     
write_number_in_cell(-cell_size, -cell_size, 7)    
write_number_in_cell(0, -cell_size, 8)             
write_number_in_cell(cell_size, -cell_size, 9)      

def draw_circle(x, y, color):
    turtle.penup()
    turtle.goto(x - 10, y - 10)  # Ajuste la position pour centrer le cercle
    turtle.pendown()
    turtle.fillcolor(color)  
    turtle.begin_fill()     
    turtle.circle(20)       
    turtle.end_fill()       
    turtle.penup()

def draw_cross(x, y):
    turtle.penup()
    turtle.goto(x - 20, y - 20)
    turtle.pendown()
    turtle.goto(x + 20, y + 20)
    turtle.penup()
    turtle.goto(x + 20, y - 20)
    turtle.pendown()
    turtle.goto(x - 20, y + 20)
    turtle.penup()

def check_win(case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9):
    # Vérification des lignes horizontales
    if (case_1 == 'X' and case_2 == 'X' and case_3 == 'X') or (case_4 == 'X' and case_5 == 'X' and case_6 == 'X') or (case_7 == 'X' and case_8 == 'X' and case_9 == 'X'):
        return 'black'
    # Vérification des lignes verticales
    if (case_1 == 'X' and case_4 == 'X' and case_7 == 'X') or (case_2 == 'X' and case_5 == 'X' and case_8 == 'X') or (case_3 == 'X' and case_6 == 'X' and case_9 == 'X'):
        return 'black'
    # Vérification des diagonales
    if (case_1 == 'X' and case_5 == 'X' and case_9 == 'X') or (case_3 == 'X' and case_5 == 'X' and case_7 == 'X'):
        return 'black'
    # Répéter pour 'O' ou d'autres conditions de victoire
    if (case_1 == 'O' and case_2 == 'O' and case_3 == 'O') or (case_4 == 'O' and case_5 == 'O' and case_6 == 'O') or (case_7 == 'O' and case_8 == 'O' and case_9 == 'O'):
        return 'white'
    # Vérification des lignes verticales
    if (case_1 == 'O' and case_4 == 'O' and case_7 == 'O') or (case_2 == 'O' and case_5 == 'O' and case_8 == 'O') or (case_3 == 'O' and case_6 == 'O' and case_9 == 'O'):
        return 'white'
    # Vérification des diagonales
    if (case_1 == 'O' and case_5 == 'O' and case_9 == 'O') or (case_3 == 'O' and case_5 == 'O' and case_7 == 'O'):
        return 'white'
    return None

def display_winner(winner):
    turtle.textinput("Victoire", f"Joueur {winner} a gagné!")
    turtle.bye()  # Ferme la fenêtre Turtle
    exit()  # Quitte le programme

# Dans la boucle principale

def get_coordinates(choice):
    if choice == 1:
        return (-cell_size, cell_size)
    elif choice == 2:
        return (0, cell_size)
    elif choice == 3:
        return (cell_size, cell_size)
    elif choice == 4:
        return (-cell_size, 0)
    elif choice == 5:
        return (0, 0) 
    elif choice == 6:
        return (cell_size, 0)
    elif choice == 7:
        return (-cell_size, -cell_size)
    elif choice == 8:
        return (0, -cell_size)
    elif choice == 9:
        return (cell_size, -cell_size)

# Initialisation des choix des joueurs
symbol_player_1 = 'X'
symbol_player_2 = 'O'
color_player_1 = 'black'  # Couleur pour le premier joueur
color_player_2 = 'white'  # Couleur pour le second joueur

# Initialisation des choix des joueurs
case_1 = None
case_2 = None
case_3 = None
case_4 = None
case_5 = None
case_6 = None
case_7 = None
case_8 = None
case_9 = None
tour = 0
cell_size = 50 

# Dans la boucle principale
for i in range(9):
    while True:
        player_choice = turtle.textinput("Choix du joueur", f"Joueur {symbol_player_1 if tour % 2 == 0 else symbol_player_2}, choisissez une case (1-9): ")

        if player_choice:
            player_choice = int(player_choice)
            if 1 <= player_choice <= 9:
                # Vérifier si le choix a déjà été fait
                if player_choice == 1 and case_1 is None:
                    case_1 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(-cell_size, cell_size, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 2 and case_2 is None:
                    case_2 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(0, cell_size, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 3 and case_3 is None:
                    case_3 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(cell_size, cell_size, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 4 and case_4 is None:
                    case_4 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(-cell_size, 0, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 5 and case_5 is None:
                    case_5 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(0, 0, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 6 and case_6 is None:
                    case_6 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(cell_size, 0, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 7 and case_7 is None:
                    case_7 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(-cell_size, -cell_size, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 8 and case_8 is None:
                    case_8 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(0, -cell_size, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                elif player_choice == 9 and case_9 is None:
                    case_9 = symbol_player_1 if tour % 2 == 0 else symbol_player_2
                    draw_circle(cell_size, -cell_size, color_player_1 if tour % 2 == 0 else color_player_2)  # Dessiner un cercle
                else:
                    turtle.textinput("Case occupée", "Cette case est déjà occupée. Choisissez une autre case.")  # Afficher un message d'erreur
                    continue  # Continuer à demander un choix

                # Vérifier si le joueur a gagné seulement après 4 coups
                if tour >= 4:  # Vérifier seulement après 5 coups
                    winner = check_win(case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9)
                    if winner:
                        display_winner(winner)

                tour += 1  # Passer au tour suivant
                break  # Sortir de la boucle pour le prochain tour
        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 9.")
turtle.done()
