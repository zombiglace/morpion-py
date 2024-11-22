Introduction Ce rapport fournit un aperçu détaillé de notre projet de création d'un jeu de morpion (Tic-Tac-Toe) en Python avec la bibliothèque Turtle. Nous avons travaillé sur la conception d'une interface graphique, la gestion des interactions utilisateur et l'implémentation de la logique du jeu.

Difficultés rencontrées Nous avons rencontré plusieurs défis, notamment :

La vérification des conditions de victoire : La mise en place d'une logique fiable pour déterminer le gagnant a nécessité de nombreux tests pour s'assurer que toutes les conditions étaient bien prises en compte.

Partage des tâches Nous avons réparti les tâches de la manière suivante :
Conception de l'interface : Ronan a créé l'interface graphique avec Turtle.
Logique du jeu : Stéphane et Julien ont développé la logique, y compris la gestion des tours et la vérification des gagnants.
Tests et débogage : Julien s'est concentré sur les tests et le débogage pour garantir le bon fonctionnement du programme.

Gestion du temps Nous avons travaillé sur le projet certains mercredis et pendant les cours.

Partage d'informations Nous avons utilisé un chat créé par Julien, mais celui-ci a été bloqué par le lycée le 3 novembre, ce qui a causé des problèmes de communication. Pour le partage de code, nous avons utilisé GitHub.

Choix de structure de données Nous avons opté pour des variables simples pour stocker les choix des joueurs (case_1 à case_9) en tant que nombres. Cela a facilité la gestion des valeurs et simplifié la vérification des conditions de victoire. Nous avons commencé par définir les cases du jeu, suivi par les interactions, puis les conditions de victoire.

Algorithmes mis en œuvre
Détermination des coordonnées : L'algorithme get_coordinates associe chaque numéro de case à ses coordonnées sur la grille.
Vérification du vainqueur : L'algorithme check_win vérifie si un joueur a gagné en contrôlant les lignes, colonnes et diagonales.

Interaction avec l'utilisateur L'interaction avec l'utilisateur se fait via des fenêtres de saisie de texte, permettant aux joueurs de choisir un numéro entre 1 et 9. Cela rend l'interface simple et intuitive.

Réutilisation de code Nous avons réutilisé des concepts et des structures de code appris en classe, notamment pour la gestion des entrées et le dessin avec Turtle et par des sites internet ainsi que des forums. 
if player_choice == 1 and case_1 is None: (is None)
Méthodes de mise au point, validation et débogage Nous avons mis en place des tests unitaires pour valider les fonctions essentielles, comme get_coordinates et check_win. À chaque ajout de fonctionnalité, nous avons intégré des tests pour prévenir les régressions. De plus, des sessions de débogage en groupe ont été organisées pour résoudre les problèmes ensemble.

Outils utilisés Nous avons utilisé les environnements de développement Idle, VSCode et Code Writer pour le développement du projet.
