# morpion-py

p1 - grille

p2- choix de l utilisateur

p3- systeme de tour rond black/white

p4-verifier les conditions de victoire
  


  
p4-fonction que genere le jeux

Répondre aux questions suivantes en rédigeant de manière à avoir une trace écrite.
Quelle balise indique qu’il s’agit d’un type de document HTML ?

La balise 
 <html lang='fr'></html> permet de dire que c est du code html

Quelle balise indique le début du document HTML ?

 <!DOCTYPE html> est le debut du document

Quelle différence constatez-vous entre les balises (head, body, footer) et (h1, h2, p) ?
head contient toute les metadata et le titre de la page qui s safficherea en haut a gauche
body est la partie principale du site et le footer est fait par le bas de la page (généralement dans les site c est les informations/moyen de contacte)


A la suite de cette explication, indiquer combien de parties constituent un document
HTML ?
Il y a 2 parties <head> qui correspond au metadata et <body> qui est la partie afficher du site

Quelles sont les parties de la page qui seront affichées à l’utilisateur ?

	<h1>Ma première page web</h1>
	<br>
	<h2>groupe NSI</h2>
	<hr>
	<h2> Lycée Polyvalent du pays d'Aunis </p>
	<h3><p style='text-align:right;color:red;font-weight:bold'>Interactions entre l’homme et la machine sur le Web </p>
	
	<p> <center>Lors de la navigation sur le Web, les internautes interagissent avec leur machine par le biais des pages Web.</center><br> 
	L’Interface Homme-Machine (IHM) repose sur la gestion d’événements associés à des 	éléments graphiques munis de méthodes algorithmiques.</p>  
	</h3>
dans ce cas la c est le texte

Lignes 12 et 14, quelle est la particularité des balises hr et br ?

<br> permet le saut de ligne et
<hr> représente un changement thématique
entre des éléments de paragraphe (une ligne)


Détailler l’exécution des lignes 11 à 19 ?

	<h1>Ma première page web</h1> permet d afficher un texte avec une grande taille souvent utilisé pour les titres
	<br> permet de sauter des lignes
	<h2>groupe NSI</h2> permet d afficher un texte avec une taille moins grande que h1 
	<hr> permet de créer une ligne
	<h2> Lycée Polyvalent du pays d'Aunis </p>
	<h3><p style='text-align:right;color:red;font-weight:bold'>Interactions entre l’homme et la machine sur le Web </p> la balise <p> correspond a un paragraphe
	
	<p> <center>Lors de la navigation sur le Web, les internautes interagissent avec leur machine par le biais des pages Web.</center><br> 
	L’Interface Homme-Machine (IHM) repose sur la gestion d’événements associés à des 	éléments graphiques munis de méthodes algorithmiques.</p>  
	</h3> <center permet de centrer un element dans la page>

Expliquer le rôle de la commande style ?

il permet de mettre du css dans une balise html mais
 c est une mauvaise pratique il est préférable de créer un fichier css a part

Comment modifier le code afin d’aligner à gauche le texte de la ligne 15
<h2 style='text-align:right;'> Lycée Polyvalent du pays d'Aunis </p>

Exercice 2 – lien hypertexte


Expliquer les lignes 15, puis 21 ?

<h2> Lycée Polyvalent du pays d'Aunis, <a href=www.lyceedupaysdaunis.com>visitez nous</a> </p>
<p> Pour revenir à la première page, cliquer <a href=web1.html> ici</a>
les balises <a href= ‘lien’></a> la balise a permet de renvoyer sur un lien et le texte entre cette balise devient un element interragissable 
