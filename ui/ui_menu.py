import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

from ui.ui_game import Game


class Menu:

    def __init__(self):
        # Gui
        self.gui = tk.Tk()

        # Frames
        self.frame1 = tk.Frame(self.gui, width=200, height=30)
        self.frame2 = tk.Frame(self.gui, width=200, height=30)

        # Buttons
        self.game_button = tk.Button(self.frame1, text="Start game", command=self.start_game)
        self.aigame_button = tk.Button(self.frame2, text="Start game against AI", command=self.start_game_ai)
        self.two_ai_button = tk.Button(self.frame2, text="Start game AI vs AI", command=self.start_game_ai)

        # Image
        self.image = Image.open("pictures/chess.png")
        self.image = self.image.resize((80, 80), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image=self.image)

        # Labels
        self.label1 = tk.Label(self.gui, image=self.image, width=80, height=80)
        self.label2 = tk.Label(self.gui, text="Chess", width=9, height=2)

        # game gui
        self.game_gui = None

    def start_gui(self):
        # Set gui properties
        self.gui.title("Chess")
        self.gui.geometry('%dx%d+%d+%d' % (400, 275, 760, 300))
        self.gui.resizable(False, False)
        if os.path.isfile("pictures/chess.png") and os.name == "posix":
            img = tk.Image("photo", file="pictures/chess.png")
            self.gui.tk.call('wm', 'iconphoto', self.gui.w, img)

        # set all elements
        self.frame1.pack_propagate(0)
        self.frame1.pack()
        self.frame1.place(x=100, y=160)
        self.game_button.pack(fill=BOTH, expand=1)
        self.frame2.pack_propagate(0)
        self.frame2.pack()
        self.frame2.place(x=100, y=210)
        self.aigame_button.pack(fill=BOTH, expand=1)
        self.label1.pack()
        self.label1.place(x=160, y=50)
        self.label2.pack()
        self.label2.place(x=160, y=10)
        self.gui.mainloop()

    def start_game(self):
        if self.game_gui is None:
            game = Game(mode=0)
            self.game_gui = game
            self.game_button.config(text="Start new game")
            self.aigame_button.config(text="Start new game against AI")
            self.two_ai_button.config(text="Start new game between two AI")
            game.start_game()
        else:
            self.game_gui.gui.destroy()
            game = Game(mode=0)
            self.game_gui = game
            game.start_game()

    def start_game_ai(self):
        if self.game_gui is None:
            game = Game(mode=1)
            self.game_gui = game
            self.game_button.config(text="Start new game")
            self.aigame_button.config(text="Start new game against AI")
            self.two_ai_button.config(text="Start new game between two AI")
            game.start_game()
        else:
            self.game_gui.gui.destroy()
            game = Game(mode=1)
            self.game_gui = game
            game.start_game()

    def start_game_both_ai(self):
        if self.game_gui is None:
            game = Game(mode=2)
            self.game_gui = game
            self.game_button.config(text="Start new game")
            self.aigame_button.config(text="Start new game against AI")
            self.two_ai_button.config(text="Start new game between two AI")
            game.start_game()
        else:
            self.game_gui.gui.destroy()
            game = Game(mode=2)
            self.game_gui = game
            game.start_game()
