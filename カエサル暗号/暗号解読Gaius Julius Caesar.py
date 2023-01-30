import tkinter as tk

# メインウィンドウを作成
baseGround = tk.Tk()
# ウィンドウのサイズを設定
baseGround.geometry('500x300')
# 画面タイトル
baseGround.title('暗号解読Gaius Julius Caesar')
# ラベル
label2 = tk.Label(text='暗号を入力')
label2.place(x=30, y=90)
# テキストボックス
textBox2 = tk.Entry()
textBox2.place(x=30, y=120)
point=500
def val():
    kazu = 0
    for i in range(26):
        moji = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        anngoubunn = ''
        x = {'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51}
        bunn = textBox2.get()
        a = -1
        print(kazu)
        for i in range(len(bunn)):
            a = a + 1
            z = x[bunn[a]]
            anngoubunn = str(anngoubunn) + str(moji[z - kazu])
        kazu = kazu + 1
        print(anngoubunn)
# ボタンの作成と配置
button = tk.Button(baseGround,
                text = 'OK',
                # クリック時にval()関数を呼ぶ
                command = val
                ).place(x=30, y=180)
baseGround.mainloop()