import os


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
    
    def display_board(self):
        os.system("clear")
        print("-" * 13)
        for i in range(0, 9, 3):
            print("|", end=" ")
            print(" | ".join(self.board[i:i+3]), end="")
            print(" |")
        if i < 9:
            print("-" * 13)
    
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False
    
    def is_valid_move(self, choice): #helper function
        return (self.board[choice - 1].isdigit())
    
    def rest_board(self):
        self.board = [str(i) for i in range(1, 10)]
    
