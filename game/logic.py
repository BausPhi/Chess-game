from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    from ui.ui_game import Game

from field import Field


class GameLogic:

    def __init__(self, ui: Game, turn: int):
        self.field = Field()
        self.turn = turn
        self.ui = ui
        pass

    def run_game(self):           # TODO
        pass

    def execute_move(self):       # TODO
        pass

    def is_legal_move(self):      # TODO
        pass

    def is_check_mate(self):      # TODO
        pass

    def field_to_one_hot_encoding(self):
        self.field.to_one_hot_encoding()
