import random
import tkinter as tk

# メインウィンドウを作成
baseGround = tk.Tk()
# ウィンドウのサイズを設定
baseGround.geometry('500x300')
# 画面タイトル
baseGround.title('暗号解読Gaius Julius Caesar')
# ラベル
label2 = tk.Label(text='原文を入力')
label2.place(x=30, y=90)
# テキストボックス
textBox2 = tk.Entry()
textBox2.place(x=30, y=120)
point=500
def val():
    kazu = random.randint(0,25)
    moji = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    anngoubunn = ''
    x = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    bunn = textBox2.get()
    a = -1
    print(kazu)
    for i in range(len(bunn)):
        a = a + 1
        z = x[bunn[a]]
        anngoubunn = str(anngoubunn) + str(moji[z + kazu])
    root = tk.Tk()
    root.geometry('200x55')

    label = tk.Label(root, text=anngoubunn)
    label.pack()

    root.mainloop()
# ボタンの作成と配置
button = tk.Button(baseGround,
                text = 'OK',
                # クリック時にval()関数を呼ぶ
                command = val
                ).place(x=30, y=180)
baseGround.mainloop()