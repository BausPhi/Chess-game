import tkinter as tk
import random

from PIL import Image, ImageTk
from tkinter import BOTH
from game.logic import GameLogic


class Game:

    def __init__(self, mode: int):

        # mode: 0 = Player vs Player, 1 = Player vs AI, 2 = AI vs AI
        self.mode = mode
        self.gui = tk.Toplevel()
        self.game = GameLogic(self, random.randint(1, 2))
        self.images = {}
        for pic in ["king", "queen", "bishop", "knight", "rook", "pawn", "king_w", "queen_w", "bishop_w", "knight_w",
                    "rook_w", "pawn_w"]:
            image = Image.open("pictures/" + pic + ".png")
            if pic == "pawn" or pic == "pawn_w":
                image = image.resize((60, 60), Image.ANTIALIAS)
            elif pic == "king" or pic == "king_w" or pic == "queen" or pic == "queen_w":
                image = image.resize((90, 90), Image.ANTIALIAS)
            else:
                image = image.resize((80, 80), Image.ANTIALIAS)
            self.images[pic] = ImageTk.PhotoImage(image=image)

        # gui elements
        self.frames = []
        self.tiles = []
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="grey"))
                    else:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="#B47D49"))
                else:
                    if j % 2 == 1:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="grey"))
                    else:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append(tk.Label(self.frames[8*i+j], bg="#B47D49"))

    def start_game(self):
        self.gui.title("Chess")
        self.gui.geometry('%dx%d+%d+%d' % (800, 800, 600, 125))
        self.gui.resizable(False, False)
        for i in range(8):
            for j in range(8):
                self.frames[8*j+i].pack()
                self.frames[8*j+i].place(x=i*100, y=j*100)
                self.tiles[8*j+i].pack(fill=BOTH, expand=True)
                self.tiles[8*j+i].place(x=0, y=0, width=100, height=100)
                if i == 1:
                    self.tiles[8*i+j].config(image=self.images['pawn'])
                if i == 6:
                    self.tiles[8 * i + j].config(image=self.images['pawn_w'])
                if i == 0:
                    if j == 0 or j == 7:
                        self.tiles[8 * i + j].config(image=self.images['rook'])
                    if j == 1 or j == 6:
                        self.tiles[8 * i + j].config(image=self.images['knight'])
                    if j == 2 or j == 5:
                        self.tiles[8 * i + j].config(image=self.images['bishop'])
                    if j == 3:
                        self.tiles[8 * i + j].config(image=self.images['king'])
                    if j == 4:
                        self.tiles[8 * i + j].config(image=self.images['queen'])
                if i == 7:
                    if j == 0 or j == 7:
                        self.tiles[8 * i + j].config(image=self.images['rook_w'])
                    if j == 1 or j == 6:
                        self.tiles[8 * i + j].config(image=self.images['knight_w'])
                    if j == 2 or j == 5:
                        self.tiles[8 * i + j].config(image=self.images['bishop_w'])
                    if j == 3:
                        self.tiles[8 * i + j].config(image=self.images['king_w'])
                    if j == 4:
                        self.tiles[8 * i + j].config(image=self.images['queen_w'])
        # If mode = 2, then 2 AI are batteling each other, so we dont click anywhere
        if self.mode == 2:
            self.gui.after(0, self.game.run_game_multiple_ai)
        self.gui.mainloop()
        pass

# Am Ende der Funktion die bei draufdrücken auf Feld passiert muss noch gechecked werden ob AI dran ist.
# Wenn ja dann mus AI Zug auch noch in dieser Funktion ausgeführt werden
