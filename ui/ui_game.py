import tkinter as tk
import random

import game.logic as logic


class Game:

    def __init__(self, mode: int):
        # mode: 0 = Player vs Player, 1 = Player vs AI, 2 = AI vs AI
        self.mode = mode
        self.gui = tk.Tk(className="Chess")

    def start_game(self, menu_to_close):
        menu_to_close.gui.destroy()
        game = logic.GameLogic(self, random.randint(1, 2))
        self.gui.mainloop()
        pass

# Am Ende der Funktion die bei draufdrücken auf Feld passiert muss noch gechecked werden ob AI dran ist.
# Wenn ja dann mus AI Zug auch noch in dieser Funktion ausgeführt werden
