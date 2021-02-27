from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    from ui.ui_game import Game

from game.field import Field
from game.ai import AI


class GameRun:

    def __init__(self, ui: Game, turn: int, mode: int):
        self.field = Field(beginning=True, empty=False, field=None)
        self.turn = turn
        self.ui = ui
        self.mode = mode
        self.ai = AI()
        self.a12 = AI()
        pass

    def execute_move(self, widget, tiles):                               # TODO
        # get information about the clicked tile
        clicked_tile, posx, posy = get_clicked_tile(widget, tiles)

        # check if there was a field clicked before
        marked, marked_pos = self.clicked_before()

        # update ui (if one was clicked before don't be able to click another one)
        self.update_ui_click(clicked_tile, marked, posx, posy)

        # if 1 field was already marked, check if it is a valid move by checking the moves field of a figure
        # if yes perform it
        return self.perform_move(marked, marked_pos, tiles, posx, posy)

    '''
    If two AI are playing against each other, we have to deactivate clicks
    and the game should play without any interaction from the user
    '''
    def run_game_multiple_ai(self):                                   # TODO
        return self

    '''
    Updates the game UI when a figure was clicked by a player.
    It only updates when the figure has the correct color according
    to the current turn
    '''
    def update_ui_click(self, clicked_tile, marked, posx, posy):
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

    '''
    Check if there was already a figure clicked before
    '''
    def clicked_before(self):
        marked = 0
        marked_pos = None
        for i in range(8):
            for j in range(8):
                if str(self.ui.tiles[j * 8 + i][0].cget("borderwidth")) == "8":
                    marked = 1
                    marked_pos = j * 8 + i
                    break
        return marked, marked_pos

    '''
    Perform the clicked move if it is valid
    '''
    def perform_move(self, marked, marked_pos, tiles, posx, posy):       # TODO
        if marked == 1:
            pos_start = (tiles[marked_pos][1], self.ui.tiles[marked_pos][2])
            pos_end = (posx, posy)
            # if the positions are the same => same tile was clicked again
            if pos_start == pos_end:
                return None

    '''
    Check for check mate, mate and a draw
    Also check if a pawn reched the end
    '''
    def post_move(self):                                                 # TODO
        pass


'''
Gets information about the clicked tile
'''
def get_clicked_tile(widget, tiles):
    posx, posy = 0, 0
    clicked_tile = ""
    for tile in tiles:
        if widget == tile[0]:
            posx = tile[1]
            posy = tile[2]
            clicked_tile = tile[0]
    return clicked_tile, posx, posy
