from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def is_legal_move(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class King(Figure):

    def __init__(self, color, id_fig):
        super().__init__("King")
        self.color = color
        self.id = id_fig

    def is_legal_move(self):
        pass

    def __str__(self):
        return "♚" + self.color


class Queen(Figure):

    def __init__(self, color, id_fig):
        super().__init__("Queen")
        self.color = color
        self.id = id_fig

    def is_legal_move(self):
        pass

    def __str__(self):
        return "♛" + self.color


class Rook(Figure):

    def __init__(self, color, id_fig):
        super().__init__("Rook")
        self.color = color
        self.id = id_fig

    def is_legal_move(self):
        pass

    def __str__(self):
        return "♜" + self.color


class Knight(Figure):

    def __init__(self, color, id_fig):
        super().__init__("Knight")
        self.color = color
        self.id = id_fig

    def is_legal_move(self):
        pass

    def __str__(self):
        return "♞" + self.color


class Bishop(Figure):

    def __init__(self, color, id_fig):
        super().__init__("Bishop")
        self.color = color
        self.id = id_fig

    def is_legal_move(self):
        pass

    def __str__(self):
        return "♝" + self.color


class Pawn(Figure):

    def __init__(self, color, id_fig):
        super().__init__("Pawn")
        self.color = color
        self.id = id_fig

    def is_legal_move(self):
        pass

    def __str__(self):
        return "♟" + self.color


class Empty(Figure):

    def __init__(self):
        super().__init__("Empty")
        self.color = "empty"

    def is_legal_move(self):
        return NotImplementedError

    def __str__(self):
        return "  "
