# importing modules
import tkinter
import random

# importing sub-modules
from random import randint
from tkinter import *
from PIL import Image, ImageTk

# app logic
# rolling function
def roll_dice():
	# variables
	# picking random number
	roll = random.randint(0, 5)

	# app conditions
	if roll == 0:
		dice.config(image=img1)
	elif roll == 1:
		dice.config(image=img2)
	elif roll == 2:
		dice.config(image=img3)
	elif roll == 3:
		dice.config(image=img4)
	elif roll == 4:
		dice.config(image=img5)
	elif roll == 5:
		dice.config(image=img6)

# variables
__version__ = str("v1.0")

# constantes
TITLE = str("Dice")

# creating main window
# settings for main window
root = Tk()
root.title(f"{TITLE}")
root.resizable(False, False)

# importing images of dices
imgd1 = Image.open("static/1.png")
img1 = ImageTk.PhotoImage(imgd1)

imgd2 = Image.open("static/2.png")
img2 = ImageTk.PhotoImage(imgd2)

imgd3 = Image.open("static/3.png")
img3 = ImageTk.PhotoImage(imgd3)

imgd4 = Image.open("static/4.png")
img4 = ImageTk.PhotoImage(imgd4)

imgd5 = Image.open("static/5.png")
img5 = ImageTk.PhotoImage(imgd5)

imgd6 = Image.open("static/6.png")
img6 = ImageTk.PhotoImage(imgd6)

# creating dice button
dice = Button(root, image=img1, relief=FLAT, command=roll_dice)
dice.pack()

# starting the app
root.mainloop()
