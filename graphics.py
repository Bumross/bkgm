from termcolor import colored
from checker import Checker
import os

class Graphics:
    
    CHECKER_TYPE_A = "x"
    CHECKER_TYPE_B = "o"
    dict_for_pos = {0:11, 1:10, 2:9, 3:8, 4:7, 5:6, 6:5, 7:4, 8:3, 9:2, 10:1, 11:0}


    @classmethod
    def draw(self, board, highligted):
        
        os.system("clear")

        print("  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("  ┣13━14━15━16━17━18┳━━━┳19━20━21━22━23━24┫")
        self.draw_block(board[12:], 0, 5, 1, highligted-13, 1)
        print("  ┃                 ┃BAR┃                 ┃")
        self.draw_block(board[11::-1], 4, -1, -1, highligted-1, -1)
        print("  ┣12━11━10━09━08━07┻━━━┻06━05━04━03━02━01┫")
        print("  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    @classmethod
    def draw_rows(self, set, row, i, highlighted, min, max):
        #returns half-row for printing
        k = min
        for pos in set:
            if pos[0] <= i:
                row += " ·"
            elif pos[0] > i:
                row += " " + colored(
                    self.CHECKER_TYPE_A if pos[1] == 0 else self.CHECKER_TYPE_B,
                    "green" if k == highlighted else "white")
            if k < max:
                row += " "
            k += 1
        return row

    @classmethod
    def draw_block(self, list, a , b, c, h, sec):
        #prints whole half board
        for i in range(a, b, c):
            row = ""
            row += "  ┃" + self.draw_rows(list[:6], row, i, h, 0, 5) + "┃   ┃" + self.draw_rows(list[6:], row, i, h, 6, 11) + "┃"
            print(row)