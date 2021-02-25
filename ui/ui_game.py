import tkinter as tk
import random
import copy
from tkinter import BOTH

from game.logic import GameLogic


class Game:

    def __init__(self, mode: int):

        # mode: 0 = Player vs Player, 1 = Player vs AI, 2 = AI vs AI
        self.mode = mode
        self.gui = tk.Tk(className="Game")
        self.game = GameLogic(self, random.randint(1, 2))

        # gui elements
        self.frames = []
        self.tiles = []
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="white"))
                    else:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="#B47D49"))
                else:
                    if j % 2 == 1:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="white"))
                    else:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="#B47D49"))

    def start_game(self):
        self.gui.title("Chess")
        self.gui.geometry('%dx%d+%d+%d' % (800, 800, 600, 125))
        self.gui.resizable(False, False)
        for i in range(8):
            for j in range(8):
                self.frames[8*i+j].pack()
                self.frames[8*i+j].place(x=i*100, y=j*100)
                self.tiles[8*i+j].pack(fill=BOTH, expand=True)
                self.tiles[8 * i + j].place(x=0, y=0, width=100, height=100)
        # If mode = 2, then 2 AI are batteling each other, so we dont click anywhere
        if self.mode == 2:
            self.gui.after(0, self.game.run_game_multiple_ai)
        self.gui.mainloop()
        pass

# Am Ende der Funktion die bei draufdrücken auf Feld passiert muss noch gechecked werden ob AI dran ist.
# Wenn ja dann mus AI Zug auch noch in dieser Funktion ausgeführt werden
