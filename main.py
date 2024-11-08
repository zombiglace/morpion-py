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
    turtle.goto(x, y - 20) 
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


def check_win(choix_1, choix_2, choix_3, choix_4, choix_5, choix_6, choix_7, choix_8, choix_9):
    # Vérification des lignes horizontales
    if (choix_1 == 'X' and choix_2 == 'X' and choix_3 == 'X') or (choix_4 == 'X' and choix_5 == 'X' and choix_6 == 'X') or (choix_7 == 'X' and choix_8 == 'X' and choix_9 == 'X'):
        return 'black'
    # Vérification des lignes verticales
    if (choix_1 == 'X' and choix_4 == 'X' and choix_7 == 'X') or (choix_2 == 'X' and choix_5 == 'X' and choix_8 == 'X') or (choix_3 == 'X' and choix_6 == 'X' and choix_9 == 'X'):
        return 'black'
    # Vérification des diagonales
    if (choix_1 == 'X' and choix_5 == 'X' and choix_9 == 'X') or (choix_3 == 'X' and choix_5 == 'X' and choix_7 == 'X'):
        return 'black'
    # Répéter pour 'O' ou d'autres conditions de victoire
    if (choix_1 == 'O' and choix_2 == 'O' and choix_3 == 'O') or (choix_4 == 'O' and choix_5 == 'O' and choix_6 == 'O') or (choix_7 == 'O' and choix_8 == 'O' and choix_9 == 'O'):
        return 'white'
    # Vérification des lignes verticales
    if (choix_1 == 'O' and choix_4 == 'O' and choix_7 == 'O') or (choix_2 == 'O' and choix_5 == 'O' and choix_8 == 'O') or (choix_3 == 'O' and choix_6 == 'O' and choix_9 == 'O'):
        return 'white'
    # Vérification des diagonales
    if (choix_1 == 'O' and choix_5 == 'O' and choix_9 == 'O') or (choix_3 == 'O' and choix_5 == 'O' and choix_7 == 'O'):
        return 'white'
    return None  # Aucun gagnant

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


# Initialisation des choix des joueurs
# Initialisation des symboles et du tour
joueur_symbols = ['O', 'X']
tour = 0

# Initialisation des positions
case_1 = None
case_2 = None
case_3 = None
case_4 = None
case_5 = None
case_6 = None
case_7 = None
case_8 = None
case_9 = None

# Fonction pour afficher le plateau
def afficher_plateau():
    print(f"{case_1 or '1'} | {case_2 or '2'} | {case_3 or '3'}")
    print("--+---+--")
    print(f"{case_4 or '4'} | {case_5 or '5'} | {case_6 or '6'}")
    print("--+---+--")
    print(f"{case_7 or '7'} | {case_8 or '8'} | {case_9 or '9'}")

# Fonction principale du jeu
def jouer():
    global tour, case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9
    while True:
        afficher_plateau()
        choix = input(f"Joueur {joueur_symbols[tour % 2]} choisissez une case (1-9) : ")

        # Validation de l'entrée
        if choix.isdigit() and 1 <= int(choix) <= 9:
            case_num = int(choix)

            # Vérification si la case est déjà prise
            if case_num == 1 and case_1 is None:
                case_1 = joueur_symbols[tour % 2]
            elif case_num == 2 and case_2 is None:
                case_2 = joueur_symbols[tour % 2]
            elif case_num == 3 and case_3 is None:
                case_3 = joueur_symbols[tour % 2]
            elif case_num == 4 and case_4 is None:
                case_4 = joueur_symbols[tour % 2]
            elif case_num == 5 and case_5 is None:
                case_5 = joueur_symbols[tour % 2]
            elif case_num == 6 and case_6 is None:
                case_6 = joueur_symbols[tour % 2]
            elif case_num == 7 and case_7 is None:
                case_7 = joueur_symbols[tour % 2]
            elif case_num == 8 and case_8 is None:
                case_8 = joueur_symbols[tour % 2]
            elif case_num == 9 and case_9 is None:
                case_9 = joueur_symbols[tour % 2]
            else:
                print("Cette case est déjà prise. Choisissez une autre case.")
                continue

            # Changer de tour
            tour += 1
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 9.")

# Lancer le jeu
jouer()

for i in range(9):
    while True:
        player_choice = turtle.textinput("Choisissez un nombre", "Choisissez un nombre entre 1 et 9:")
        
        if player_choice:
            player_choice = int(player_choice)
            if 1 <= player_choice <= 9:
                # Vérifie si le choix a déjà été fait
                if choix[player_choice - 1] is None:  # Vérifie si la case est vide
                    choix[player_choice - 1] = joueur_symbols[tour % 2]  # Assigne le symbole au choix
                    
                    # Vérifie si le joueur a gagné seulement après 4 coups
                    if tour >= 4:  # Vérifier seulement après 5 coups
                        winner = check_win(*choix)
                        if winner:
                            display_winner(winner)
                            turtle.bye()  # Ferme la fenêtre Turtle
                            exit()  # Quitte le programme
                    
                    x, y = get_coordinates(player_choice)

                    if tour % 2 == 0:
                        draw_circle(x, y, "white")
                    else:
                        draw_circle(x, y, "black") 
                    
                    tour += 1
                    break
                else:
                    turtle.textinput("Erreur", "Ce nombre a déjà été choisi. Veuillez en choisir un autre.")
            else:
                turtle.textinput("Erreur", "Veuillez entrer un nombre valide entre 1 et 9.")
        else:
            turtle.textinput("Erreur", "Veuillez entrer un nombre valide entre 1 et 9.")
#win condition
turtle.done()
#win condition
