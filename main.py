from player import Player
from menu import Menu
from board import Board

# to clear screan when u get 1st info:
import os

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
    
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()
    
    
    def setup_player(self):
        player_symbol = []
        for index, player in enumerate(self.players, start=1):
            print(f"Player {index}, enter your details: ")
            player.choose_name()
            if index == 1:
                player.choose_symbole()
            elif index == 2:
                while True:
                    print(f"dont use the symbol '{self.players[0].symbol}' of player '{self.players[0].name}' ")
                    player.choose_symbole()
                    if self.players[0].symbol != self.players[1].symbol:
                        break
            os.system("clear")
        
    
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    
    def restart_game(self):
        self.board.rest_board()
        self.current_player_index = 0
        self.play_game()
    
    
    def check_win(self):
        win_combination = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],    #rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],    #colums
            [0, 4, 8], [2, 4, 6]                #diagonals
        ]
    
        for combo in win_combination:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                for player in self.players:
                    if player.symbol == self.board.board[combo[0]]:
                        self.board.display_board()
                        print(f"{player.name} is win")
                return True
            return False
    
    def check_draw(self):
        if all(not cell.isdigit() for cell in self.board.board):
            self.board.display_board()
            print("No one win")
            return True
        return False
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn {player.symbol}")
        while True:
            try:
                cell_choice = int(input("Chose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalide move, try again.")
            except ValueError:
                print("Pease enter a number between 1 and 9")
        self.switch_player()
        
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    def quit_game(self):
        print("Thank you for playing")

game = Game()

game.start_game()