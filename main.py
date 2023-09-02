import random

colors = ["r", "b", "v", "j", "m", "o"]

def main():
    secret_colors = random.sample(colors, 4)
    print(' '.join(secret_colors))
    nb_bien_place = 0

    while nb_bien_place != 4:
        print('Quel est votre choix (r b v j m o) :')
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
        
        print(nb_bien_place, " bien placé(s)")
        print(nb_good_color , " mal placé(s)")

if __name__ == "__main__":
    main()
