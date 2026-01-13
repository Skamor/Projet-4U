class history:
    def __init__(self):
        self.games = []
    
    def show_game(self):
        if len(self.games) <= 0:
            print("aucun jeu passé a regarder")
        else:
            while True:
                print("choisissez un jeu à regarder")
                print("il y a", len(self.games), "jeux", 0, "est le premier et", len(self.games)-1, "est le dernier")
                choice = int(input())
                if choice >=0 and choice<= len(self.games):
                    self.games[choice].show_game_state()
                    break
                else:
                    print("option invalide")
    def add_game(self, game):
        self.games.append(game)
                
