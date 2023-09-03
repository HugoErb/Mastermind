import random
import itertools
import time

def main():
    still_possible_combinations = [
    ('v', 'r', 'o', 'm'), 
    ('v', 'b', 'b', 'v'), 
    ('v', 'b', 'b', 'j'), 
    ('v', 'b', 'b', 'm'), 
    ('v', 'b', 'b', 'o'), 
    ('v', 'b', 'v', 'b'), 
    ('v', 'b', 'j', 'b'), 
    ('v', 'b', 'm', 'b'), 
    ('v', 'b', 'o', 'b'), 
    ('v', 'v', 'j', 'b'), 
    ('v', 'v', 'm', 'b'), 
    ('v', 'v', 'o', 'b'), 
    ('v', 'j', 'v', 'b'), 
    ('v', 'j', 'j', 'b'), 
    ('v', 'j', 'm', 'b'), 
    ('v', 'j', 'o', 'b'), 
    ('v', 'm', 'v', 'b'), 
    ('v', 'm', 'm', 'b'), 
    ('v', 'm', 'o', 'b'), 
    ('v', 'o', 'v', 'b'), 
    ('v', 'o', 'j', 'b'), 
    ('v', 'o', 'm', 'b'), 
    ('v', 'o', 'o', 'b'), 
    ('j', 'r', 'r', 'r'), 
    ('j', 'r', 'r', 'v'), 
    ('j', 'r', 'r', 'j'), 
    ('j', 'r', 'r', 'm'), 
    ('j', 'r', 'r', 'o'), 
    ('j', 'r', 'v', 'r'), 
    ('j', 'r', 'v', 'v'), 
    ('j', 'r', 'v', 'j'), 
    ('j', 'r', 'v', 'm'), 
    ('j', 'r', 'v', 'o'), 
    ('j', 'r', 'j', 'r'), 
    ('j', 'r', 'j', 'j'), 
    ('j', 'r', 'j', 'm'), 
    ('j', 'r', 'j', 'o'), 
    ('j', 'r', 'm', 'r'), 
    ('j', 'r', 'm', 'v'), 
    ('j', 'r', 'm', 'j'), 
    ('j', 'r', 'm', 'm'), 
    ('j', 'r', 'm', 'o'), 
    ('j', 'r', 'o', 'r'), 
    ('j', 'r', 'o', 'v'), 
    ('j', 'r', 'o', 'j'), 
    ('j', 'r', 'o', 'm'), 
    ('j', 'r', 'o', 'o'), 
    ('j', 'b', 'b', 'v'), 
    ('j', 'b', 'b', 'j'), 
    ('j', 'b', 'b', 'm'), 
    ('j', 'b', 'b', 'o'), 
    ('j', 'b', 'v', 'b'), 
    ('j', 'b', 'j', 'b'), 
    ('j', 'b', 'm', 'b'), 
    ('j', 'b', 'o', 'b'), 
    ('j', 'v', 'v', 'b'), 
    ('j', 'v', 'j', 'b'), 
    ('j', 'v', 'm', 'b'), 
    ('j', 'v', 'o', 'b'), 
    ('j', 'j', 'v', 'b'), 
    ('j', 'j', 'j', 'b'), 
    ('j', 'j', 'm', 'b'), 
    ('j', 'j', 'o', 'b'), 
    ('j', 'm', 'v', 'b'), 
    ('j', 'm', 'j', 'b'), 
    ('j', 'm', 'm', 'b'), 
    ('j', 'm', 'o', 'b'), 
    ('j', 'o', 'v', 'b'), 
    ('j', 'o', 'j', 'b'), 
    ('j', 'o', 'm', 'b'), 
    ('j', 'o', 'o', 'b'), 
    ('m', 'r', 'r', 'r'), 
    ('m', 'r', 'r', 'v'), 
    ('m', 'r', 'r', 'j'), 
    ('m', 'r', 'r', 'm'), 
    ('m', 'r', 'r', 'o'), 
    ('m', 'r', 'v', 'r'), 
    ('m', 'r', 'v', 'v'), 
    ('m', 'r', 'v', 'j'), 
    ('m', 'r', 'v', 'o'), 
    ('m', 'r', 'j', 'r'), 
    ('m', 'r', 'j', 'v'), 
    ('m', 'r', 'j', 'j'), 
    ('m', 'r', 'j', 'm'), 
    ('m', 'r', 'j', 'o'), 
    ('m', 'r', 'm', 'r'), 
    ('m', 'r', 'm', 'v'), 
    ('m', 'r', 'm', 'j'), 
    ('m', 'r', 'm', 'm'), 
    ('m', 'r', 'm', 'o'), 
    ('m', 'r', 'o', 'r'), 
    ('m', 'r', 'o', 'v'), 
    ('m', 'r', 'o', 'j'), 
    ('m', 'r', 'o', 'm'), 
    ('m', 'r', 'o', 'o'), 
    ('m', 'b', 'b', 'v'), 
    ('m', 'b', 'b', 'j'), 
    ('m', 'b', 'b', 'm'), 
    ('m', 'b', 'b', 'o'), 
    ('m', 'b', 'v', 'b'), 
    ('m', 'b', 'j', 'b'), 
    ('m', 'b', 'm', 'b'), 
    ('m', 'b', 'o', 'b'), 
    ('m', 'v', 'v', 'b'), 
    ('m', 'v', 'j', 'b'), 
    ('m', 'v', 'm', 'b'), 
    ('m', 'v', 'o', 'b'), 
    ('m', 'j', 'j', 'b'), 
    ('m', 'j', 'm', 'b'), 
    ('m', 'j', 'o', 'b'), 
    ('m', 'm', 'v', 'b'), 
    ('m', 'm', 'j', 'b'), 
    ('m', 'm', 'm', 'b'), 
    ('m', 'm', 'o', 'b'), 
    ('m', 'o', 'v', 'b'), 
    ('m', 'o', 'j', 'b'), 
    ('m', 'o', 'm', 'b'), 
    ('m', 'o', 'o', 'b'), 
    ('o', 'r', 'r', 'r'), 
    ('o', 'r', 'r', 'v'), 
    ('o', 'r', 'r', 'j'), 
    ('o', 'r', 'r', 'm'), 
    ('o', 'r', 'r', 'o'), 
    ('o', 'r', 'v', 'v'), 
    ('o', 'r', 'v', 'j'), 
    ('o', 'r', 'v', 'm'), 
    ('o', 'r', 'v', 'o'), 
    ('o', 'r', 'j', 'r'), 
    ('o', 'r', 'j', 'v'), 
    ('o', 'r', 'j', 'j'), 
    ('o', 'r', 'j', 'm'), 
    ('o', 'r', 'm', 'r'), 
    ('o', 'r', 'm', 'v'), 
    ('o', 'r', 'm', 'j'), 
    ('o', 'r', 'm', 'm'), 
    ('o', 'r', 'm', 'o'), 
    ('o', 'r', 'o', 'r'), 
    ('o', 'r', 'o', 'v'), 
    ('o', 'r', 'o', 'j'), 
    ('o', 'r', 'o', 'm'), 
    ('o', 'r', 'o', 'o'), 
    ('o', 'b', 'b', 'v'), 
    ('o', 'b', 'b', 'j'), 
    ('o', 'b', 'b', 'm'), 
    ('o', 'b', 'b', 'o'), 
    ('o', 'b', 'v', 'b'), 
    ('o', 'b', 'j', 'b'), 
    ('o', 'b', 'm', 'b'), 
    ('o', 'b', 'o', 'b'), 
    ('o', 'v', 'v', 'b'), 
    ('o', 'v', 'j', 'b'), 
    ('o', 'v', 'm', 'b'), 
    ('o', 'v', 'o', 'b'), 
    ('o', 'j', 'v', 'b'), 
    ('o', 'j', 'j', 'b'), 
    ('o', 'j', 'm', 'b'), 
    ('o', 'j', 'o', 'b'), 
    ('o', 'm', 'v', 'b'), 
    ('o', 'm', 'm', 'b'), 
    ('o', 'm', 'o', 'b'), 
    ('o', 'o', 'v', 'b'), 
    ('o', 'o', 'j', 'b'), 
    ('o', 'o', 'm', 'b'), 
    ('o', 'o', 'o', 'b')
]
    start_time = time.time()
    define_next_combination_try(still_possible_combinations)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Le programme 1 a été exécuté en : {execution_time} secondes")

    start_time = time.time()
    define_next_combination_try_2(still_possible_combinations)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Le programme 2 a été exécuté en : {execution_time} secondes")

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
    
    # On Créé un dictionnaire pour stocker le nombre de combinaisons qui donneraient chaque réponse possible
    possible_responses = {response: 0 for response in itertools.product(range(5), repeat=2)}
    print(possible_responses)
    
    # Pour chaque combinaison possible, on calcule le nombre de combinaisons qui donneraient chaque réponse possible
    for combination in still_possible_combinations:
        for combo in still_possible_combinations:
            response = check_colors(combination, combo)
            possible_responses[response] += 1
    
        # Trouver le maximum des combinaisons restantes pour chaque réponse possible
        max_restantes = max(possible_responses.values())
        
        # Réinitialiser les réponses pour la prochaine itération
        for response in possible_responses:
            possible_responses[response] = 0
        
        # Si cette combinaison minimise le nombre maximum de combinaisons restantes, alors on considère que c'est pour l'instant la meilleure combinaison à tester
        if max_restantes < score_min:
            best_combination = combination
            score_min = max_restantes
            
    return best_combination

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

def define_next_combination_try_2(still_possible_combinations: list) -> list:
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

if __name__ == '__main__':
    main()