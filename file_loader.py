import json

class FileLoader:

    def __init__(self, filename):
        self.filename = filename
  

    def load_game(self):
        with open(self.filename, "r") as openfile:
            file_data = dict(json.load(openfile))

        lst = [[] for _ in range(24)]

        for items in file_data.items():
            lst[int(items[0])-1] = list(items[1].values())

        for i in lst:
            if len(i) == 0:
                i.append(-1)


        return(lst)
    

    def save_game(self, board):

        dict_file = {}

        i = 1
        for column in board:
            if len(column) != 1:
                dict_file[i] = {"number": column[0], "color": column[1]}
            i += 1

        with open(self.filename, "w") as outfile:
            json.dump(dict_file, outfile)