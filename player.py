class Player:
    
    def __init__(self):
        self.name = ''
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha() == True:
                self.name = name.strip()
                break
            print("Invalide name, please letters only: ")
    def choose_symbole(self):
        while True:
            symbole = input(f"{self.name}, choose your symbol (a single letter): ")
            if symbole.isalpha() and len(symbole) == 1:
                self.symbol = symbole.strip().upper()
                break
            print("Invalide symbol, please a single letters only: ")
