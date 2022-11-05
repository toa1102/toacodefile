import random
print('')
print('じゃんけんゲーム')
print('')
hazimari = input('enterでスタート')
#名前
name = input('名前を入力してください : ')
print(name + 'さんこんにちは')
print('このゲームは勝つまで終われません')
print('-----------------------------------------------')
print('じゃんけんゲームへようこそ!!')
print('じゃんけんをするよ')
def jyanken():
    gest = int(input('何を出しますか❓(0:グー，1:チョキ，2:パー)'))
    com = random.randint(0,2)
    #ゲストに出す手を決めてもらう
    #↓引き分けバージョン↓
    if gest == com:
        if gest == 0:
            print(name + 'の手はグーです。')
            print('コンピューターの手はグーです。')
            print('引き分け　　1ポイント')
        elif gest == 1:
            print(name + 'の手はチョキです。')
            print('コンピューターの手はチョキです。')
            print('引き分け　　1ポイント')
        elif gest == 2:
            print(name + 'の手はパーです。')
            print('コンピューターの手はパーです。')
            print('引き分け　　1ポイント')
        else:
            print('エラーです')
    #↓負けバージョン↓
    elif gest - 1 == com:
        if com == 0:
            print(name + 'の手はチョキです。')
            print('コンピューターの手はグーです。')
            print('負け　　0ポイント')
        elif com == 1:
            print(name + 'の手はパーです。')
            print('コンピューターの手はチョキです。')
            print('負け　　0ポイント')
        else:
            print('判定できません')
    elif gest + 2 == com:
            print(name + 'の手はグーです。')
            print('コンピューターの手はパーです。')
            print('負け　　0ポイント')
    #↓勝ちバージョン↓
    elif gest + 1 == com:
        if gest == 0:
            print(name + 'の手はパーです。')
            print('コンピューターの手はグーです。')
            print('勝ち　　3ポイント')
        elif gest == 1:
            print(name + 'の手はチョキです。')
            print('コンピューターの手はパーです。')
            print('勝ち　　3ポイント')
        else:
            print('判定できません')
    elif gest - 2 == com:
        print(name + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    else:
        print('判定できません')
jyanken()

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
