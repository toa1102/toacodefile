import random
#名前
a = input('名前を入力してください : ')
print(a + 'さんこんにちは')
print('このゲームは勝つまで終われません')
print('-----------------------------------------------')
print('じゃんけんゲームへようこそ❕❕')
print('じゃんけんをするよ')
#ゲストに出す手を決めてもらう
print('何を出しますか❓(0:グー,1:チョキ,2:パー)')
aa = int(input('数字で入力してください : '))
#コンピューターの出す手を決める
aaa = random.randint(0, 2)
#↓引き分けバージョン↓
if aaa == 0 and aa == 0:
    print(a + 'の手はグーです。')
    print('コンピューターの手はグーです。')
    print('引き分け　　1ポイント')
elif aaa == 1 and aa == 1:
    print(a + 'の手はチョキです。')
    print('コンピューターの手はチョキです。')
    print('引き分け　　1ポイント')
elif aaa == 2 and aa == 2:
    print(a + 'の手はパーです。')
    print('コンピューターの手はパーです。')
    print('引き分け　　1ポイント')
#↓負けバージョン↓
elif aaa == 0 and aa == 1:
    print(a + 'の手はチョキです。')
    print('コンピューターの手はグーです。')
    print('負け　　0ポイント')
elif aaa == 1 and aa == 2:
    print(a + 'の手はパーです。')
    print('コンピューターの手はチョキです。')
    print('負け　　0ポイント')
elif aaa == 2 and aa == 0:
    print(a + 'の手はグーです。')
    print('コンピューターの手はパーです。')
    print('負け　　0ポイント')
#↓勝ちバージョン↓
elif aaa == 1 and aa == 0:
    print(a + 'の手はパーです。')
    print('コンピューターの手はグーです。')
    print('勝ち　　3ポイント')
elif aaa == 2 and aa == 1:
    print(a + 'の手はチョキです。')
    print('コンピューターの手はパーです。')
    print('勝ち　　3ポイント')
elif aaa == 0 and aa == 2:
    print(a + 'の手はパーです。')
    print('コンピューターの手はグーです。')
    print('勝ち　　3ポイント')
else:
    print('')
aaaa = int(input('もし【負け・あいこ】は1と入力してください'))
if aaaa == 1:
    #ゲストに出す手を決めてもらう
    print('何を出しますか❓(0:グー,1:チョキ,2:パー)')
    aa = int(input('数字で入力してください : '))
    #コンピューターの出す手を決める
    aaa = random.randint(0, 2)
    #↓引き分けバージョン↓
    if aaa == 0 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はグーです。')
        print('引き分け　　1ポイント')
    elif aaa == 1 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はチョキです。')
        print('引き分け　　1ポイント')
    elif aaa == 2 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はパーです。')
        print('引き分け　　1ポイント')
    #↓負けバージョン↓
    elif aaa == 0 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はグーです。')
        print('負け　　0ポイント')
    elif aaa == 1 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はチョキです。')
        print('負け　　0ポイント')
    elif aaa == 2 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はパーです。')
        print('負け　　0ポイント')
    #↓勝ちバージョン↓
    elif aaa == 1 and aa == 0:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    elif aaa == 2 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はパーです。')
        print('勝ち　　3ポイント')
    elif aaa == 0 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    else:
        print('')
else:
    print('')
aaaa = int(input('もし【負け・あいこ】は1と入力してください'))
if aaaa == 1:
    #ゲストに出す手を決めてもらう
    print('何を出しますか❓(0:グー,1:チョキ,2:パー)')
    aa = int(input('数字で入力してください : '))
    #コンピューターの出す手を決める
    aaa = random.randint(0, 2)
    #↓引き分けバージョン↓
    if aaa == 0 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はグーです。')
        print('引き分け　　1ポイント')
    elif aaa == 1 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はチョキです。')
        print('引き分け　　1ポイント')
    elif aaa == 2 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はパーです。')
        print('引き分け　　1ポイント')
    #↓負けバージョン↓
    elif aaa == 0 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はグーです。')
        print('負け　　0ポイント')
    elif aaa == 1 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はチョキです。')
        print('負け　　0ポイント')
    elif aaa == 2 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はパーです。')
        print('負け　　0ポイント')
    #↓勝ちバージョン↓
    elif aaa == 1 and aa == 0:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    elif aaa == 2 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はパーです。')
        print('勝ち　　3ポイント')
    elif aaa == 0 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    else:
        print('')
else:
    print('')
aaaa = int(input('もし【負け・あいこ】は1と入力してください'))
if aaaa == 1:
    #ゲストに出す手を決めてもらう
    print('何を出しますか❓(0:グー,1:チョキ,2:パー)')
    aa = int(input('数字で入力してください : '))
    #コンピューターの出す手を決める
    aaa = random.randint(0, 2)
    #↓引き分けバージョン↓
    if aaa == 0 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はグーです。')
        print('引き分け　　1ポイント')
    elif aaa == 1 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はチョキです。')
        print('引き分け　　1ポイント')
    elif aaa == 2 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はパーです。')
        print('引き分け　　1ポイント')
    #↓負けバージョン↓
    elif aaa == 0 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はグーです。')
        print('負け　　0ポイント')
    elif aaa == 1 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はチョキです。')
        print('負け　　0ポイント')
    elif aaa == 2 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はパーです。')
        print('負け　　0ポイント')
    #↓勝ちバージョン↓
    elif aaa == 1 and aa == 0:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    elif aaa == 2 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はパーです。')
        print('勝ち　　3ポイント')
    elif aaa == 0 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    else:
        print('')
else:
    print('')
aaaa = int(input('もし【負け・あいこ】は1と入力してください'))
if aaaa == 1:
    #ゲストに出す手を決めてもらう
    print('何を出しますか❓(0:グー,1:チョキ,2:パー)')
    aa = int(input('数字で入力してください : '))
    #コンピューターの出す手を決める
    aaa = random.randint(0, 2)
    #↓引き分けバージョン↓
    if aaa == 0 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はグーです。')
        print('引き分け　　1ポイント')
    elif aaa == 1 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はチョキです。')
        print('引き分け　　1ポイント')
    elif aaa == 2 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はパーです。')
        print('引き分け　　1ポイント')
    #↓負けバージョン↓
    elif aaa == 0 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はグーです。')
        print('負け　　0ポイント')
    elif aaa == 1 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はチョキです。')
        print('負け　　0ポイント')
    elif aaa == 2 and aa == 0:
        print(a + 'の手はグーです。')
        print('コンピューターの手はパーです。')
        print('負け　　0ポイント')
    #↓勝ちバージョン↓
    elif aaa == 1 and aa == 0:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    elif aaa == 2 and aa == 1:
        print(a + 'の手はチョキです。')
        print('コンピューターの手はパーです。')
        print('勝ち　　3ポイント')
    elif aaa == 0 and aa == 2:
        print(a + 'の手はパーです。')
        print('コンピューターの手はグーです。')
        print('勝ち　　3ポイント')
    else:
        print('')
else:
    print('')
