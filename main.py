

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

def draw_circle(x, y):
    turtle.penup()
    turtle.goto(x, y - 20) 
    turtle.pendown()
    turtle.circle(20)
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


def check_win(choix_1, choix_2, choix_3, choix_4, choix_5, choix_6, choix_7, choix_8, choix_9, joueur):
    # Vérification des lignes
    if (choix_1 == joueur and choix_2 == joueur and choix_3 == joueur) or \
       (choix_4 == joueur and choix_5 == joueur and choix_6 == joueur) or \
       (choix_7 == joueur and choix_8 == joueur and choix_9 == joueur):
        return True

    # Vérification des colonnes
    if (choix_1 == joueur and choix_4 == joueur and choix_7 == joueur) or \
       (choix_2 == joueur and choix_5 == joueur and choix_8 == joueur) or \
       (choix_3 == joueur and choix_6 == joueur and choix_9 == joueur):
        return True

    # Vérification des diagonales
    if (choix_1 == joueur and choix_5 == joueur and choix_9 == joueur) or \
       (choix_3 == joueur and choix_5 == joueur and choix_7 == joueur):
        return True

    return False
#demande user

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

tour = 0
choix_1 = choix_2 = choix_3 = choix_4 = choix_5 = choix_6 = choix_7 = choix_8 = choix_9 = None


for i in range(9):
    while True:
        player_choice = turtle.textinput("Choisissez un nombre", "Choisissez un nombre entre 1 et 9:")
        
        if player_choice:
            player_choice = int(player_choice)
            if 1 <= player_choice <= 9:
                # Vérifie si le choix a déjà été fait
                if player_choice not in [choix_1, choix_2, choix_3, choix_4, choix_5, choix_6, choix_7, choix_8, choix_9]:
                    # Assigne le choix à la variable correspondante
                    if tour == 0:
                        choix_1 = player_choice
                    elif tour == 1:
                        choix_2 = player_choice
                    elif tour == 2:
                        choix_3 = player_choice
                    elif tour == 3:
                        choix_4 = player_choice
                    elif tour == 4:
                        choix_5 = player_choice
                    elif tour == 5:
                        choix_6 = player_choice
                    elif tour == 6:
                        choix_7 = player_choice
                    elif tour == 7:
                        choix_8 = player_choice
                    elif tour == 8:
                        choix_9 = player_choice

                    if check_win(choix_1, choix_2, choix_3, choix_4, choix_5, choix_6, choix_7, choix_8, choix_9, player_choice):
                        turtle.textinput("Victoire", f"Joueur {tour % 2 + 1} a gagné!")
                        turtle.bye()  # Ferme la fenêtre Turtle
                        exit()  # Quitte le programme
                
                    x, y = get_coordinates(player_choice)

                    if tour % 2 == 0:
                        draw_circle(x, y) 
                    else:
                        draw_cross(x, y) 
                    
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
