import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

from ui.ui_game import Game


class Menu:

    def __init__(self):
        self.gui = tk.Tk(className="Chess")
        # When buttons use width/height and have a text in it => size in chars (1*char = 8px)
        # When it uses a picture => size in pixels
        self.frame1 = tk.Frame(self.gui, width=200, height=30)
        self.frame2 = tk.Frame(self.gui, width=200, height=30)
        self.game_button = tk.Button(self.frame1, text="Start game", command=self.start_game)
        self.aigame_button = tk.Button(self.frame2, text="Start game against AI", command=self.start_game_ai)
        self.image = Image.open("pictures/chess.png")
        self.image = self.image.resize((80, 80), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image=self.image)
        self.label1 = tk.Label(self.gui, image=self.image, width=80, height=80)
        self.label2 = tk.Label(self.gui, text="Chess", width=9, height=2)

    def start_gui(self):
        # set gui icon
        self.gui.geometry('%dx%d+%d+%d' % (400, 250, 600, 50))
        self.gui.resizable(False, False)
        img = ""
        if os.path.isfile("pictures/chess.png"):
            img = tk.Image("photo", file="pictures/chess.png")
        self.gui.tk.call('wm', 'iconphoto', self.gui.w, img)
        # set gui title
        self.gui.title("Chess")
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
        game = Game(mode=0)
        game.gui.after(0, self.gui.destroy())
        game.start_game()

    def start_game_ai(self):
        game = Game(mode=1)
        game.gui.after(0, self.gui.destroy())
        game.start_game()

    def start_game_both_ai(self):
        game = Game(mode=2)
        game.gui.after(0, self.gui.destroy())
        game.start_game()
