
class Menu:
    def display_main_menu(self):
        print("Welcom to my X-O game!")
        print("1, Start Game")
        print("2, Quit Game")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice not in ["1", "2"]:
                print("Invalide choice.")
            else:
                return choice
    
    def display_endgame_menu(self):
        menu_text = """
        Game Over!
        1, Restart Game
        2, Quit Game
        Enter your choice (1 or 2): """
        while True:
            choice = input(menu_text)
            if choice not in ["1", "2"]:
                print("Invalide choice.")
            else:
                return choice
        return choice

