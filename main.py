import random

colors = ['r', 'b', 'v', 'j', 'm', 'o']

def main():
    secret_colors = random.sample(colors, 4)
    print(' '.join(secret_colors))
    nb_bien_place = 0
    nb_turns = 1

    while nb_bien_place != 4 and nb_turns <= 8:
        print(f'\nTour n° {nb_turns}')
        print('Quel est votre choix (r b v j m o) :')
        user_choice = input()
        while check_string_composition(user_choice, colors) is False:
            print('Veuillez rentrer une suite de couleurs autorisées (r b v j m o) :')
            user_choice = input()
        tmp_list = secret_colors.copy()
        nb_bien_place = 0
        nb_good_color = 0
        
        for i in range(4):
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
        
    if(nb_turns > 8):
        print('\nPartie perdu...')
        print(f'La réponse était {secret_colors}')
    else:
        print('\nPartie gagnée, bravo !')
        print(f'Nombre de tours : {nb_turns}')

def check_string_composition(input_string, string_list):
    '''
    Vérifie si la chaîne de caractères est composée uniquement de chaînes présentes dans la liste donnée.

    Args:
        input_string (str): La chaîne à vérifier.
        string_list (list): Liste de chaînes de caractères à comparer.

    Returns:
        bool: True si la chaîne est composée uniquement de caractères de la liste, False sinon.
    '''
    if len(input_string) > 4:
        return False
    for char in input_string:
        if char not in string_list:
            return False
    return True

if __name__ == '__main__':
    main()
