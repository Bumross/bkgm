import json
from file_loader import FileLoader

file = FileLoader("data.json")

columns = file.load_game()


lst = [[] for _ in range(24)]

def draw_rows(set, row, i):
    #returns half-row for printing
    k = 0
    for pos in set:
        if pos[0] <= i:
            row += " ·"
        elif pos[0] > i:
            row += " x" if pos[1] == 0 else " o"
        if k < 5:
            row += " "
        k += 1
    return row

def draw_block(list, a , b, c):
    #prints whole half board
    for i in range(a, b, c):
        row = ""
        row += "  ┃" + draw_rows(list[:6], row, i) + "┃   ┃" + draw_rows(list[6:], row, i) + "┃"
        print(row)

for items in columns.items():
    lst[int(items[0])-1] = list(items[1].values())

for i in lst:
    if len(i) == 0:
        i.append(-1)

print("  ┏13━14━15━16━17━18┳━━━┳19━20━21━22━23━24┓")
draw_block(lst[12:], 0, 5, 1)
print("  ┃                 ┃   ┃                 ┃")
draw_block(lst[11::-1], 4, -1, -1)
print("  ┗━━━━━━━━━━━━━━━━━┻━━━┻━━━━━━━━━━━━━━━━━┛")