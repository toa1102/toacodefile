import tkinter as tk
import random
math1 = random.randint(1,9)
math2 = random.randint(1,9)
math3 = random.randint(1,9)
math4 = random.randint(1,9)
math5 = random.randint(1,9)
math6 = random.randint(1,9)
math7 = random.randint(1,9)
math8 = random.randint(1,9)
math9 = random.randint(1,9)
math10 = random.randint(1,9)

root = tk.Tk()
root.geometry('200x55')

label = tk.Label(root, text='ユーザー名とパスワードを入力')
label.pack()

root.mainloop()

# メインウィンドウを作成
baseGround = tk.Tk()
# ウィンドウのサイズを設定
baseGround.geometry('500x300')
# 画面タイトル
baseGround.title('テキストボックスの値を取得する')
# ラベル
label1 = tk.Label(text=str(math1) + '+' + str(math2))
label1.place(x=30, y=40)
label2 = tk.Label(text=str(math1) + '+' + str(math2))
label2.place(x=30, y=40)
label3 = tk.Label(text=str(math1) + '+' + str(math2))
label3.place(x=30, y=40)
label4 = tk.Label(text=str(math1) + '+' + str(math2))
label4.place(x=30, y=40)
label5 = tk.Label(text=str(math1) + '+' + str(math2))
label5.place(x=30, y=40)
# テキストボックス
textBox1 = tk.Entry(width=40)
textBox1.place(x=30, y=60)
textBox2 = tk.Entry()
textBox2.place(x=30, y=60)
textBox3 = tk.Entry()
textBox3.place(x=30, y=60)
textBox4 = tk.Entry()
textBox4.place(x=30, y=60)
textBox5 = tk.Entry()
textBox5.place(x=30, y=60)
point=500
def val():
    # テキストボックスの値を取得
    if textBox1.get() == str(math1 + math2) and textBox1.get() == str(math3 + math4) and textBox2.get() == str(math5 + math6) and textBox3.get() == str(math1 + math2) and textBox4.get() == str(math7 + math8) and textBox5.get() == str(math9 + math10):
        print('100')
    elif textBox1.get() == str(math1 + math2) and textBox1.get() == str(math3 + math4) and textBox2.get() == str(math5 + math6) and textBox4.get() == str(math1 + math2) and textBox5.get() == str(math7 + math8):
        print('80')
    elif textBox1.get() == str(math1 + math2) and textBox1.get() == str(math3 + math4) and textBox2.get() == str(math5 + math6) and textBox4.get() == str(math1 + math2) and textBox5.get() == str(math9 + math10):
        print('80')
    elif textBox1.get() == str(math1 + math2) and textBox1.get() == str(math3 + math4) and textBox2.get() == str(math5 + math6) and textBox4.get() == str(math1 + math2) and textBox5.get() == str(math7 + math8) and textBox5.get() == str(math9 + math10):
        print('80')
    elif textBox1.get() == str(math1 + math2) and textBox1.get() == str(math3 + math4) and textBox2.get() == str(math5 + math6) and textBox4.get() == str(math1 + math2) and textBox5.get() == str(math7 + math8) and textBox5.get() == str(math9 + math10):
        print('80')
    elif textBox1.get() == str(math1 + math2) and textBox1.get() == str(math3 + math4) and textBox2.get() == str(math5 + math6) and textBox4.get() == str(math1 + math2) and textBox5.get() == str(math7 + math8) and textBox5.get() == str(math9 + math10):
        print('80')

    else:
        print('NO')
# ボタンの作成と配置
button = tk.Button(baseGround,
                text = 'OK',
                # クリック時にval()関数を呼ぶ
                command = val
                ).place(x=30, y=180)
baseGround.mainloop()


#if textBox1.get() == 'toa1102' and textBox2.get() == 'toatoatoa2':
#    root = tk.Tk()
#    root.geometry('200x55')
#
#    label = tk.Label(root, text='excellent!!')
#    label.pack()
#
#    root.mainloop()
#elif textBox1.get() == 'toa1102':
#    root = tk.Tk()
#    root.geometry('200x55')
#
#    label = tk.Label(root, text='true')
#    label.pack()
#
#    root.mainloop()
#else:
#    root = tk.Tk()
#    root.geometry('200x55')
#
#    label = tk.Label(root, text='fail')
#    label.pack()
#
#    root.mainloop()
