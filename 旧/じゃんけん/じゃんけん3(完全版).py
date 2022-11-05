import random
from じゃんけん2 import jyanken
print('')
print('じゃんけんゲーム')
print('')
print('-----------------------------------------------')
hazimari = input('enterでスタート')
# 名前
print('第2戦')
print('じゃんけんゲームへようこそ!!')
name = input('名前を入力してください : ')
print(name + 'さんこんにちは')
print('このゲームは勝つまで終われません')
print('-----------------------------------------------')
print('じゃんけんをするよ')
print('')

#繰り返し処理
katikamake = int(input('負け・あいこの場合は1と、勝ちの場合は0と入力してください。'))
while katikamake == 1:
    jyanken()
    katikamake2 = int(input('負け・あいこの場合は1と、勝ちの場合は0と入力してください。'))
    if katikamake2 == 0:
        katikamake = 0
print('')
print('おめでとうございます!!')
print('あなたはコンピューターに勝ちました!!')
print('')

owari = input('終わりですenterを押してください')
