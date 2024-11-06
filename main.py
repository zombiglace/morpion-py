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

#demande user
tour = 0
choix_1 = choix_2 = choix_3 = choix_4 = choix_5 = choix_6 = choix_7 = choix_8 = choix_9 = None


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
                

                    def verifier_gagnant(tour, choix_1, choix_2, choix_3):
                        if tour % 2 == 0:
                            if choix_1 and choix_2 and choix_3:
                                print("Les ronds ont gagné !")
                                turtle.done()
                                return True
                        else:  # C'est le tour du joueur 2
                            if choix_1 and choix_2 and choix_3:
                                print("Les croix ont gagné !")

                                turtle.done()
                        return False

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
