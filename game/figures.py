from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def is_legal_move(self):
        pass


class King(Figure):

    def __init__(self):
        super().__init__("King")

    def is_legal_move(self):       # TODO
        pass


class Queen(Figure):

    def __init__(self):
        super().__init__("Queen")

    def is_legal_move(self):       # TODO
        pass


class Rook(Figure):

    def __init__(self):
        super().__init__("Rook")

    def is_legal_move(self):       # TODO
        pass


class Knight(Figure):

    def __init__(self):
        super().__init__("Knight")

    def is_legal_move(self):       # TODO
        pass


class Horse(Figure):

    def __init__(self):
        super().__init__("Horse")

    def is_legal_move(self):       # TODO
        pass


class Pawn(Figure):

    def __init__(self):
        super().__init__("Pawn")

    def is_legal_move(self):       # TODO
        pass
