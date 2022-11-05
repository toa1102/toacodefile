from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import time
from webbrowser import get

from click import command
from pyrsistent import s
point = 500
timer = 0
root = Tk()
root.title('My First App')
nomber1 = random.randint(1,9)
nomber2 = random.randint(1,9)
nomber3 = random.randint(1,9)
goukei = nomber1 + nomber2 + nomber3
# ウィジェットの作成
time_sta = time.time()
frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text=(str(nomber1) + ' + ' + str(nomber2) + ' + ' + str(nomber3) + '答え:'))
time_end = time.time()
tim = time_sta + time_end
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print('Hello, %s.' % t.get()))
# レイアウト
frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)
# ウィンドウの表示開始
root.mainloop()
print('score : ' + str(round(point, 2)))
root = tk.Tk()
root.geometry('200x55')

label = tk.Label(root, text='テキスト')
label.pack()

root.mainloop()

#if %s == goukei and tim <= 1.5:
#    command=lambda: print('excellent!!')
#    point = point
#    command=lambda: print(round(tim, 1))
#elif %s == goukei and tim <= 5:
#    command=lambda: print('true')
#    point = point - round(tim, 1)
#    command=lambda: print(round(tim, 1))
#else:
#    command=lambda: print('fail')
#    point = point - 100 - round(tim, 1)
#    command=lambda: print(round(tim, 1))
#
#command=lambda: print('excellent!!')