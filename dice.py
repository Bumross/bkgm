import random

class Dice():
    def dice_values():
        value_1 = random.randint(1, 6)
        value_2 = random.randint(1, 6)
        values = [value_1, value_2]
        return values
    
    def print_dice(values):
        ref = {
            1: ["┎───┒", "┃ 1 ┃","┖───┚" ],
            2: ["┎───┒", "┃ 2 ┃","┖───┚" ],
            3: ["┎───┒", "┃ 3 ┃","┖───┚" ],
            4: ["┎───┒", "┃ 4 ┃","┖───┚" ],
            5: ["┎───┒", "┃ 5 ┃","┖───┚" ],
            6: ["┎───┒", "┃ 6 ┃","┖───┚" ]
        }

        val_1, val_2 = ref[values[0]], ref[values[1]]
        for i in range(3):
            print("                " + val_1[i] + "   " + val_2[i])
        