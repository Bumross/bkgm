#totally for nothing, for later implementation recomending whole rebuild of the code-


class Checker:
    

    def __init__(self, color, column):
        self._columns = []
        self._color = color
        self._column = column


    def move(self, col, board):
        pass


    def get_color(self):
        return self._color
    

    def get_position(self, board):
        pass
    

    def delete_jumped_checkers(self, col, prev_col, board):
        #after checker jumped, delete it from previous column
        pass


    def save_to_memory(self, column):
        #saving to self columns every visited column by checker
        pass


    def move_is_valid(self, col, cur_col, board):
        pass
    # 3 couldnt be valid move but 7 could
    # 3+4 nonvalid and 4+3 valid