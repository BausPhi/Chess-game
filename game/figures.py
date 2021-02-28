from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def __init__(self, name: str, position: tuple, color: str, moves):
        self.name = name
        self.color = color  # ID of a figure together with name
        self.position = position  # ID of a figure
        self.moves = moves

    '''
    Calculates all possible moves for the current
    game state of the moving player
    Also checks if the player would be mate if he would
    execute that move
    '''
    @abstractmethod
    def update_possible_moves(self, field):
        pass

    '''
    Calculates all possible moves for the current
    game state
    '''
    @abstractmethod
    def get_possible_moves(self, field):
        pass

    '''
    Calculates all moves from current position
    without looking at other figures
    Only uses the figure specific possible movements
    according to position in field
    '''
    @abstractmethod
    def all_moves(self):
        pass

    '''
    Returns the string representation of a figure
    '''
    @abstractmethod
    def __str__(self):
        pass


class King(Figure):

    def __init__(self, color, pos):
        super().__init__("King", pos, color, [])
        self.rochade = True

    def update_possible_moves(self, field):                   # TODO check for mate
        self.moves = []
        moves = self.all_moves()
        for move in moves:
            if field[move[0]][move[1]].color != self.color:
                self.moves.append({"start": self.position, "end": move})

    def get_possible_moves(self, field):
        filtered_moves = []
        moves = self.all_moves()
        for move in moves:
            if field[move[0]][move[1]].color != self.color:
                filtered_moves.append({"start": self.position, "end": move})
        return filtered_moves

    def all_moves(self):
        moves = []
        x = self.position[0]
        y = self.position[1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x + i < 8 and 0 <= y + j < 8:
                    moves.append((x + i, y + j))
        return moves

    def __str__(self):
        return "♚" + self.color


class Queen(Figure):

    def __init__(self, color, pos):
        super().__init__("Queen", pos, color, [])
        self.rochade = None

    def update_possible_moves(self, field):                   # TODO check for mate
        pass

    def get_possible_moves(self, field):
        pass

    def all_moves(self):
        pass

    def __str__(self):
        return "♛" + self.color


class Rook(Figure):

    def __init__(self, color, pos):
        super().__init__("Rook", pos, color, [])
        self.rochade = True

    def update_possible_moves(self, field):                   # TODO check for mate
        pass

    def get_possible_moves(self, field):
        pass

    def all_moves(self):
        pass

    def __str__(self):
        return "♜" + self.color


class Knight(Figure):

    def __init__(self, color, pos):
        super().__init__("Knight", pos, color, [])
        self.rochade = True

    def update_possible_moves(self, field):                   # TODO check for mate
        self.moves = []
        moves = self.all_moves()
        for move in moves:
            tile = field[move[0]][move[1]]
            if isinstance(tile, Empty) or tile.color == other_color(self.color):
                self.moves.append({"start": self.position, "end": move})

    def get_possible_moves(self, field):
        filtered_moves = []
        moves = self.all_moves()
        for move in moves:
            tile = field[move[0]][move[1]]
            if isinstance(tile, Empty) or tile.color == other_color(self.color):
                filtered_moves.append({"start": self.position, "end": move})
        return filtered_moves

    def all_moves(self):
        moves = []
        x = self.position[0]
        y = self.position[1]
        for first_move in [-2, 2]:
            for second_move in [-1, 1]:
                if 0 <= x + first_move < 8:
                    if 0 <= y + second_move < 8:
                        moves.append((x + first_move, y + second_move))
                if 0 <= y + first_move < 8:
                    if 0 <= x + second_move < 8:
                        moves.append((x + second_move, y + first_move))
        return moves

    def __str__(self):
        return "♞" + self.color


class Bishop(Figure):

    def __init__(self, color, pos):
        super().__init__("Bishop", pos, color, [])
        self.rochade = True

    def update_possible_moves(self, field):                   # TODO check for mate
        self.moves = []
        x = self.position[0]
        y = self.position[1]
        loop1, loop2, loop3, loop4 = True, True, True, True
        for i in range(1, 8):
            if loop1:
                if x - i >= 0 and y - i >= 0:
                    tile = field[x - i][y - i]
                    if isinstance(tile, Empty):
                        self.moves.append({"start": self.position, "end": (x - i, y - i)})
                    elif tile.color != self.color:
                        self.moves.append({"start": self.position, "end": (x - i, y - i)})
                        loop1 = False
                    else:
                        loop1 = False
            if loop2:
                if x - i >= 0 and y + i < 8:
                    tile = field[x - i][y + i]
                    if isinstance(tile, Empty):
                        self.moves.append({"start": self.position, "end": (x - i, y + i)})
                    elif tile.color != self.color:
                        self.moves.append({"start": self.position, "end": (x - i, y + i)})
                        loop2 = False
                    else:
                        loop2 = False
            if loop3:
                if x + i < 8 and y - i >= 0:
                    tile = field[x + i][y - i]
                    if isinstance(tile, Empty):
                        self.moves.append({"start": self.position, "end": (x + i, y - i)})
                    elif tile.color != self.color:
                        self.moves.append({"start": self.position, "end": (x + i, y - i)})
                        loop3 = False
                    else:
                        loop3 = False
            if loop4:
                if x + i < 8 and y + i < 8:
                    tile = field[x + i][y + i]
                    if isinstance(tile, Empty):
                        self.moves.append({"start": self.position, "end": (x + i, y + i)})
                    elif tile.color != self.color:
                        self.moves.append({"start": self.position, "end": (x + i, y + i)})
                        loop4 = False
                    else:
                        loop4 = False

    def get_possible_moves(self, field):
        moves = []
        x = self.position[0]
        y = self.position[1]
        loop1, loop2, loop3, loop4 = True, True, True, True
        for i in range(1, 8):
            if loop1:
                if x - i >= 0 and y - i >= 0:
                    tile = field[x - i][y - i]
                    if isinstance(tile, Empty):
                        moves.append({"start": self.position, "end": (x - i, y - i)})
                    elif tile.color != self.color:
                        moves.append({"start": self.position, "end": (x - i, y - i)})
                        loop1 = False
                    else:
                        loop1 = False
            if loop2:
                if x - i >= 0 and y + i < 8:
                    tile = field[x - i][y + i]
                    if isinstance(tile, Empty):
                        moves.append({"start": self.position, "end": (x - i, y + i)})
                    elif tile.color != self.color:
                        moves.append({"start": self.position, "end": (x - i, y + i)})
                        loop2 = False
                    else:
                        loop2 = False
            if loop3:
                if x + i < 8 and y - i >= 0:
                    tile = field[x + i][y - i]
                    if isinstance(tile, Empty):
                        moves.append({"start": self.position, "end": (x + i, y - i)})
                    elif tile.color != self.color:
                        moves.append({"start": self.position, "end": (x + i, y - i)})
                        loop3 = False
                    else:
                        loop3 = False
            if loop4:
                if x + i < 8 and y + i < 8:
                    tile = field[x + i][y + i]
                    if isinstance(tile, Empty):
                        moves.append({"start": self.position, "end": (x + i, y + i)})
                    elif tile.color != self.color:
                        moves.append({"start": self.position, "end": (x + i, y + i)})
                        loop4 = False
                    else:
                        loop4 = False
        return moves

    def all_moves(self):
        return NotImplementedError

    def __str__(self):
        return "♝" + self.color


class Pawn(Figure):

    def __init__(self, color, pos):
        super().__init__("Pawn", pos, color, [])
        self.rochade = True

    def update_possible_moves(self, field):                   # TODO check for mate
        self.moves = []
        moves = self.all_moves()
        startx, starty = self.position[0], self.position[1]
        for move in moves:
            endx, endy = move[0], move[1]
            if startx != endx and starty != endy:
                if field[endx][endy].color == other_color(self.color):
                    self.moves.append({"start": self.position, "end": move})
            elif starty + 2 == endy:
                if isinstance(field[startx][starty + 1], Empty) and isinstance(field[startx][starty + 2], Empty):
                    self.moves.append({"start": self.position, "end": move})
            elif starty - 2 == endy:
                if isinstance(field[startx][starty - 1], Empty) and isinstance(field[startx][starty - 2], Empty):
                    self.moves.append({"start": self.position, "end": move})
            elif starty + 1 == endy:
                if isinstance(field[startx][starty + 1], Empty):
                    self.moves.append({"start": self.position, "end": move})
            elif starty - 1 == endy:
                if isinstance(field[startx][starty - 1], Empty):
                    self.moves.append({"start": self.position, "end": move})

    def get_possible_moves(self, field):
        filtered_moves = []
        moves = self.all_moves()
        startx, starty = self.position[0], self.position[1]
        for move in moves:
            endx, endy = move[0], move[1]
            if startx != endx and starty != endy:
                if field[endx][endy].color == other_color(self.color):
                    filtered_moves.append({"start": self.position, "end": move})
            elif starty + 2 == endy:
                if isinstance(field[startx][starty + 1], Empty) and isinstance(field[startx][starty + 2], Empty):
                    filtered_moves.append({"start": self.position, "end": move})
            elif starty - 2 == endy:
                if isinstance(field[startx][starty - 1], Empty) and isinstance(field[startx][starty - 2], Empty):
                    filtered_moves.append({"start": self.position, "end": move})
            elif starty + 1 == endy:
                if isinstance(field[startx][starty + 1], Empty):
                    filtered_moves.append({"start": self.position, "end": move})
            elif starty - 1 == endy:
                if isinstance(field[startx][starty - 1], Empty):
                    filtered_moves.append({"start": self.position, "end": move})
        return filtered_moves

    def all_moves(self):
        moves = []
        if self.color == "w":
            x = self.position[0]
            y = self.position[1]
            if 0 <= y - 1 < 8:
                moves.append((x, y - 1))
                if 0 <= x - 1 < 8:
                    moves.append((x - 1, y - 1))
                if 0 <= x + 1 < 8:
                    moves.append((x + 1, y - 1))
            if y == 6:
                moves.append((x, y - 2))
        else:
            x = self.position[0]
            y = self.position[1]
            if 0 <= y + 1 < 8:
                moves.append((x, y + 1))
                if 0 <= x - 1 < 8:
                    moves.append((x - 1, y + 1))
                if 0 <= x + 1 < 8:
                    moves.append((x + 1, y + 1))
            if y == 1:
                moves.append((x, y + 2))
        return moves

    def __str__(self):
        return "♟" + self.color


class Empty(Figure):

    def __init__(self, pos):
        super().__init__("Empty", pos, None, None)
        self.rochade = True

    def update_possible_moves(self, field):
        return NotImplementedError

    def get_possible_moves(self, field):
        return NotImplementedError

    def all_moves(self):
        return NotImplementedError

    def __str__(self):
        return "  "


def other_color(color):
    if color == "w":
        return "b"
    if color == "b":
        return "w"
