from grille import grille
from piece import piece

def main():
    jeu = grille()
    while True:
        tour_joueur_1(jeu)
        jeu.show_game_state()
        if jeu.check_win():
            print("le joueur 1 a gagner")
            break
        tour_joueur_2(jeu)
        if jeu.check_win():
            print("le joueur 2 a gagner")

def tour_joueur_1(jeu):
    print("tour au joueur 1")
    jeu.show_game_state()
    while True:
        print("dans quel colone voulez-vous jouer?")
        col = int(input())
        if col not in range(7):
            print("réponse incorrecte. la valeur doit être de 0 à 6")
        elif not jeu.play_into_board(col, piece("x")):
            print("il n'y a pas d'espace dans cette colone")
        else:
            break

def tour_joueur_2(jeu):
    print("tour au joueur 2")
    jeu.show_game_state()
    while True:
        print("dans quel colone voulez-vous jouer?")
        col = int(input())
        if col not in range(7):
            print("réponse incorrecte. la valeur doit être de 0 à 6")
        elif not jeu.play_into_board(col, piece("o")):
            print("il n'y a pas d'espace dans cette colone")
        else:
            break
    

main()