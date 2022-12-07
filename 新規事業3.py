import tkinter as tk
import random

root = tk.Tk()
root.geometry('500x300')

label = tk.Label(root, text='数学ゲーム')
label.pack()

root.mainloop()

scor = 100

for i in range(5):
    math1 = random.randint(1,9)
    math2 = random.randint(1,9)
    # メインウィンドウを作成
    baseGround = tk.Tk()
    # ウィンドウのサイズを設定
    baseGround.geometry('500x300')
    # 画面タイトル
    baseGround.title('テキストボックスの値を取得する')
    # ラベル
    label1 = tk.Label(text=str(math1) + '+' + str(math2))
    label1.place(x=30, y=40)
    # テキストボックス
    textBox1 = tk.Entry(width=40)
    textBox1.place(x=30, y=60)
    point=500
    def val():
        # テキストボックスの値を取得
        if textBox1.get() == str(math1 + math2):
            pass

        else:
            scor = scor - 20

    # ボタンの作成と配置
    button = tk.Button(baseGround,
                    text = 'OK',
                    # クリック時にval()関数を呼ぶ
                    command = val
                    ).place(x=30, y=180)
    baseGround.mainloop()
