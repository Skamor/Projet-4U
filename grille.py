from piece import piece

class grille:
    def __init__(self):
        self.grille = []
        for i in range(6):
            temp = []
            for j in range(7):
                temp.append("#")
            self.grille.append(temp)
    
    def show_game_state(self):
        for i in range(7):
            print(i, end=" ")
        print()
        for i in self.grille:
            for j in i:
                print(j, end=" ")
            print()
    
    def check_available(self, col):
        i = 5
        while i >= 0:
            if self.grille[i][col] == "#":
                return i
            else:
                i-=1
        return -1
    
    def play_into_board(self, col, piece):
        row = self.check_available(col)
        if row == -1:
            return False
        self.grille[row][col] = piece
        return True
    
    def check_win(self):
        win = False
        for i in range(len(self.grille)):
            win = self.check_row(i)
            if win:
                print("vous avez gagner")
                break
        for i in range(len(self.grille[0])):
            win = self.check_col(i)
            if win:
                print("vous avez gagner")
                break
        lines = (((3,0), (2,1), (1,2), (0,3)), 
                 ((4,0), (3,1), (2,2), (1,3), (0,4)), 
                 ((5,0), (4,1), (3,2), (2,3), (1,4), (0,5)), 
                 ((5,1), (4,2), (3,3), (2,4), (1,5), (0,6)), 
                 ((5,2), (4,3), (3,4), (2,5), (1,6)), 
                 ((5,3), (4,4), (3,5), (2,6)),
                 ((2,0), (3,1), (4,2), (5,3)),
                 ((1,0), (2,1), (3,2), (4,3), (5,4)),
                 ((0,0), (1,1), (2,2), (3,3), (4,4), (5,5)),
                 ((0,1), (1,2), (2,3), (3,4), (4,5), (5,6)),
                 ((0,2), (1,3), (2,4), (3,5), (4,6)),
                 ((0,3), (1,4), (2,5), (3,6)))
        for i in lines:
            win = self.check_diag(i)
            if win:
                print("vous avez gagner")
                break


    def check_row(self, row):
        temp = []
        for i in self.grille[row]:
            temp.append(i)
        return self.check_4(temp)
    
    def check_col(self, col):
        temp = []
        for i in range(len(self.grille)):
            temp.append(self.grille[i][col])
        return self.check_4(temp)

    def check_diag(self, line):
        temp = []
        for coord in line:
            temp.append(self.grille[coord[0]][coord[1]])
        return self.check_4(temp)
    
    def check_4(self, temp):
        occurences = 1
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1] and isinstance(temp[i], piece) and isinstance(temp[i+1], piece):
                occurences +=1
            else:
                occurences = 1
            if occurences == 4:
                return True


        