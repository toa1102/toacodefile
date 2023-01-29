import tkinter as tk
import random

root = tk.Tk()
root.geometry('200x55')

label = tk.Label(root, text='おみくじbot')
label.pack()

omikuji = random.randint()