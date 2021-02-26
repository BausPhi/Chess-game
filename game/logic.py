from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    from ui.ui_game import Game

from game.field import Field
from game.ai import AI


class GameLogic:

    def __init__(self, ui: Game, turn: int, mode: int):
        self.field = Field()
        self.turn = turn
        self.ui = ui
        self.mode = mode
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
        # check if there was a field clicked before
        marked = 0
        marked_pos = None
        for i in range(8):
            for j in range(8):
                if str(self.ui.tiles[j*8+i][0].cget("borderwidth")) == "8":
                    marked = 1
                    marked_pos = j*8+i
                    break
        # update ui (if one was clicked before don't be able to click another one)
        border_value = str(clicked_tile.cget("borderwidth"))
        if self.turn == 1 and self.field.points[posx][posy].color == "w":
            if marked == 0:
                if border_value == "2":
                    clicked_tile.config(borderwidth=8, relief="groove")
            if border_value == "8":
                clicked_tile.config(borderwidth=2, relief="flat")
        elif self.turn == 2 and self.field.points[posx][posy].color == "b":
            if marked == 0:
                if border_value == "2":
                    clicked_tile.config(borderwidth=8, relief="groove")
            if border_value == "8":
                clicked_tile.config(borderwidth=2, relief="flat")
        # if 1 field was already marked, check if it is a valid move, if yes perform it
        if marked == 1:
            pos_start = (tiles[marked_pos][2], self.ui.tiles[marked_pos][1])
            pos_end = (posx, posy)
            # if the positions are the same => same tile was clicked again
            if pos_start == pos_end:
                return
            if not self.is_legal_move(pos_start, pos_end):
                return
            print("Legal Move")

    # Am Ende der Funktion die bei draufdrücken auf Feld passiert muss noch gechecked werden ob AI dran ist.
    # Wenn ja dann mus AI Zug auch noch in dieser Funktion ausgeführt werden

    def is_legal_move(self, pos_start: tuple, pos_end: tuple):        # TODO
        if self.field.is_check_mate(pos_start, pos_end):
            return False
        figure = self.field.points[pos_start[0]][pos_start[1]]
        return figure.is_legal_move(pos_start, pos_end)
        pass

    def move(self, pos_start: tuple, pos_end: tuple):                 # TODO
        pass

    def field_to_one_hot_encoding(self):
        self.field.to_one_hot_encoding()

    def run_game_multiple_ai(self):                                   # TODO
        return self
