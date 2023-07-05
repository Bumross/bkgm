from file_loader import FileLoader
from graphics import Graphics
from dice import Dice

class Game():


    def __init__(self):
        self._fl = FileLoader("data.json")
        self._game_over = False
        self._ai = False
        self._player_on_turn = 0
        self._dfl = FileLoader("default.json")
        self._ai_color = None
        self._highlihted = 0
        self._diceroll = None


    def start(self):
        #starting the game, loop for game until the game is over
        self._board = self.init_board()
        self.play_vs_ai_prompt()

        print("Enter the position of checker of column number (for example 13 or 2)")
        while not self._game_over:
            self.draw()
            self.update()

        print("Player with" + ("cross" if self.player_on_turn== 0 else "rounds") + "wins!")


    def draw(self):
        Graphics.draw(self._board, self._highlihted)


    def init_board(self):
        while True:
            load_from_json = input("0 -> start new game | 1 -> load game: ")
            if load_from_json =="0" or load_from_json == "1":
                break

        if load_from_json:
            try:
                return self.load_columns_from_json()
            except FileNotFoundError:
                print("File not found :(")
                return self.load_default_board()
            except Exception as e:
                print(e)
                print("Loading the base structure")
                return self.load_default_board()
        
        else:
            return self.load_default_board()


    def load_columns_from_json(self):
        columns = self._fl.load_game()
        return columns


    def load_default_columns(self):
        columns = self._dfl.load_game()
        return columns



    def update(self):
        if not self._ai:
            print("Player with " + ("cross" if self._player_on_turn == 0 else "rounds") + " is on turn!")
        else:
            print("You are on turn!")

        #add the alert of checkers on bar / finished checkers

        self._diceroll = Dice.dice_values()
        print(f"The dice numbers are: {self._diceroll[0], self._diceroll[1]}")

        if self._ai == 2 or (self._ai ==1 and self._player_on_turn == self._ai_color):
            self.require_ai_to_highlight_figure()
        else:
            self.require_player_to_highlight_figure()

        self.draw()

        if self._ai == 2 or (self._ai == 1 and self._player_on_turn == self._ai_color):
            self.require_ai_to_move()
        else:
            self.require_player_to_move()



    def require_player_to_highlight_figure(self):
        while True:
            column = int(input("Choose your checker to move: "))

            if not 0 < column < 25:
                print("Number of column is not valid")
                continue
            
            self._highlihted = column
            return



    def play_vs_ai_prompt(self):
        #setting the game, choosing playstyle and color
        while True:
            try:
                self._ai = int(input("0 -> two players game | 1 -> game against AI | 2 -> AI vs AI: "))
                if self._ai == 1:
                    while True:
                        try:
                            self._ai_color = int(input("0 -> cross | 1 -> rounds: "))
                            if self._ai_color == 0 or self._ai_color == 1:
                                return
                        except:
                            print("Enter the number 0, 1 or 2")
                elif self._ai == 0 or self._ai == 2:
                    return
            except:
                print("Enter the number 0, 1 or 2")