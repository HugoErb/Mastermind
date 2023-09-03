import random
import itertools

colors = ['r', 'b', 'v', 'j', 'm', 'o']
nb_combinations = 4
nb_turns_limit = 8

def main():
    secret_colors = random.sample(colors, nb_combinations)
    print(' '.join(secret_colors))
    nb_bien_place = 0
    nb_turns = 1
    solver_activated = False

    while nb_bien_place != nb_combinations and nb_turns <= nb_turns_limit:
        print(f'\nTour n° {nb_turns}')
        if not solver_activated:
            print('Quel est votre choix (r b v j m o) :')
            user_choice = list(input())
            if nb_turns == 1 and user_choice == ['*']:
                print('Activation du solveur')
                solver_activated = True
                # On créé une liste contenant toutes les combinaisons possibles
                still_possible_combinations = list(itertools.product(colors, repeat=nb_combinations))
                user_choice = ['r','r','b','b']
                print(f'Le solveur à choisi {user_choice}')
                try_res = check_colors(user_choice, secret_colors)
            else:
                if (user_choice == ['*']):
                    print('L\'activation du solveur n\'est possible que durant le premier tour.')
                while not check_string_composition(user_choice, colors, nb_combinations):
                    print('Veuillez rentrer une suite de couleurs autorisées (r b v j m o) :')
                    user_choice = list(input())
                try_res = check_colors(user_choice, secret_colors)
        else:
            still_possible_combinations = remove_impossible_combinations(still_possible_combinations, user_choice, try_res[0], try_res[1])
            user_choice = define_next_combination_try(still_possible_combinations)
            print(f'Le solveur à choisi {user_choice}')
            try_res = check_colors(user_choice, secret_colors)

        nb_bien_place = try_res[0]
        print(nb_bien_place, ' bien placé(s)')
        print(try_res[1], ' mal placé(s)')
        nb_turns += 1
        
    if(nb_turns > nb_turns_limit):
        print('\nPartie perdu...')
        print(f'La réponse était {secret_colors}')
    else:
        print('\nPartie gagnée, bravo !')
        print(f'Nombre de tours : {nb_turns-1}')

def remove_impossible_combinations(still_possible_combinations, user_choice, nb_bien_places, nb_good_colors):
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
    tmp_list = list(secret_colors)
    for i in range(len(user_choice)):
        if user_choice[i] == tmp_list[i]:
            nb_bien_place += 1
            tmp_list[i] = None
        elif user_choice[i] in tmp_list:
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
    possible_responses_tmp = possible_responses
    
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
        possible_responses_tmp = possible_responses
            
    return best_combination

def check_string_composition(input_string: str, string_list: list, nb_combinations: int) -> bool:
    '''
    Vérifie si la chaîne de caractères est composée uniquement de chaînes présentes dans la liste donnée.

    Args:
        input_string (str): La chaîne à vérifier.
        string_list (list): Liste de chaînes de caractères à comparer.
        nb_combinations (int): Nombre de couleurs par combinaisons.

    Returns:
        bool: True si la chaîne est composée uniquement de caractères de la liste, False sinon.
    '''
    # On vérifie la bonne taille de input_string et si chaque caractère de input_string est bien dans string_list.
    return len(input_string) <= nb_combinations and all(char in string_list for char in input_string)


if __name__ == '__main__':
    main()
