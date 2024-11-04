import turtle

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


turtle.speed(-80)  
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



#demande user
for i in range(9):

    player_choice = turtle.textinput("Choisissez un nombre", "Choisissez un nombre entre 1 et 9:")

    
#rond/croix
def draw_circle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(20)
    turte.penup()

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

#win condition


turtle.done()
