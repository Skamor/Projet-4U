from grille import grille
from piece import piece
from history import history

def main():
    previous_games = history()
    while True:
        while True:
            print("que voulez vous faire?\n1. jouer\n2. quitter\n3. voir l'historique\nentrez un chiffre (1 à 3)")
            anwser = int(input())
            if not (anwser >= 1 or anwser <= 3):
                print("réponse invalide")
            else:
                break
        if anwser == 1:
            jeu = grille()
            while True:
                tour_joueur_1(jeu)
                jeu.show_game_state()
                if jeu.check_win():
                    print("le joueur 1 a gagner")
                    previous_games.add_game(jeu)
                    break
                tour_joueur_2(jeu)
                jeu.show_game_state()
                if jeu.check_win():
                    print("le joueur 2 a gagner")
                    previous_games.add_game(jeu)
                    break
        elif anwser == 2:
            print("bye bye")
            break
        elif anwser == 3:
            previous_games.show_game()


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