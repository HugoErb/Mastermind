# Mastermind
Ce projet est un clone du Mastermind, un jeu de réflexion et de déduction où le but est de déterminer une combinaison secrète de couleurs en un minimum de tentatives. Ce projet inclut également un solveur basé sur l'algorithme de Knuth.

## Algorithme de Knuth
L'algorithme de Knuth est une méthode pour résoudre le jeu Mastermind en un minimum de tentatives. Il a été développé par Donald Knuth en 1977 et garantit de trouver la combinaison secrète en 5 tentatives ou moins.

L'algorithme fonctionne comme suit :

1. Initialisation : Commencer avec un ensemble de toutes les 1296 combinaisons possibles (dans le cas classique où le Mastermind utilise 6 couleurs et une combinaison de 4 pions).

1. Première Tentative : Faire une première tentative. Knuth propose de commencer avec la combinaison '1122'.

1. Élimination : Après chaque tentative, éliminer toutes les combinaisons de l'ensemble qui ne produiraient pas la même réponse que celle obtenue pour la tentative actuelle.

1. Sélection : Pour les tentatives suivantes, sélectionner la combinaison de l'ensemble actuel qui minimiserait le nombre de combinaisons restantes dans le pire des cas. Autrement dit, sélectionner la combinaison qui, pour chaque réponse possible, laisse le plus petit nombre maximum de combinaisons possibles.

1. Répéter : Répéter les étapes 3 et 4 jusqu'à ce que la combinaison correcte soit trouvée.

## Utilisation

1. Clonez ce dépôt GitHub.
1. Exécutez python main.py dans un terminal.
1. Suivez les instructions à l'écran pour entrer vos tentatives et recevoir un retour. Pour activer le solveur, rentrez '*' lors du premier tour.