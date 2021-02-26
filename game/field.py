from game.figures import *

import copy


class Field:

    def __init__(self):                 # TODO
        self.points = intialize_board()
        # self.print_board()

    def to_one_hot_encoding(self):      # TODO
        pass

    def print_board(self):
        print("-------------------------")
        for i in range(8):
            print("|" + str(self.points[i][0]) + "|" + str(self.points[i][1]) + "|" + str(self.points[i][2]) +
                  "|" + str(self.points[i][3]) + "|" + str(self.points[i][4]) + "|" + str(self.points[i][5]) +
                  "|" + str(self.points[i][6]) + "|" + str(self.points[i][7]) + "|")
            print("-------------------------")

    def is_check_mate(self, pos_start: tuple, pos_end: tuple):            # TODO
        field = copy.deepcopy(self.points)
        field = movefigures(pos_start, pos_end, field, self)
        color = field[pos_end[0]][pos_end[1]].color
        return check_mate_check(field, color)


def intialize_board():
    color = "w"
    color_b = "b"
    pawns, rooks, knights, bishops = [], [], [], []
    pawns_b, rooks_b, knights_b, bishops_b = [], [], [], []
    for i in range(8):
        pawns.append(Pawn(color, i))
        pawns_b.append(Pawn(color_b, i))
    for i in range(2):
        rooks.append(Rook(color, i))
        knights.append(Knight(color, i))
        bishops.append(Bishop(color, i))
        rooks_b.append(Rook(color_b, i))
        knights_b.append(Knight(color_b, i))
        bishops_b.append(Bishop(color_b, i))
    king = King(color, 1)
    queen = Queen(color, 1)
    king_b = King(color_b, 1)
    queen_b = Queen(color_b, 1)
    field = []
    for i in range(8):
        temp = []
        if i == 6:
            for j in range(8):
                temp.append(pawns[j])
        if i == 7:
            temp.append(rooks[0])
            temp.append(knights[0])
            temp.append(bishops[0])
            temp.append(king)
            temp.append(queen)
            temp.append(bishops[1])
            temp.append(knights[1])
            temp.append(rooks[1])
        if i == 1:
            for j in range(8):
                temp.append(pawns_b[j])
        if i == 0:
            temp.append(rooks_b[0])
            temp.append(knights_b[0])
            temp.append(bishops_b[0])
            temp.append(king_b)
            temp.append(queen_b)
            temp.append(bishops_b[1])
            temp.append(knights_b[1])
            temp.append(rooks_b[1])
        if 1 < i < 6:
            for j in range(8):
                temp.append(Empty())
        field.append(temp)
    return field


def movefigures(pos_start: tuple, pos_end: tuple, field, fields):
    field[pos_end[0]][pos_end[1]] = field[pos_start[0]][pos_start[1]]
    field[pos_start[0]][pos_start[1]] = Empty()
    return field
    pass


def print_board(field):
    print("-------------------------")
    for i in range(8):
        print("|" + str(field[i][0]) + "|" + str(field[i][1]) + "|" + str(field[i][2]) +
                "|" + str(field[i][3]) + "|" + str(field[i][4]) + "|" + str(field[i][5]) +
                "|" + str(field[i][6]) + "|" + str(field[i][7]) + "|")
        print("-------------------------")


def check_mate_check(field, color: int):
    moves = []
    king_pos = None
    for i in range(8):
        for j in range(8):
            figure = field[i][j]
            if isinstance(figure, Empty):
                continue
            if figure.color != color:
                continue
            if isinstance(figure, King):
                king_pos = (i, j)
            moves = figure.get_possible_moves((i, j))
    for move in moves:
        if king_pos == move:
            return True
    return False
