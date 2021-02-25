from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    from ui.ui_game import Game

from game.field import Field
from game.ai import AI


class GameLogic:

    def __init__(self, ui: Game, turn: int):
        self.field = Field()
        self.turn = turn
        self.ui = ui
        self.ai = AI()
        self.a12 = AI()
        pass

    def execute_move(self, pos1: tuple[int], pos2: tuple[int]):       # TODO
        pass

    def is_legal_move(self):                                          # TODO
        pass

    def is_check_mate(self):                                          # TODO
        pass

    def field_to_one_hot_encoding(self):
        self.field.to_one_hot_encoding()

    def run_game_multiple_ai(self):                                   # TODO
        return self
