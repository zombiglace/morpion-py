Introduction :

Ce rapport présente un compte rendu détaillé de notre projet de développement d'un jeu de morpion en utilisant Python et la bibliothèque Turtle.

Difficultés rencontrées :

Nous avons rencontré plusieurs difficultés lors du développement, notamment la vérification des conditions de victoire et la gestion des interactions avec les utilisateurs.

Partage des tâches :

Nous avons divisé les tâches en trois parties : conception de l'interface graphique (Ronan), logique du jeu et tests et débogage(julien et stephane).

Gestion du temps :

Nous avons travaillé sur le projet certains mercredis et en cours.

Partage d'informations :

Nous avons utilisé un chat créer par julien qui a été bloquer le lundi 3 novembre par le lycée. Ainsi que GitHub pour partager les informations et le code.

Choix de structure de données :

Nous avons choisi d'utiliser des variables simples pour stocker les choix des joueurs.
 ( case_1 = None case_2 = None case_3 = None case_4 = None case_5 = None case_6 = None case_7 = None case_8 = None case_9 = None) en tant que nombres

Algorithmes mis en œuvre :

Nous avons mis en œuvre plusieurs algorithmes, notamment pour déterminer les coordonnées (L'algorithme get_coordinates prend en entrée un numéro de case et renvoie les coordonnées correspondantes. Cela se fait par une série de conditions if qui associent chaque numéro à ses coordonnées sur la grille.)

def get_coordinates(choice): if choice == 1: return (-cell_size, cell_size) elif choice == 2: return (0, cell_size) elif choice == 3: return (cell_size, cell_size) elif choice == 4: return (-cell_size, 0) elif choice == 5: return (0, 0) elif choice == 6: return (cell_size, 0) elif choice == 7: return (-cell_size, -cell_size) elif choice == 8: return (0, -cell_size) elif choice == 9: return (cell_size, -cell_size) vérifier les conditions de victoire 
(def check_win(case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8, case_9): # Vérification des lignes horizontales if (case_1 == 'X' and case_2 == 'X' and case_3 == 'X') or (case_4 == 'X' and case_5 == 'X' and case_6 == 'X') or (case_7 == 'X' and case_8 == 'X' and case_9 == 'X'): return 'black' # Vérification des lignes verticales if (case_1 == 'X' and case_4 == 'X' and case_7 == 'X') or (case_2 == 'X' and case_5 == 'X' and case_8 == 'X') or (case_3 == 'X' and case_6 == 'X' and case_9 == 'X'): return 'black' # Vérification des diagonales if (case_1 == 'X' and case_5 == 'X' and case_9 == 'X') or (case_3 == 'X' and case_5 == 'X' and case_7 == 'X'): return 'black' # Répéter pour 'O' ou d'autres conditions de victoire if (case_1 == 'O' and case_2 == 'O' and case_3 == 'O') or (case_4 == 'O' and case_5 == 'O' and case_6 == 'O') or (case_7 == 'O' and case_8 == 'O' and case_9 == 'O'): return 'white' # Vérification des lignes verticales if (case_1 == 'O' and case_4 == 'O' and case_7 == 'O') or (case_2 == 'O' and case_5 == 'O' and case_8 == 'O') or (case_3 == 'O' and case_6 == 'O' and case_9 == 'O'): return 'white' # Vérification des diagonales if (case_1 == 'O' and case_5 == 'O' and case_9 == 'O') or (case_3 == 'O' and case_5 == 'O' and case_7 == 'O'): return 'white' return None)

ou bien dessiner la grille et les symboles.

Interaction avec l'utilisateur :

Nous avons mis en place une interaction avec l'utilisateur via des fenêtres de saisie de texte pour permettre aux joueurs de choisir un numéro entre 1 et 9.

Réutilisation de code :

Nous avons réutilisé des concepts et des structures de code appris en classe, notamment pour la gestion des entrées et le dessin avec Turtle et par des sites internet ainsi que des forums.
if player_choice == 1 and case_1 is None:
(is None)

Méthodes de mise au point, validation et débogage Nous avons mis en place des tests unitaires pour valider les fonctions critiques et avons organisé des sessions de débogage en groupe pour examiner les problèmes ensemble.

Outils utilisés :

Nous avons utilisé Idle, VSCode et Code Writer pour développer le projet.
