class piece:
    def __init__(self, symbole):
        self.symbole = symbole
    def __eq__(self, other):
        if self.symbole == other:
            return True
        
    def __repr__(self):
        return self.symbole