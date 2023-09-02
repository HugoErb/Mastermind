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
            user_choice = input()
            if nb_turns == 1 and user_choice == '*':
                print('Activation du solveur')
                solver_activated = True
                # On créé une liste contenant toutes les combinaisons possibles
                all_combinations = list(itertools.product(colors, repeat=nb_combinations))
                user_choice = ['r','r','b','b']
                print(f'Le solveur à choisi {user_choice}')
                try_res = check_colors(user_choice, nb_combinations, secret_colors)
            else:
                if (user_choice == '*'):
                    print('L\'activation du solveur n\'est possible que durant le premier tour.')
                while not check_string_composition(user_choice, colors, nb_combinations):
                    print('Veuillez rentrer une suite de couleurs autorisées (r b v j m o) :')
                    user_choice = input()
                try_res = check_colors(user_choice, nb_combinations, secret_colors)
        else:
            all_combinations = remove_useless_combinations(all_combinations, try_res[0], try_res[1], nb_combinations, user_choice)
            user_choice = define_next_combination_try(all_combinations)
            print(f'Le solveur à choisi {user_choice}')
            try_res = check_colors(user_choice, nb_combinations, secret_colors)

        print(try_res[0], ' bien placé(s)')
        print(try_res[1], ' mal placé(s)')
        nb_bien_place = try_res[0]
        nb_turns += 1
        
    if(nb_turns > nb_turns_limit):
        print('\nPartie perdu...')
        print(f'La réponse était {secret_colors}')
    else:
        print('\nPartie gagnée, bravo !')
        print(f'Nombre de tours : {nb_turns}')

def remove_useless_combinations(all_combinations: list, nb_bien_places: int, nb_good_colors: int, nb_combinations: int, user_choice: list) -> list:
    for combination in all_combinations:
        if check_colors(combination, nb_combinations, user_choice) != [nb_bien_places, nb_good_colors]:
            all_combinations.remove(combination)
    print(f"Nombre de combinaisons restantes : {len(all_combinations)}")
    return all_combinations
    
def check_colors(user_choice: list, nb_combinations: int, secret_colors: list) -> tuple:
    nb_bien_place = 0
    nb_good_color = 0
    tmp_list = list(secret_colors).copy()
    for i in range(nb_combinations):
            # Check du nombre de couleurs bien placées
            if user_choice[i] == tmp_list[i]:
                nb_bien_place += 1
                tmp_list[i] = None

            # Check du nombre de couleurs présentes mais mal placées
            elif user_choice[i] in tmp_list:
                nb_good_color += 1
        
    return [nb_bien_place, nb_good_color]

def define_next_combination_try(all_combinations):
    # Initialise le score minimum à une valeur élevée
    score_min = float('inf')
    best_combination = None
    
    # Vérifie chaque combinaison possible
    for combination in all_combinations:
        # Pour chaque combinaison possible, calcule le nombre maximum de combinaisons restantes pour chaque réponse possible
        max_restantes = 0
        for reponse in itertools.product(range(5), repeat=2): # réponses de (0, 0) à (4, 4)
            restantes = sum(1 for combo in all_combinations if reponse == obtenir_reponse(combination, combo))
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

def check_string_composition(input_string, string_list, nb_combinations) -> bool:
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
