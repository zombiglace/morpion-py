Rapport de Projet
Introduction
Ce rapport présente un compte rendu détaillé de notre travail sur le projet de développement d'un jeu de morpion (Tic-Tac-Toe) en utilisant Python et la bibliothèque Turtle. Le projet a impliqué la conception d'une interface graphique, la gestion des interactions avec les utilisateurs, ainsi que la mise en œuvre de la logique du jeu.

Difficultés Rencontrées
Au cours du développement, plusieurs difficultés ont été rencontrées :

Vérification des Conditions de Victoire : Implémenter une logique robuste pour déterminer si un joueur a gagné a nécessité des tests approfondis pour s'assurer que toutes les conditions étaient couvertes, ainsi que le systeme de tour.  

Partage des Tâches
Dans notre groupe, nous avons divisé les tâches comme :

Conception de l'Interface : Ronan a pris en charge la création de l'interface graphique en utilisant Turtle.

Logique du Jeu : Stephane et julien ont été responsable de l'implémentation de la logique du jeu, y compris la gestion des tours, la vérification des gagnants et la gestion des entrées.

Tests et Débogage : Julien s'est concentré sur les tests et le débogage, en s'assurant que le programme fonctionnait comme prévu.

Gestion du Temps
Nous avons travaillés sur le projet certains mercredi ainsi qu'en cours.

Partage d'Informations
Nous avons utilisé un chat créer par julien qui a été bloquer par le lycée le lundi 3 Novembre ce qui nous a ensuite causer des problemes de communication, et pour le partage du code nous avons utilisé github.

Choix de Structure de Données
Pour ce projet, nous avons choisi d'utiliser des variables simples pour stocker les choix des joueurs (
case_1 = None
case_2 = None
case_3 = None
case_4 = None
case_5 = None
case_6 = None
case_7 = None
case_8 = None
case_9 = None)
en tant que nombres. Cette approche a permis une gestion facile des valeurs et a simplifié la vérification des conditions de victoire.
Nous nous sommes organisé pour commencé par les cases du jeux les interractions puis nous avons suivi par la win conditions.

Algorithmes Mis en Œuvre
Détermination des Coordonnées : L'algorithme get_coordinates prend en entrée un numéro de case et renvoie les coordonnées correspondantes. Cela se fait par une série de conditions if qui associent chaque numéro à ses coordonnées sur la grille.

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

Vérification du Vainqueur : L'algorithme check_win vérifie si un joueur a gagné en vérifiant les lignes, colonnes et diagonales. Cela se fait par des vérifications conditionnelles qui comparent les choix des joueurs.

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

Autres Algorithmes :

Dessin de la Grille : Un algorithme simple pour dessiner la grille de jeu.
Dessin des Symboles : Des fonctions pour dessiner des cercles de couleur.
Interaction avec l'Utilisateur
L'interaction avec l'utilisateur a été mise en place via des fenêtres de saisie de texte pour permettre aux joueurs de choisir un numéro entre 1 et 9. Ce choix a été fait pour rendre l'interface simple et intuitive, tout en évitant les complications d'une interface graphique plus complexe.

Réutilisation de Code
ont a réutilisé des concepts et des structures de code qu ont a appris en classe, notamment en ce qui concerne la gestion des entrées et le dessin avec Turtle. ont a également consulté des ressources en ligne pour des fonctions non vu comme ceci:

if player_choice == 1 and case_1 is None:

avec la notion de is None ce qui nous permet de faire en sortent que le joueur puissent assigner un rond a la case demandé.

Méthodes de Mise au Point, Validation et Débogage
Ont a mis en place des tests unitaires pour valider les fonctions critiques, comme get_coordinates et check_win. Chaque fois qu'une fonctionnalité était ajoutée, ont s'assurais de l'intégrer dans les tests pour garantir qu'aucune régression ne se produisait. De plus, des sessions de débogage en groupe ont été organisées pour examiner les problèmes ensemble et trouver des solutions efficaces.

Nous avons utilisé idle,vscode, et code writer
