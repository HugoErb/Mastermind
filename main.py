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
            still_possible_combinations = remove_useless_combinations(still_possible_combinations, user_choice, try_res[0], try_res[1])
            user_choice = define_next_combination_try(still_possible_combinations)
            print(f'Le solveur à choisi {user_choice}')
            try_res = check_colors(user_choice, secret_colors)

        print(try_res[0], ' bien placé(s)')
        print(try_res[1], ' mal placé(s)')
        nb_bien_place = try_res[0]
        nb_turns += 1
        
    if(nb_turns > nb_turns_limit):
        print('\nPartie perdu...')
        print(f'La réponse était {secret_colors}')
    else:
        print('\nPartie gagnée, bravo !')
        print(f'Nombre de tours : {nb_turns-1}')

def remove_useless_combinations(still_possible_combinations, user_choice, nb_bien_places, nb_good_colors):
    combination_to_keep = (nb_bien_places, nb_good_colors)
    still_possible_combinations[:] = [combination for combination in still_possible_combinations
                           if check_colors(user_choice, combination) == combination_to_keep]
    print(f"Nombre de combinaisons restantes : {len(still_possible_combinations)}")
    return still_possible_combinations

def check_colors(user_choice, secret_colors):
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

def define_next_combination_try(still_possible_combinations):
    score_min = float('inf')
    best_combination = None
    
    # Vérifie chaque combinaison possible
    for combination in still_possible_combinations:
        # Pour chaque combinaison possible, calcule le nombre maximum de combinaisons restantes pour chaque réponse possible
        max_restantes = 0
        for reponse in itertools.product(range(5), repeat=2):
            restantes = sum(1 for combo in still_possible_combinations if reponse == obtenir_reponse(combination, combo))
            max_restantes = max(max_restantes, restantes)
        
        # Si cette combination minimise le nombre maximum de combinaisons restantes, met à jour la meilleure combination et le score minimum
        if max_restantes < score_min:
            best_combination = combination
            score_min = max_restantes
            
    return best_combination

def obtenir_reponse(combination, combo):
    rouges = sum(g == c for g, c in zip(combination, combo))
    blancs = sum(g in combo for g in combination) - rouges
    return rouges, blancs

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
    if len(input_string) > nb_combinations:
        return False
    for char in input_string:
        if char not in string_list:
            return False
    return True

if __name__ == '__main__':
    main()
