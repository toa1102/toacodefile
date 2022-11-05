import random
print('')
hazimari = input('バカラ!!!')
print('')
print('あなたの持ちコインは1000コインです。')
coin = 1000
print('player,draw,banker　どれに賭けますか❓')
katimake = input('p,d,bで答えて下さい')
print('(5),(10),(50),(100)のうち、いくら賭けますか❓')
tip = int(input('数字で入力してください'))
#kadの配布
kad2 = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K', '♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K', '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']
kad3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
numbr1 = random.randint(0,51)
numbr2 = random.randint(1,50)
numbr3 = random.randint(2,49)
comnumbr1 = random.randint(3,48)
comnumbr2 = random.randint(4,47)
comnumbr3 = random.randint(5,46)

kad3numbr2p = kad3[numbr1] + kad3[numbr2]
kad3numbr3p = kad3numbr2p + kad3[numbr3]
kad3comnumbr2p = kad3[comnumbr1] + kad3[comnumbr2]
kad3comnumbr3p = kad3comnumbr2p + kad3[comnumbr3]
print('     ' + kad2[numbr1] + '       ' + kad2[numbr2] + '   |   ' + kad2[comnumbr1] + '       ' + kad2[comnumbr2])
print('        player     |      banker         ')
print('         ' + str(kad3numbr2p)[-1] + '         |         ' + str(kad3comnumbr2p)[-1] + '          ')
#プレイヤー8.9
if int(str(kad3numbr2p)[-1]) == 8 or int(str(kad3numbr2p)[-1]) == 9:
    if int(str(kad3numbr2p)[-1]) == int(str(kad3comnumbr2p)[-1]):
        print('同点です')
        if katimake == 'd':
            print(str(tip) + 'プラスされました!!!')
            print('あなたのコインは' + str(coin + tip) + 'です。')
        else:
            print(str(tip) + '回収されました…。')
            print('あなたのコインは' + str(coin - tip) + 'です。')
    elif int(str(kad3numbr2p)[-1]) >= int(str(kad3comnumbr2p)[-1]):
        print('playerの勝ちです')
        if katimake == 'p':
            print(str(tip) + 'プラスされました!!!')
            print('あなたのコインは' + str(coin + tip) + 'です。')
        else:
            print(str(tip) + '回収されました…。')
            print('あなたのコインは' + str(coin - tip) + 'です。')
    elif int(str(kad3comnumbr2p)[-1]) >= int(str(kad3numbr2p)[-1]):
        print('bankerの勝ちです')
        if katimake == 'b':
            print(str(tip) + 'プラスされました!!!')
            print('あなたのコインは' + str(coin + tip) + 'です。')
        else:
            print(str(tip) + '回収されました…。')
            print('あなたのコインは' + str(coin - tip) + 'です。')
#プレイヤー6.7 and バンカー0.1.2.3.4.5.6.7.8.9.
elif int(str(kad3numbr2p)[-1]) == 6 or int(str(kad3numbr2p)[-1]) == 7:
    if int(str(kad3comnumbr2p)[-1]) <= 5:
        print('bankerのカードの1の位が5より小さいのでもう1枚引きます。')
        print('     ' + kad2[numbr1] + '       ' + kad2[numbr2] + '   |   ' + '   ' + kad2[comnumbr1] + '   ' + kad2[comnumbr2] + '    ' + kad2[comnumbr3])
        print('        player     |      banker         ')
        print('         ' + str(kad3numbr3p)[-1] + '         |         ' + str(kad3comnumbr3p)[-1] + '          ')
        if int(str(kad3numbr2p)[-1]) >= int(str(kad3comnumbr3p)[-1]):
            print(str(tip) + 'プラスされました!!!')
            print('あなたのコインは' + str(coin + tip) + 'です。')
            coin = coin + tip
        elif int(str(kad3comnumbr3p)[-1]) >= int(str(kad3numbr2p)[-1]):
            print(str(tip) + '回収されました…。')
            print('あなたのコインは' + str(coin - tip) + 'です。')
            coin = coin - tip
    elif int(str(kad3comnumbr2p)[-1]) >= 6:
        if int(str(kad3numbr2p)[-1]) == int(str(kad3comnumbr2p)[-1]):
            print('同点です')
            if katimake == 'd':
                print(str(tip) + 'プラスされました!!!')
                print('あなたのコインは' + str(coin + tip) + 'です。')
            else:
                print(str(tip) + '回収されました…。')
                print('あなたのコインは' + str(coin - tip) + 'です。')
        elif int(str(kad3numbr2p)[-1]) >= int(str(kad3comnumbr2p)[-1]):
            print('playerの勝ちです')
            if katimake == 'p':
                print(str(tip) + 'プラスされました!!!')
                print('あなたのコインは' + str(coin + tip) + 'です。')
            else:
                print(str(tip) + '回収されました…。')
                print('あなたのコインは' + str(coin - tip) + 'です。')
        elif int(str(kad3comnumbr2p)[-1]) >= int(str(kad3numbr2p)[-1]):
            print('bankerの勝ちです')
            if katimake == 'b':
                print(str(tip) + 'プラスされました!!!')
                print('あなたのコインは' + str(coin + tip) + 'です。')
            else:
                print(str(tip) + '回収されました…。')
                print('あなたのコインは' + str(coin - tip) + 'です。')
else:
    print('')
    print('playerのカードの1の位が5より小さいのでもう1枚引きます。')
    print('   ' + str(kad2[numbr1]) + '   ' + str(kad2[numbr2]) + '    ' + str(kad2[numbr3]) + '   |   ' + '   ' + str(kad2[comnumbr1]) + '   ' + str(kad2[comnumbr2]))
    print('        player     |      banker         ')
    print('         ' + str(kad3numbr3p)[-1] + '         |         ' + str(kad3comnumbr2p)[-1] + '          ')
    print('')
    if int(str(kad3numbr3p)[-1]) == 0 or int(str(kad3numbr2p)[-1]) == 1:
        if int(str(kad3comnumbr3p)[-1]) == 0 or int(str(kad3comnumbr3p)[-1]) == 1 or int(str(kad3comnumbr3p)[-1]) == 2 or int(str(kad3comnumbr3p)[-1]) == 3:
            print('bankerのカードの1の位が3より小さいのでもう1枚引きます。')
            print('   ' + kad2[numbr1] + '   ' + kad2[numbr2] + '    ' + kad2[numbr3] + '   |   ' + '   ' + kad2[comnumbr1] + '   ' + kad2[comnumbr2] + '    ' + kad2[comnumbr3])
            print('        player     |      banker         ')
            print('         ' + str(kad3numbr3p)[-1] + '         |         ' + str(kad3comnumbr3p)[-1] + '          ')
        else:
            if int(str(kad3numbr2p)[-1]) >= int(str(kad3comnumbr3p)[-1]):
                print(str(tip) + 'プラスされました!!!')
                print('あなたのコインは' + str(coin + tip) + 'です。')
                coin = coin + tip
            elif int(str(kad3comnumbr3p)[-1]) >= int(str(kad3numbr2p)[-1]):
                print(str(tip) + '回収されました…。')
                print('あなたのコインは' + str(coin - tip) + 'です。')
                coin = coin - tip
owari = input('終わりですenterを押してください')
#    print('bankerのカードの1の位が5より小さいのでもう1枚引きます。')
#    print('   ' + kad2[numbr1] + '   ' + kad2[numbr2] + '    ' + kad2[numbr3] + '   |   ' + '   ' + kad2[comnumbr1] + '   ' + kad2[comnumbr2] + '    ' + kad2[comnumbr3])
#    print('        player     |      banker         ')
#    print('         ' + str(kad3numbr3p)[-1] + '         |         ' + str(kad3comnumbr3p)[-1] + '          ')
#else:
#    print('bankerのカードの1の位が5より大きいのでストップします')
#
#        if katimake == 'd':
#            print(str(tip) + 'プラスされました!!!')
#            print('あなたのコインは' + str(coin + tip) + 'です。')
#        else:
#            print(str(tip) + '回収されました…。')
#            print('あなたのコインは' + str(coin - tip) + 'です。')
#
#            if int(str(kad3numbr2p)[-1]) >= int(str(kad3comnumbr3p)[-1]):
#                print(str(tip) + 'プラスされました!!!')
#                print('あなたのコインは' + str(coin + tip) + 'です。')
#                coin = coin + tip
#            elif int(str(kad3comnumbr3p)[-1]) >= int(str(kad3numbr2p)[-1]):
#                print(str(tip) + '回収されました…。')
#                print('あなたのコインは' + str(coin - tip) + 'です。')
#                coin = coin - tip