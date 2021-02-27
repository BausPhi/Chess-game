from game.figures import *

import copy


class Field:

    def __init__(self, beginning, empty, field):
        if beginning:
            self.points = intialize_board()
        elif empty:
            self.points = intialize_board()
            for i in range(8):
                for j in range(8):
                    self.points[i][j] = Empty(pos=(i, j))
        else:
            self.points = field

    '''
    Converts the field to a one-hot encoded version.
    Needs to be used for integration of the AI.
    '''
    def to_one_hot_encoding(self):  # TODO
        pass

    '''
    Performs a move on the field
    If king or rook moves set rochade to False
    '''
    def move_figure(self, start: tuple, end: tuple):
        self.points[end[0]][end[1]] = self.points[start[0]][start[1]]
        self.points[end[0]][end[1]].position = (end[0], end[1])
        self.points[start[0]][start[1]] = Empty(pos=(start[0], start[1]))
        return

    '''
    Returns a copy of the field.
    Can be used to simulate moves for example to check if
    moves result in a mate.
    '''
    def field_copy(self):
        return copy.deepcopy(self.points)

    def king_in_danger(self, player):        # TODO
        pass

    '''
    Checks whether a player is check mate.
    If yes, the game is over
    '''
    def is_check_mate(self, player):
        if not self.king_in_danger(player):
            return False
        if player == 1:
            color = "w"
        else:
            color = "b"
        moves = []
        for row in self.points:
            for figure in row:
                if figure.name == "King" and figure.color == color:
                    moves = figure.moves
        for move in moves:
            copy_field = self.field_copy()
            copy_field[move['end'][0]][move['end'][1]] = copy_field[move['start'][0]][move['start'][1]]
            copy_field[move['start'][0]][move['start'][1]] = Empty(pos=(move['start'][0], move['start'][1]))
            copy_field = Field(beginning=False, empty=False, field=copy_field)
            if not copy_field.is_mate(player):
                return False
        return True

    '''
    Checks whether a player is check mate.
    If yes, the game is over
    '''
    def is_mate(self, player):               # TODO
        if player == 1:
            enemy_color = "b"
            color = "w"
        else:
            enemy_color = "w"
            color = "b"
        enemy_figures = []
        for row in self.points:
            for figure in row:
                if figure.color == enemy_color:
                    enemy_figures.append(figure)
        king_pos = None
        for i in range(8):
            for j in range(8):
                if self.points[i][j].name == "King" and self.points[i][j].color == color:
                    king_pos = (i, j)
        for figure in enemy_figures:
            for move in figure.get_possible_moves(figure.get_position(self.points)):
                if move["end"] == king_pos:
                    return True
        return False
        pass

    '''
    Checks whether the game ended in a draw
    '''
    def is_draw(self):               # TODO
        pass

    '''
    Calculates every possible move for every figure and saves
    them in moves field of the figure
    It is only done for the figures of the player whose turn it is
    '''
    def update_all_possible_moves(self, turn):     # TODO
        pass

    '''
    Checks if a rochade is possible or not
    Returns a list of towers, a rochade is possible with
    '''
    def rochade_possible(self, turn):              # TODO
        pass

    '''
    Checks if there is a pawn at the end of the field
    and returns the pawn if there is one, else None
    '''
    def pawn_at_end(self, turn):
        for i in range(8):
            for j in range(8):
                if j == 7 and turn == 2:
                    figure = self.points[i][j]
                    if isinstance(figure, Pawn) and figure.color == "b":
                        return figure
                if j == 0 and turn == 1:
                    figure = self.points[i][j]
                    if isinstance(figure, Pawn) and figure.color == "w":
                        return figure
        return None

    '''
    Converts a pawn to a given figure
    '''
    def convert_pawn(self, pawn, figure):          # TODO
        pass

    '''
    Prints the board for debugging code
    '''
    def print_board(self):
        print("-------------------------")
        for i in range(8):
            print("|" + str(self.points[0][i]) + "|" + str(self.points[1][i]) + "|" + str(self.points[2][i]) +
                  "|" + str(self.points[3][i]) + "|" + str(self.points[4][i]) + "|" + str(self.points[5][i]) +
                  "|" + str(self.points[6][i]) + "|" + str(self.points[7][i]) + "|")
            print("-------------------------")


'''
Initializes the field at the beginning of the game.
Initializes the figure elements and sets them at the
correct position on the field. 
'''
def intialize_board():
    color = "w"
    color_b = "b"
    field = []
    for i in range(8):
        temp = []
        if i == 6:
            for j in range(8):
                temp.append(Pawn(color=color, pos=(j, 6)))
        if i == 7:
            temp.append(Rook(color=color, pos=(0, 7)))
            temp.append(Knight(color=color, pos=(1, 7)))
            temp.append(Bishop(color=color, pos=(2, 7)))
            temp.append(King(color=color, pos=(3, 7)))
            temp.append(Queen(color=color, pos=(4, 7)))
            temp.append(Bishop(color=color, pos=(5, 7)))
            temp.append(Knight(color=color, pos=(6, 7)))
            temp.append(Rook(color=color, pos=(7, 7)))
        if i == 1:
            for j in range(8):
                temp.append(Pawn(color=color_b, pos=(j, 1)))
        if i == 0:
            temp.append(Rook(color=color_b, pos=(0, 0)))
            temp.append(Knight(color=color_b, pos=(1, 0)))
            temp.append(Bishop(color=color_b, pos=(2, 0)))
            temp.append(King(color=color_b, pos=(3, 0)))
            temp.append(Queen(color=color_b, pos=(4, 0)))
            temp.append(Bishop(color=color_b, pos=(5, 0)))
            temp.append(Knight(color=color_b, pos=(6, 0)))
            temp.append(Rook(color=color_b, pos=(7, 0)))
        if 1 < i < 6:
            for j in range(8):
                temp.append(Empty(pos=(j, i)))
        field.append(temp)
    field_reordered = []
    for i in range(8):
        spalte = []
        for j in range(8):
            spalte.append(field[j][i])
        field_reordered.append(spalte)
    return field_reordered


'''
Prints the board for debugging code
'''
def print_board(field):
    print("-------------------------")
    for i in range(8):
        print("|" + str(field[0][i]) + "|" + str(field[1][i]) + "|" + str(field[2][i]) +
              "|" + str(field[3][i]) + "|" + str(field[4][i]) + "|" + str(field[5][i]) +
              "|" + str(field[6][i]) + "|" + str(field[7][i]) + "|")
        print("-------------------------")
