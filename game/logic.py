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

    def execute_move(self, widget, tiles):                               # TODO
        # get information about the clicked tile
        posx, posy = 0, 0
        clicked_tile = ""
        for tile in tiles:
            if widget == tile[0]:
                posy = tile[1]
                posx = tile[2]
                clicked_tile = tile[0]
        border_value = str(clicked_tile.cget("borderwidth"))
        if self.turn == 1 and self.field.points[posx][posy].color == "w":
            if border_value == "2":
                clicked_tile.config(borderwidth=5, relief="groove")
            if border_value == "5":
                clicked_tile.config(borderwidth=2, relief="flat")
        elif self.turn == 2 and self.field.points[posx][posy].color == "b":
            if border_value == "2":
                clicked_tile.config(borderwidth=5, relief="groove")
            if border_value == "5":
                clicked_tile.config(borderwidth=2, relief="flat")

    # Am Ende der Funktion die bei draufdrücken auf Feld passiert muss noch gechecked werden ob AI dran ist.
    # Wenn ja dann mus AI Zug auch noch in dieser Funktion ausgeführt werden

    def is_legal_move(self, pos_start: tuple, pos_end: tuple):        # TODO
        pass

    def is_check_mate(self):                                          # TODO
        pass

    def field_to_one_hot_encoding(self):
        self.field.to_one_hot_encoding()

    def run_game_multiple_ai(self):                                   # TODO
        return self
