import random
print('ミニバトルを始めます')
a = input('名前を入力してください : ')
print(a + 'さんこんにちは')
print('-----------------------------------------------')
print('スライムが1匹現れた❕❕')
print('手持ちHPは3です')
aa = int(input('0~5までの好きな数字を入力してください'))
aaa = random.randint(0, 5)
if aaa == aa:
    print('クリティカルヒット❕❕')
else:
    print('ダメージ1')
    print('残りHPは2です')
    aa = int(input('0~5までの好きな数字を入力してください'))
    aaa = random.randint(0, 5)
    if aaa == aa:
        print('クリティカルヒット❕❕')
    else:
        print('ダメージ1')
        print('残りHPは1です')
        aa = int(input('0~5までの好きな数字を入力してください'))
        aaa = random.randint(0, 5)
        if aaa == aa:
            print('クリティカルヒット❕❕')
        else:
            print('負け')
aaaa = int(input('終わりです　1と入力してください'))