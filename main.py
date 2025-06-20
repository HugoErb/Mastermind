import random
import itertools

COLORS = ['r', 'b', 'v', 'j', 'm', 'o']
NB_COMBINATIONS = 4
NB_TURNS_LIMIT = 8

def main():
    secret_colors = random.sample(COLORS, NB_COMBINATIONS)
    print(' '.join(secret_colors))

    nb_turns = game(secret_colors)

    print_end_game_infos(nb_turns, NB_TURNS_LIMIT, secret_colors)

def game(secret_colors: list) -> int:
    nb_bien_place = 0
    nb_turns = 0
    solver_activated = False
    still_possible_combinations = []
    try_res = None

    while nb_bien_place != NB_COMBINATIONS and nb_turns <= NB_TURNS_LIMIT:
        nb_turns += 1
        print(f'\nTour n° {nb_turns}')
        if not solver_activated:
            user_choice, solver_activated = get_user_choice(nb_turns, COLORS, NB_COMBINATIONS)
            if solver_activated:
                still_possible_combinations, user_choice = solver_processing(None, None, None, COLORS, NB_COMBINATIONS)
        else:
            still_possible_combinations, user_choice = solver_processing(still_possible_combinations, user_choice, try_res, COLORS, NB_COMBINATIONS)

        try_res = check_colors(user_choice, secret_colors)
        nb_bien_place = try_res[0]
        print(nb_bien_place, ' bien placé(s)')
        print(try_res[1], ' mal placé(s)')
    return nb_turns
        
def print_end_game_infos(nb_turns: int, NB_TURNS_LIMIT: int, secret_colors: list):
    """
    Affiche les informations de fin de partie, indiquant si l'utilisateur a gagné ou perdu, et, le cas échéant, affiche les couleurs secrètes.

    Args:
    nb_turns (int): Le nombre de tours joués.
    NB_TURNS_LIMIT (int): Le nombre maximum de tours autorisés.
    secret_colors (list): Liste des couleurs secrètes.

    Notes:
    Si le nombre de tours joués est supérieur à la limite de tours, affiche un message indiquant que la partie est perdue et affiche les couleurs recherchées.
    Sinon, la fonction affiche un message de félicitations pour avoir gagné la partie et affiche le nombre de tours joués.
    """
    if(nb_turns > NB_TURNS_LIMIT):
        print('\nPartie perdue...')
        print(f'La réponse était {secret_colors}')
    else:
        print('\nPartie gagnée, bravo !')
        print(f'Nombre de tours : {nb_turns}')
        exit()

def get_user_choice(nb_turns: int, COLORS: list, NB_COMBINATIONS: int) -> tuple:
    """
    Demande à l'utilisateur de choisir une combinaison de couleurs ou d'activer le solveur.

    Args:
    nb_turns (int): Le numéro du tour en cours.
    COLORS (list): Liste des couleurs autorisées (par exemple, ['r', 'b', 'v', 'j', 'm', 'o']).
    NB_COMBINATIONS (int): Nombre de couleurs par combinaison.

    Returns:
    tuple: Un tuple contenant deux éléments :
      - user_choice (list): La liste des couleurs choisies par l'utilisateur.
      - bool: True si l'utilisateur a choisi d'activer le solveur, False sinon.
    """
    user_choice = list(input('Quel est votre choix (r b v j m o) :'))
    if user_choice == ['*']:
        if nb_turns == 1:
            print('Activation du solveur')
            return None, True  # Activation du solveur
        else:
            print('L\'activation du solveur n\'est possible que durant le premier tour.')
    while not check_string_composition(user_choice, COLORS, NB_COMBINATIONS):
        user_choice = list(input(f'Veuillez rentrer une suite de {NB_COMBINATIONS} couleurs autorisées (r b v j m o) :'))
    return user_choice, False

def solver_processing(still_possible_combinations: list, user_choice: list, try_res: tuple, COLORS: list, NB_COMBINATIONS: int) -> tuple:
    """
    Gère le traitement du solveur pour trouver la prochaine combinaison à essayer.

    Si 'try_res' est None, cela signifie que c'est la première fois que le solveur est activé, 
    et il initialise 'still_possible_combinations' à toutes les combinaisons possibles 
    et définit 'user_choice' à une combinaison arbitraire.

    Si 'try_res' n'est pas None, cela signifie que le solveur a déjà été activé, et il 
    élimine les combinaisons impossibles de 'still_possible_combinations' et définit 
    'user_choice' à la prochaine combinaison à essayer.

    Args:
    still_possible_combinations (list): Liste des combinaisons possibles restantes.
    user_choice (list): Dernière combinaison de couleurs choisie par l'utilisateur ou par le solveur.
    try_res (tuple): Résultat du dernier essai (nb_bien_place, nb_mal_place) ou None si c'est le premier essai.
    COLORS (list): Liste des couleurs autorisées.
    NB_COMBINATIONS (int): Nombre de couleurs par combinaison.

    Returns:
    tuple: Un tuple contenant deux éléments :
      - still_possible_combinations (list): Liste mise à jour des combinaisons possibles restantes.
      - user_choice (list): La prochaine combinaison de couleurs que le solveur souhaite essayer.
    """
    if try_res is None:
        still_possible_combinations = list(itertools.product(COLORS, repeat=NB_COMBINATIONS))
        user_choice = ['r','r','b','b']
    else:
        still_possible_combinations = remove_impossible_combinations(still_possible_combinations, user_choice, try_res[0], try_res[1])
        user_choice = define_next_combination_try(still_possible_combinations)
    print(f'Le solveur à choisi {user_choice}')
    return still_possible_combinations, user_choice

def remove_impossible_combinations(still_possible_combinations: list, user_choice:list, nb_bien_places:int, nb_good_colors:int) -> list:
    """
    Supprime les combinaisons impossibles de la liste des combinaisons encore possibles en fonction du choix de l'utilisateur et du résultat de ce choix.

    Args:
    still_possible_combinations (list): Liste des combinaisons encore possibles.
    user_choice (list): Liste des couleurs choisies par l'utilisateur.
    nb_bien_places (int): Nombre de couleurs bien placées dans le choix de l'utilisateur.
    nb_good_colors (int): Nombre de bonnes couleurs mal placées dans le choix de l'utilisateur.

    Returns:
    list: Liste mise à jour des combinaisons encore possibles après suppression des combinaisons impossibles.
    """
    combination_to_keep = (nb_bien_places, nb_good_colors)
    still_possible_combinations[:] = [combination for combination in still_possible_combinations
                           if check_colors(user_choice, combination) == combination_to_keep]
    return still_possible_combinations

def check_colors(user_choice: list, secret_colors: list) -> tuple:
    """
    Compare la sélection de couleurs de l'utilisateur avec les couleurs secrètes pour déterminer le nombre de couleurs bien placées et le nombre de bonnes couleurs mal placées.

    Args:
    user_choice (list): Liste des couleurs choisies par l'utilisateur.
    secret_colors (list): Liste des couleurs secrètes.

    Returns:
    tuple: Un tuple contenant deux éléments :
      - nb_bien_place (int): Le nombre de couleurs de la sélection de l'utilisateur qui sont identiques et à la même position que dans les couleurs secrètes.
      - nb_good_color (int): Le nombre de couleurs de la sélection de l'utilisateur qui sont présentes dans les couleurs secrètes mais qui ne sont pas à la bonne position.
    """
    nb_bien_place = 0
    nb_good_color = 0
    for i in range(len(user_choice)):
        if user_choice[i] == secret_colors[i]:
            nb_bien_place += 1
        elif user_choice[i] in secret_colors:
            nb_good_color += 1
    return nb_bien_place, nb_good_color

def define_next_combination_try(still_possible_combinations: list) -> list:
    """
    Détermine la meilleure combinaison à essayer ensuite en minimisant le pire des cas du nombre de combinaisons restantes possibles.

    Args:
    still_possible_combinations (list): Liste des combinaisons possibles restantes.

    Returns:
    list: La meilleure combinaison à essayer ensuite.
    """
    score_min = float('inf')
    best_combination = None
    
    # On créé un dictionnaire pour stocker le nombre de combinaisons qui donneraient chaque réponse possible
    possible_responses = {response: 0 for response in itertools.product(range(5), repeat=2)}
    possible_responses_tmp = possible_responses.copy()
    
    # Pour chaque combinaison possible, on calcule le nombre de combinaisons qui donneraient chaque réponse possible
    for combination in still_possible_combinations:
        for combination2 in still_possible_combinations:
            response = check_colors(combination, combination2)
            possible_responses_tmp[response] += 1
    
        # Trouver le maximum des combinaisons restantes pour chaque réponse possible
        max_restantes = max(possible_responses_tmp.values())

        # Si cette combinaison minimise le nombre maximum de combinaisons restantes, alors on considère que c'est pour l'instant la meilleure combinaison à tester
        if max_restantes < score_min:
            best_combination = combination
            score_min = max_restantes
        
        # Réinitialisation des réponses pour la prochaine itération
        possible_responses_tmp = possible_responses.copy()
            
    return best_combination

def check_string_composition(input_string: str, string_list: list, NB_COMBINATIONS: int) -> bool:
    '''
    Vérifie si la chaîne de caractères est composée uniquement de n caractères présents dans la liste donnée.

    Args:
        input_string (str): La chaîne à vérifier.
        string_list (list): Liste de chaînes de caractères à comparer.
        NB_COMBINATIONS (int): Nombre de couleurs par combinaisons.

    Returns:
        bool: True si la chaîne est composée uniquement de caractères de la liste, False sinon.
    '''
    # On vérifie la bonne taille de input_string et si chaque caractère de input_string est bien dans string_list.
    return len(input_string) <= NB_COMBINATIONS and all(char in string_list for char in input_string)


if __name__ == '__main__':
    main()
