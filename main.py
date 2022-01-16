import random
import time
import copy
from os import system


def clear():
    _ = system('clear')


class Board:
    def __init__(self, table_):
        self.table_ = table_

    def fill(self):
        for row in self.table_:
            for elem in range(len(row)):
                x = random.randint(0, 20)
                if x < 3:
                    row[elem] = "█"
                else:
                    row[elem] = " "

    def update_cell(self, i, j, old_table):
        count_alive_neighbours = 0
        for a in [-1, 0, 1]:
            for bottom in [-1, 0, 1]:
                if a == 0 and bottom == 0:
                    continue
                if old_table[(i + a) % len(self.table_)][(j + bottom) % len(self.table_[0])] == "█":
                    count_alive_neighbours += 1
        if count_alive_neighbours == 3 and old_table[i][j] == " ":
            self.table_[i][j] = "█"
        if (count_alive_neighbours < 2 or count_alive_neighbours > 3) and old_table[i][j] == "█":
            self.table_[i][j] = " "

    def update_board(self):
        old_table = self.table_
        for i in range(len(self.table_)):
            for j in range(len(self.table_[0])):
                self.update_cell(i, j, old_table)

    def play_game(self):
        while True:
            for i in self.table_:
                for j in i:
                    print(j, end='|')
                print()
            print("\n" * 1)
            copy_table = copy.deepcopy(self.table_)
            self.update_board()
            if copy_table == self.table_:
                print("ENDGAME -- CYCLE")
                break
            time.sleep(0.1)


print("Input width and height of table. Default is 60 * 50 for fullscreen")
w, h = map(int, (input().split()))
table = [["" for x in range(w)] for y in range(h)]
b = Board(table)
b.fill()
b.play_game()
