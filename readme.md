# Mastermind

Clone du jeu Mastermind en Python. Le but est de deviner une combinaison secrète de 4 couleurs en 8 tentatives maximum. Le projet inclut également un solveur automatique basé sur l'algorithme de Knuth.

## Comment jouer

### Lancement

```bash
python main.py
```

### Couleurs disponibles

| Code | Couleur  |
|------|----------|
| `r`  | Rouge    |
| `b`  | Bleu     |
| `v`  | Vert     |
| `j`  | Jaune    |
| `m`  | Magenta  |
| `o`  | Orange   |

### Saisie d'une tentative

À chaque tour, tapez **4 lettres sans espace** correspondant aux couleurs de votre choix, puis appuyez sur Entrée.

Exemple : `rbjm` pour Rouge, Bleu, Jaune, Magenta.

> Les doublons sont autorisés (ex: `rrbj`).

### Interprétation des indices

Après chaque tentative, le jeu affiche deux nombres :

- **Bien placé(s)** : nombre de couleurs correctes à la bonne position.
- **Mal placé(s)** : nombre de couleurs présentes dans la combinaison secrète mais à une mauvaise position.

Exemple : si le secret est `r b v j` et que vous jouez `r v m j` :
- `r` → bien placé
- `v` → mal placé (présente mais pas en position 2)
- `m` → absent
- `j` → bien placé

Résultat : **2 bien placé(s), 1 mal placé(s)**

### Conditions de victoire / défaite

- **Victoire** : vous trouvez la combinaison exacte (4 bien placés).
- **Défaite** : vous n'avez pas trouvé en 8 tours. La combinaison secrète est alors révélée.

### Activer le solveur automatique

Au **premier tour uniquement**, tapez `*` pour activer le solveur. Celui-ci jouera automatiquement jusqu'à trouver la solution en utilisant l'algorithme de Knuth.

---

## Algorithme de Knuth

L'algorithme de Knuth (1977) garantit de trouver n'importe quelle combinaison en **5 tentatives ou moins** (sur 1296 combinaisons possibles).

Son fonctionnement :

1. **Initialisation** : partir de l'ensemble des 1296 combinaisons possibles (6 couleurs, 4 positions).
2. **Première tentative** : jouer `rrbb` (combinaison de départ efficace).
3. **Élimination** : après chaque réponse, supprimer de l'ensemble toutes les combinaisons qui n'auraient pas produit le même résultat.
4. **Sélection** : choisir la combinaison qui, dans le pire des cas, élimine le plus grand nombre de candidats restants (minimax).
5. **Répéter** les étapes 3 et 4 jusqu'à trouver la solution.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/HugoErb/Mastermind.git
   cd Mastermind
   ```
2. Lancez le jeu (Python 3.9+ requis, aucune dépendance externe) :
   ```bash
   python main.py
   ```
