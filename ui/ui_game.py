import tkinter as tk
import random

from PIL import Image, ImageTk
from tkinter import BOTH
from game.gamerun import GameRun


class Game:

    def __init__(self, mode: int):

        # mode: 0 = Player vs Player, 1 = Player vs AI, 2 = AI vs AI
        self.mode = mode
        self.gui = tk.Toplevel()
        self.game = GameRun(self, random.randint(1, 2), self.mode)
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
                        self.tiles.append((tk.Label(self.frames[8*i+j], bg="grey"), j, i))
                        self.tiles[8*i+j][0].bind("<Button-1>", self.on_click)
                    else:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append((tk.Label(self.frames[8*i+j], bg="#B47D49"), j, i))
                        self.tiles[8*i+j][0].bind("<Button-1>", self.on_click)
                else:
                    if j % 2 == 1:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append((tk.Label(self.frames[8*i+j], bg="grey"), j, i))
                        self.tiles[8*i+j][0].bind("<Button-1>", self.on_click)
                    else:
                        self.frames.append(tk.Frame(self.gui, width=100, height=100, background="grey"))
                        self.tiles.append((tk.Label(self.frames[8*i+j], bg="#B47D49"), j, i))
                        self.tiles[8*i+j][0].bind("<Button-1>", self.on_click)
        self.turn_frame = tk.Frame(self.gui, width=200, height=50, background="grey")
        if self.game.turn == 2 and mode == 1:
            self.turn_label = tk.Label(self.turn_frame, text="The bot is playing", bd=5, relief="solid")
        elif mode == 2:
            self.turn_label = tk.Label(self.turn_frame, text="The bots are playing against each other", bd=5,
                                       relief="solid")
        else:
            self.turn_label = tk.Label(self.turn_frame, text="Player " + str(self.game.turn) + ", it is your turn",
                                       bd=5, relief="solid")

    def start_game(self):
        self.gui.title("Chess")
        self.gui.geometry('%dx%d+%d+%d' % (800, 900, 600, 75))
        self.gui.resizable(False, False)
        # set all field tiles at the correct position
        for i in range(8):
            for j in range(8):
                self.frames[8*j+i].pack()
                self.frames[8*j+i].place(x=i*100, y=j*100)
                self.tiles[8*j+i][0].pack(fill=BOTH, expand=True)
                self.tiles[8*j+i][0].place(x=0, y=0, width=100, height=100)
                if j == 1:
                    self.tiles[8*j+i][0].config(image=self.images['pawn'])
                if j == 6:
                    self.tiles[8*j+i][0].config(image=self.images['pawn_w'])
                if j == 0:
                    if i == 0 or i == 7:
                        self.tiles[8*j+i][0].config(image=self.images['rook'])
                    if i == 1 or i == 6:
                        self.tiles[8*j+i][0].config(image=self.images['knight'])
                    if i == 2 or i == 5:
                        self.tiles[8*j+i][0].config(image=self.images['bishop'])
                    if i == 3:
                        self.tiles[8*j+i][0].config(image=self.images['king'])
                    if i == 4:
                        self.tiles[8*j+i][0].config(image=self.images['queen'])
                if j == 7:
                    if i == 0 or i == 7:
                        self.tiles[8*j+i][0].config(image=self.images['rook_w'])
                    if i == 1 or i == 6:
                        self.tiles[8*j+i][0].config(image=self.images['knight_w'])
                    if i == 2 or i == 5:
                        self.tiles[8*j+i][0].config(image=self.images['bishop_w'])
                    if i == 3:
                        self.tiles[8*j+i][0].config(image=self.images['king_w'])
                    if i == 4:
                        self.tiles[8*j+i][0].config(image=self.images['queen_w'])
        self.turn_frame.pack()
        self.turn_frame.place(x=300, y=825)
        self.turn_label.pack(fill=BOTH, expand=True)
        self.turn_label.place(x=0, y=0, width=200, height=50)
        # If mode = 2, then 2 AI are batteling each other, so we dont click anywhere
        if self.mode == 2:
            self.gui.after(0, self.game.run_game_multiple_ai)
        self.gui.mainloop()
        pass

    def on_click(self, event):
        status = self.game.execute_move(event.widget, self.tiles)
        # game over
        if status is None:
            return None
        if status is True:
            pass    # finish game
        return status
