Mastermind Solver
Introduction
Mastermind est un jeu de réflexion et de déduction créé par Mordecai Meirowitz dans les années 1970. Le but du jeu est de déterminer une combinaison secrète de couleurs en un minimum de tentatives.

Le jeu se joue généralement avec une combinaison de 4 pions, chacun pouvant être de l'une des 6 couleurs différentes. Le joueur qui tente de deviner la combinaison fait une série de tentatives. Après chaque tentative, il reçoit un feedback sous forme de pions noirs et blancs. Un pion noir signifie qu'un pion de la tentative est de la bonne couleur et est placé à la bonne position. Un pion blanc signifie qu'un pion de la tentative est de la bonne couleur mais n'est pas placé à la bonne position.

Algorithme de Knuth
L'algorithme de Knuth est une méthode pour résoudre le jeu Mastermind en un minimum de tentatives. Il a été développé par Donald Knuth en 1977 et garantit de trouver la combinaison secrète en 5 tentatives ou moins.

L'algorithme fonctionne comme suit :

Initialisation : Commencer avec un ensemble de toutes les 1296 combinaisons possibles (dans le cas classique où le Mastermind utilise 6 couleurs et une combinaison de 4 pions).

Première Tentative : Faire une première tentative. Knuth propose de commencer avec la combinaison '1122'.

Élimination : Après chaque tentative, éliminer toutes les combinaisons de l'ensemble qui ne produiraient pas la même réponse que celle obtenue pour la tentative actuelle.

Sélection : Pour les tentatives suivantes, sélectionner la combinaison de l'ensemble actuel qui minimiserait le nombre de combinaisons restantes dans le pire des cas. Autrement dit, sélectionner la combinaison qui, pour chaque réponse possible, laisse le plus petit nombre maximum de combinaisons possibles.

Répéter : Répéter les étapes 3 et 4 jusqu'à ce que la combinaison correcte soit trouvée.

Utilisation
[Incluez ici les instructions pour utiliser votre code, par exemple :]

Clonez ce dépôt GitHub.
Exécutez python mastermind.py dans un terminal.
Suivez les instructions à l'écran pour entrer vos tentatives et recevoir le feedback.