Rapport de Projet
Introduction
Ce rapport présente un compte rendu détaillé de notre travail sur le projet de développement d'un jeu de morpion (Tic-Tac-Toe) en utilisant Python et la bibliothèque Turtle. Le projet a impliqué la conception d'une interface graphique, la gestion des interactions avec les utilisateurs, ainsi que la mise en œuvre de la logique du jeu.

Difficultés Rencontrées
Au cours du développement, plusieurs difficultés ont été rencontrées :

Vérification des Conditions de Victoire : Implémenter une logique robuste pour déterminer si un joueur a gagné a nécessité des tests approfondis pour s'assurer que toutes les conditions étaient couvertes.

Partage des Tâches
Dans notre groupe, nous avons divisé les tâches comme suit :

Conception de l'Interface : Un membre a pris en charge la création de l'interface graphique en utilisant Turtle.

Logique du Jeu : J'ai été responsable de l'implémentation de la logique du jeu, y compris la gestion des tours, la vérification des gagnants et la gestion des entrées.

Tests et Débogage : Un autre membre s'est concentré sur les tests et le débogage, en s'assurant que le programme fonctionnait comme prévu.

Gestion du Temps
Nous avons établi travaillé sur le projet certains mercredi ainsi qu'en cours.

Partage d'Informations
Nous avons utilisé un chat créer par julien qui a été bloquer par le lycée ce lundi 3 Novembre ce qui nous a ensuite causer des problemes de communication, et pour le partage du code nous avons utilisé github.

Choix de Structure de Données
Pour ce projet, j'ai choisi d'utiliser des variables simples pour stocker les choix des joueurs (choix_1 à choix_9) en tant que nombres. Cette approche a permis une gestion facile des valeurs et a simplifié la vérification des conditions de victoire. Une liste aurait pu être utilisée, mais cela aurait introduit une complexité supplémentaire dans la gestion des indices.
et nous nous sommes organisé pour commencé par les cases du jeux les interractions et les win conditions

Algorithmes Mis en Œuvre
Détermination des Coordonnées : L'algorithme get_coordinates prend en entrée un numéro de case et renvoie les coordonnées correspondantes. Cela se fait par une série de conditions if qui associent chaque numéro à ses coordonnées sur la grille.

python
Insert Code
Edit
Copy code
def get_coordinates(choice):
    if choice == 1:
        return (-cell_size, cell_size)
    # ... autres conditions
Vérification du Vainqueur : L'algorithme check_win vérifie si un joueur a gagné en vérifiant les lignes, colonnes et diagonales. Cela se fait par des vérifications conditionnelles qui comparent les choix des joueurs.

python
Insert Code
Edit
Copy code
def check_win(choix_1, choix_2, choix_3, choix_4, choix_5, choix_6, choix_7, choix_8, choix_9, joueur):
    # Vérification des lignes, colonnes et diagonales
Autres Algorithmes :

Dessin de la Grille : Un algorithme simple pour dessiner la grille de jeu.
Dessin des Symboles : Des fonctions pour dessiner des cercles et des croix.
Interaction avec l'Utilisateur
L'interaction avec l'utilisateur a été mise en place via des fenêtres de saisie de texte pour permettre aux joueurs de choisir un numéro entre 1 et 9. Ce choix a été fait pour rendre l'interface simple et intuitive, tout en évitant les complications d'une interface graphique plus complexe.

Réutilisation de Code
ont a réutilisé des concepts et des structures de code qu ont a appris en classe, notamment en ce qui concerne la gestion des entrées et le dessin avec Turtle. ont a également consulté des ressources en ligne pour des fonctions non vu comme ceci:

if player_choice not in [choix_1, choix_2, choix_3, choix_4, choix_5, choix_6, choix_7, choix_8, choix_9]:

avec la notion de not in ce qui nous permet de faire en sortent que le joueur ne puissent pas ecrire 2 fois le meme nombres

Méthodes de Mise au Point, Validation et Débogage
Ont a mis en place des tests unitaires pour valider les fonctions critiques, comme get_coordinates et check_win. Chaque fois qu'une fonctionnalité était ajoutée, ont s'assurais de l'intégrer dans les tests pour garantir qu'aucune régression ne se produisait. De plus, des sessions de débogage en groupe ont été organisées pour examiner les problèmes ensemble et trouver des solutions efficaces.
