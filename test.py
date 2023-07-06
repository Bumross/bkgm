from file_loader import FileLoader

board = [[2, 1], [-1], [-1], [-1], [-1], [5, 0], [-1], [3, 0], [-1], [-1], [-1], [5, 1], [5, 0], [-1], [-1], [-1], [3, 1], [-1], [5, 1], [-1], [-1], [-1], [-1], [2, 0]]

dict_file = {}

i = 1
for column in board:
    if len(column) != 1:
        dict_file[i] = {"number": column[0], "color": column[1]}
    i += 1

print(dict_file)