import random
#前書き
print('')
kotoba = input('ブラックジャックゲーム')
print('enterで実行')
print('')
# ダイヤ・スペード・ハート・クローバー
#   D   ,   s    ,   H   ,    c
kad1 = ['♦ ','♠ ','♥ ','☘ ']
kad2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
kad3 = [1,2,3,4,5,6,7,8,9,10,10,10,10]
numbr1h = random.randint(0,12)
numbr2h = random.randint(0,12)
numbr3h = random.randint(0,12)
numbr4h = random.randint(0,12)
numbr1 = random.randint(0,3)
numbr2 = random.randint(0,3)
numbr3 = random.randint(0,3)
numbr4 = random.randint(0,3)
comnumbr1h = random.randint(0,12)
comnumbr2h = random.randint(0,12)
comnumbr3h = random.randint(0,12)
comnumbr4h = random.randint(0,12)
comnumbr1 = random.randint(0,3)
comnumbr2 = random.randint(0,3)
comnumbr3 = random.randint(0,3)
comnumbr4 = random.randint(0,3)
#1枚は表示，1枚は＊で表示
print('あなたのカードは' + str(kad1[numbr1]) + str(kad2[numbr1h]) + 'と' + str(kad1[numbr2]) + str(kad2[numbr2h]) + 'です。')
print('ディーラーのカードは' + str(kad1[comnumbr1]) + str(kad2[comnumbr1h]) + 'と' + '＊' + 'です。')
player1 = kad3[numbr1h] + kad3[numbr2h]
player2 = player1 + kad3[numbr3h]
player3 = player2 + kad3[numbr4h]
com2x = kad3[comnumbr1h] + kad3[comnumbr2h]
com3x = com2x + kad3[comnumbr3h]
com4x = com3x + kad3[comnumbr4h]
yesNo = input('カードを引きますか？ yes or No:')
dkad2p = str(kad1[comnumbr1]) + str(kad2[comnumbr1h]) + 'と' + str(kad1[comnumbr2]) + str(kad2[comnumbr2h])
dcad3p = dkad2p + 'と' + str(kad1[comnumbr3]) + str(kad2[comnumbr3h])
dcad4p = dcad3p + 'と' + str(kad1[comnumbr4]) + str(kad2[comnumbr4h])
if yesNo == 'yes':
    print('あなたのカードは' + str(kad1[numbr1]) + str(kad2[numbr1h]) + 'と' + str(kad1[numbr2]) + str(kad2[numbr2h]) + 'と' + str(kad1[numbr3]) + str(kad2[numbr3h]) + 'です。')
    yesNo = input('カードを引きますか？ yes or No:')
    if yesNo == 'yes':
        print('あなたのカードは' + dcad4p + 'でした。')
        if com2x >= 16:
            comxx1 = 'ディーラーのカードの合計は' + dkad2p + 'でした。'
            print(comxx1)
            if player3 <= 15 or player3 >= 22:
                print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです。')
            elif com2x >= 22:
                print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
            elif player3 >= com2x + 1:
                print('おめでとうございます！')
                print('あなたの勝ちです!!!')
            elif com4x <= com2x:
                print('残念…。')
                print('あなたの負けです')
            else:
                print('申し訳ございません。')
                print('再度実行をお願い致します。')
        elif com2x <= 16:
            if com3x >= 17:
                comxx1 = 'ディーラーのカードは' + dcad3p + 'でした。'
                print(comxx1)
                if player3 <= 15 or player3 >= 22:
                    print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
                elif com2x >= 22:
                    print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
                elif player3 >= com2x + 1:
                    print('おめでとうございます！')
                    print('あなたの勝ちです!!!')
                elif com4x <= com2x:
                    print('残念…。')
                    print('あなたの負けです')
                else:
                    print('申し訳ございません。')
                    print('再度実行をお願い致します。')
            elif com3x <= 16:
                comxx1 = 'ディーラーのカードは' + dcad4p + 'でした。'
                print(comxx1)
                if player3 <= 15 or player3 >= 22:
                    print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
                elif com2x >= 22:
                    print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
                elif player3 >= com2x + 1:
                    print('おめでとうございます！')
                    print('あなたの勝ちです!!!')
                elif com4x <= com2x:
                    print('残念…。')
                    print('あなたの負けです')
                else:
                    print('申し訳ございません。')
                    print('再度実行をお願い致します。')
    elif yesNo == 'No' or yesNo == 'no':
        if com2x >= 16:
            comxx1 = 'ディーラーのカードは' + dkad2p + 'でした。'
            print(comxx1)
            if player3 <= 15 or player3 >= 22:
            print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
            elif com2x >= 22:
                print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
            elif player3 >= com2x + 1:
                print('おめでとうございます！')
                print('あなたの勝ちです!!!')
            elif com4x <= com2x:
                print('残念…。')
                print('あなたの負けです')
            else:
                print('申し訳ございません。')
                print('再度実行をお願い致します。')
        elif com2x <= 16:
            if com3x >= 17:
                comxx1 = 'ディーラーのカードは' + dcad3p + 'でした。'
            if player3 <= 15 or player3 >= 22:
                print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
            elif com2x >= 22:
                print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
            elif player3 >= com2x + 1:
                print('おめでとうございます！')
                print('あなたの勝ちです!!!')
            elif com4x <= com2x:
                print('残念…。')
                print('あなたの負けです')
            else:
                print('申し訳ございません。')
                print('再度実行をお願い致します。')
        elif com3x <= 16:
            comxx1 = 'ディーラーのカードは' + dcad4p + 'でした'
            if player3 <= 15 or player3 >= 22:
                print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
            elif com2x >= 22:
                print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
            elif player3 >= com2x + 1:
                print('おめでとうございます！')
                print('あなたの勝ちです!!!')
            elif com4x <= com2x:
                print('残念…。')
                print('あなたの負けです')
            else:
                print('申し訳ございません。')
                print('再度実行をお願い致します。')
                print(comxx1)
    else:
        print('申し訳ございません。')
        print('再度実行をお願い致します。')
elif yesNo == 'No' or yesNo == 'no':
    #comxx1代入
    if com2x >= 16:
        comxx1 = 'ディーラーのカードは' + dkad2p + 'でした。'
        print(comxx1)
        if player3 <= 15 or player3 >= 22:
            print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
        elif com2x >= 22:
            print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
        elif player3 >= com2x + 1:
            print('おめでとうございます！')
            print('あなたの勝ちです!!!')
        elif com4x <= com2x:
            print('残念…。')
            print('あなたの負けです')
        else:
            print('申し訳ございません。')
            print('再度実行をお願い致します。')
    elif com2x <= 16:
        if com3x >= 17:
            comxx1 = 'ディーラーのカードは' + dcad3p + 'でした。'
            if player3 <= 15 or player3 >= 22:
                print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
            elif com2x >= 22:
                print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
            elif player3 >= com2x + 1:
                print('おめでとうございます！')
                print('あなたの勝ちです!!!')
            elif com4x <= com2x:
                print('残念…。')
                print('あなたの負けです')
            else:
                print('申し訳ございません。')
                print('再度実行をお願い致します。')
        elif com3x <= 16:
            comxx1 = 'ディーラーのカードは' + dcad4p + 'でした'
            if player3 <= 15 or player3 >= 22:
                print('あなたのカードの合計は' + player3 + 'なため、あなたの負けです')
            elif com2x >= 22:
                print('ディーラーのカードの合計は21より大きいのであなたの勝ちです!!!')
            elif player3 >= com2x + 1:
                print('おめでとうございます！')
                print('あなたの勝ちです!!!')
            elif com4x <= com2x:
                print('残念…。')
                print('あなたの負けです')
            else:
                print('申し訳ございません。')
                print('再度実行をお願い致します。')
else:
    print('申し訳ございません。')
    print('再度実行をお願い致します。')