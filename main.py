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
        print('Quel est votre choix (r b v j m o) :')
        user_choice = input()
        if nb_turns == 1 and not solver_activated and user_choice == '*':
            print('Activation du solveur')
            solver_activated = True
            # On créé une liste contenant toutes les combinaisons possibles
            all_combinations = list(itertools.product(colors, repeat=nb_combinations))
        else:
            if (user_choice == '*'):
                print('L\'activation du solveur n\'est possible que durant le premier tour.')
            while not check_string_composition(user_choice, colors):
                print('Veuillez rentrer une suite de couleurs autorisées (r b v j m o) :')
                user_choice = input()
        tmp_list = secret_colors.copy()
        nb_bien_place = 0
        nb_good_color = 0
        
        for i in range(nb_combinations):
            # Check du nombre de couleurs bien placées
            if user_choice[i] == tmp_list[i]:
                nb_bien_place += 1
                tmp_list[i] = None

            # Check du nombre de couleurs présentes mais mal placées
            elif user_choice[i] in tmp_list:
                nb_good_color += 1
        
        print(nb_bien_place, ' bien placé(s)')
        print(nb_good_color , ' mal placé(s)')
        nb_turns += 1
        
    if(nb_turns > nb_turns_limit):
        print('\nPartie perdu...')
        print(f'La réponse était {secret_colors}')
    else:
        print('\nPartie gagnée, bravo !')
        print(f'Nombre de tours : {nb_turns}')

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
