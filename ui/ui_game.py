import tkinter as tk
import random

from game.logic import GameLogic


class Game:

    def __init__(self, mode: int):
        # mode: 0 = Player vs Player, 1 = Player vs AI, 2 = AI vs AI
        self.mode = mode
        self.gui = tk.Tk(className="Game")
        self.game = GameLogic(self, random.randint(1, 2))
        # gui elements
        self.tiles = []                        # TODO set files

    def start_game(self):
        self.gui.title("Chess")
        # If mode = 2, then 2 AI are batteling each other, so we dont click anywhere
        if self.mode == 2:
            self.gui.after(0, self.game.run_game_multiple_ai)
        self.gui.mainloop()
        pass

# Am Ende der Funktion die bei draufdrücken auf Feld passiert muss noch gechecked werden ob AI dran ist.
# Wenn ja dann mus AI Zug auch noch in dieser Funktion ausgeführt werden
