import random
from playsound import playsound
print()
koment = input('勇者の冒険')
print()
name1 = input('あなたの名前を入力してください')
print()
koment = input('エピローグ')
print()
koment = input('ある日．．．。')
koment = input(name1 + '    あー　ヤバい！　ｋバーガーでハンバーガー間違えて１０個買っちゃった！')
koment = input(name1 + '    １個で良かったのに．．．。')
koment = input(name1 + '    お隣さんにあげよう')
koment = input(name1 + '    （お隣さんの家に着いた）')
koment = input(name1 + '    すみませーん！')
koment = input(name1 + '    あれ？朝はいるはずなのに．．．。')
koment = input(name1 + '    （ん？なんか落ちているぞ）')
koment = input('「この家の者はkeisuke城に拉致されている」')
koment = input(name1 + '    大変だ！　助けに行かなきゃ！！！')
koment = input(name1 + '    ふう。やっと着いた')

koment = input('城の門番　スライムが現れた。')
koment = input('戦闘開始!')
print('何をだしますか？')
aaa = int(input('1:サーベル　2:刀'))
if aaa == random.randint(1,2):
    playsound("剣で斬る3.mp3")
    koment = input(name1 + '    クリティカルヒット！')
    koment = input(name1 + '    あなたの勝ちです！')
else:
    koment = input(name1 + '    外れ')
    print('何をしますか？')
    aaa = int(input('1:盾を出す2:よける'))
    if aaa == random.randint(1,2):
        print('防御成功')
        print('何をだしますか？')
        aaa = int(input('1:サーベル　2:刀'))
        if aaa == random.randint(1,2):
            playsound("剣で斬る3.mp3")
            koment = input(name1 + '    クリティカルヒット！')
            koment = input(name1 + '    あなたの勝ちです！')
        else:
            koment = input(name1 + '    外れ')
            print('何をしますか？')
            aaa = int(input('1:盾を出す2:よける'))
            if aaa <= 1:
                print('防御成功')
                print('何をだしますか？')
                aaa = int(input('1:サーベル　2:刀'))
                if aaa <= 1:
                    koment = input(name1 + '    クリティカルヒット！')
                    koment = input(name1 + '    あなたの勝ちです！')
    else:
        print('防御失敗')
        print('何をだしますか？')
        aaa = int(input('1:サーベル　2:刀'))
        if aaa == random.randint(1,2):
            koment = input(name1 + '    クリティカルヒット！')
            koment = input(name1 + '    あなたの勝ちです！')
        else:
            koment = input(name1 + '    外れ')
            print('何をしますか？')
            aaa = int(input('1:盾を出す2:よける'))
            if aaa <= 1:
                print('防御成功')
                print('何をだしますか？')
                aaa = int(input('1:サーベル　2:刀'))
                if aaa <= 1:
                    playsound("剣で斬る3.mp3")
                    koment = input(name1 + '    クリティカルヒット！')
                    koment = input(name1 + '    あなたの勝ちです！')

koment = input(name1 + '    ')
koment = input(name1 + '    ')
koment = input(name1 + '    ')
koment = input(name1 + '    ')
koment = input(name1 + '    ')
