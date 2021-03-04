from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    from ui.ui_game import Game

from game.field import Field
from game.ai import AI
from game.figures import *


class GameRun:

    def __init__(self, ui: Game, turn: int, mode: int):
        self.field = Field(beginning=True, empty=False, field=None)
        self.turn = turn
        self.ui = ui
        self.mode = mode
        if mode == 1:
            self.ai = AI()
        elif mode == 2:
            self.a12 = AI()
        pass
        self.saved_game_scenarios = [self.field.points]

    def execute_move(self, widget, tiles):
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
                self.before_move(self.field.points[posx][posy])
                if border_value == "2":
                    clicked_tile.config(borderwidth=8, relief="groove")
            if border_value == "8":
                clicked_tile.config(borderwidth=2, relief="flat")
        elif self.turn == 2 and self.field.points[posx][posy].color == "b":
            if marked == 0:
                self.before_move(self.field.points[posx][posy])
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
    Returns if game is over
    '''
    def perform_move(self, marked, marked_pos, tiles, posx, posy):
        if marked == 1:
            pos_start = (tiles[marked_pos][1], self.ui.tiles[marked_pos][2])
            figure = self.field.points[pos_start[0]][pos_start[1]]
            pos_end = (posx, posy)
            figure_end = self.field.points[pos_end[0]][pos_end[1]]
            # If the same tile as before is clicked => do nothing
            if pos_start == pos_end:
                for i in range(64):
                    if self.ui.tiles[i][0].cget("borderwidth") == 4:
                        self.ui.tiles[i][0].config(borderwidth=2, relief="flat")
                return False, "", 0
            # Unmarks the current figure and marks the new figure
            if figure.color == figure_end.color:
                self.ui.tiles[marked_pos][0].config(borderwidth=2, relief="flat")
                self.ui.tiles[posy * 8 + posx][0].config(borderwidth=8, relief="groove")
                self.before_move(figure_end)
            # If the clicked figure has a possible move to the field where you clicked => execute it
            for move in figure.moves:
                if move["end"] == pos_end:
                    self.field.move_figure(move["start"], move["end"])
                    return self.after_move()
            return False, "", 0
        return False, "", 0

    '''
    Check for check mate, mate and a draw
    Also check if a pawn reched the end
    Change the turn
    '''
    def after_move(self):
        # change pawns at end
        figure = self.field.pawn_at_end(self.turn)
        if figure is not None:
            if self.turn == 1:
                self.field.points[figure.position[0]][figure.position[1]] = Queen(color="w", pos=figure.position)
                self.field.points[figure.position[0]][figure.position[1]].created = True
            else:
                self.field.points[figure.position[0]][figure.position[1]] = Queen(color="b", pos=figure.position)
                self.field.points[figure.position[0]][figure.position[1]].created = True
        # swap turn
        turn = self.turn
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        # update gui
        draw = self.change_gui_after_move()
        # check for mate, chec_mate and a draw
        self.saved_game_scenarios.append(copy.deepcopy(self.field.points))
        if self.field.is_draw(turn) or draw:
            return True, "Draw", 0
        elif self.field.is_check_mate(turn):
            return True, "Check Mate", turn
        elif self.field.is_mate(turn):
            for row in self.field.points:
                for figure in row:
                    if self.turn == 1:
                        if figure.name == "King" and figure.color == "w":
                            self.ui.tiles[figure.position[1] * 8 + figure.position[0]][0].config(image=self.ui.images["king_w_red"])
                    else:
                        if figure.name == "King" and figure.color == "b":
                            self.ui.tiles[figure.position[1] * 8 + figure.position[0]][0].config(image=self.ui.images["king_red"])
            return False, "", 0
        return False, "", 0

    '''
    Updates the figures on the UI after the move, changes the label
    that shows the current player's turn etc.
    '''
    def change_gui_after_move(self):
        self.ui.turn_label.config(text="Player " + str(self.turn) + ", it is your turn")
        for tile in self.ui.tiles:
            tile[0].config(borderwidth=2, relief="flat")
        for row in self.field.points:
            for figure in row:
                pos = figure.position
                pos_tile = pos[1] * 8 + pos[0]
                if figure.color == "w":
                    if figure.name == "King":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["king_w"])
                    if figure.name == "Pawn":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["pawn_w"])
                    if figure.name == "Queen":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["queen_w"])
                    if figure.name == "Rook":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["rook_w"])
                    if figure.name == "Knight":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["knight_w"])
                    if figure.name == "Bishop":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["bishop_w"])
                elif figure.color == "b":
                    if figure.name == "King":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["king"])
                    if figure.name == "Pawn":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["pawn"])
                    if figure.name == "Queen":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["queen"])
                    if figure.name == "Rook":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["rook"])
                    if figure.name == "Knight":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["knight"])
                    if figure.name == "Bishop":
                        self.ui.tiles[pos_tile][0].config(image=self.ui.images["bishop"])
                else:
                    self.ui.tiles[pos_tile][0].config(image='')
        for i in range(len(self.field.destroyed_b)):
            self.ui.black_destroyed_labels[i].config(image=self.ui.small_images[self.field.destroyed_b[i].name.lower()])
        for i in range(len(self.field.destroyed_w)):
            self.ui.white_destroyed_labels[i].config(image=self.ui.small_images[self.field.destroyed_w[i].name.lower() + "_w"])
        if self.field.useless_moves >= 100:
            return True
        if self.three_times_same_scenario():
            return True
        return False

    '''
    Updates the new possible moves for a player
    and marks it on the field.
    Is called when the player marks a figure that he would
    like to move
    '''
    def before_move(self, figure):
        for i in range(64):
            if self.ui.tiles[i][0].cget("borderwidth") == 4:
                self.ui.tiles[i][0].config(borderwidth=2, relief="flat")
        if self.turn == 1 and figure.color == "w":
            figure.update_possible_moves(self.field)
            for move in figure.moves:
                self.ui.tiles[move["end"][1] * 8 + move["end"][0]][0].config(borderwidth=4, relief="solid")
        if self.turn == 2 and figure.color == "b":
            figure.update_possible_moves(self.field)
            for move in figure.moves:
                self.ui.tiles[move["end"][1] * 8 + move["end"][0]][0].config(borderwidth=4, relief="solid")
        return

    '''
    Checks if we had three times the same field
    (the same figures were on the same field)
    '''
    def three_times_same_scenario(self):
        count = 0
        for scenario in self.saved_game_scenarios:
            if self.compare_scenarios(scenario):
                count += 1
            if count >= 3:
                return True
        if count < 3:
            return False

    '''
    Compare two different scenarios and return
    if they are the same or not
    '''
    def compare_scenarios(self, scenario):
        for i in range(8):
            for j in range(8):
                #print(self.field.points[i][j].name)
                #print(scenario[i][j].name)
                if self.field.points[i][j].name != scenario[i][j].name:
                    return False
        return True


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
