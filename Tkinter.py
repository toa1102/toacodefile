import tkinter as tk

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
label1 = tk.Label(text='ユーザー名')
label1.place(x=30, y=40)
label2 = tk.Label(text='パスワード')
label2.place(x=30, y=90)
# テキストボックス
textBox1 = tk.Entry(width=40)
textBox1.place(x=30, y=60)
textBox2 = tk.Entry()
textBox2.place(x=30, y=120)
point=500
def val():
    # テキストボックスの値を取得
    if textBox1.get() == 'toa1102' and textBox2.get() == 'toatoatoa2':
        print('ok')
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
