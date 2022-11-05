import random
com = random.randint(16,30)
gest1 = random.randint(1,11)
gest2 = random.randint(1,11)
gest3 = random.randint(1,11)
gest4 = random.randint(7,11)
print('ブラックジャックを始めます')
print('--------------------------------------------------')
print('あなたのカードは' + str(gest1) + 'と' + str(gest2) + 'です。')

goukei = gest1 + gest2
goukei1 = gest1 + gest2 + gest3
goukei2 = gest1 + gest2 + gest3 + gest4
def blackJack():
    kad = input('カードを引きますか？ yes or No:')
    if kad == 'yes':
        print('あなたのカードは' + str(gest1) + 'と' + str(gest2) + 'と' + str(gest3) + 'です')
        kad = input('カードを引きますか？ yes or No:')
        if kad == 'yes':
            print('あなたのカードは' + str(gest1) + 'と' + str(gest2) + 'と' + str(gest3) + 'と' + str(gest4) + 'です。')
            if com <= 20 and goukei2 == 21:
                print('ブラックジャック!!!')
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!1')
            elif com >= 22 and goukei2 == 21:
                print('ブラックジャック!!1')
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!1')
            elif com >= 22 and goukei2 <= 21:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!2')
            elif com <= goukei2 and goukei2 <= 20:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!3')
            elif goukei2 <= 20 and com >= 22:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!4')
            elif com == 21 and goukei2 == 21:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('同点です5')
            elif com == goukei2:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('同点です6')
            elif com >= 22 and goukei2 >= 22:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('同点です7')
            elif com >= goukei2 and com <= 21:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの負けです8')
            elif com >= goukei2:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの負けです9')
            elif com <= goukei2:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの負けです10')
            else:
                print('判定できません10')
        elif kad == 'No' and gest1 + gest2 + gest4 <= 16:
            print('カードを引いてください')
        elif kad == 'No':
            if com <= 20 and goukei == 21:
                print('ブラックジャック!!!')
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!1')
            elif com >= 22 and goukei <= 21:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!2')
            elif com <= goukei and goukei <= 20:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!3')
            elif goukei <= 20 and com >= 22:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの勝ちです!!4')
            elif com == 21 and goukei == 21:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('同点です5')
            elif com == goukei:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('同点です6')
            elif com >= 22 and goukei >= 22:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('同点です7')
            elif com >= goukei and com <= 21:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの負けです8')
            elif com >= goukei:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの負けです9')
            elif com <= goukei:
                print('コンピューターのカードは' + str(com) + 'でした')
                print('あなたの負けです10')
            else:
                print('判定できません10')
        else:
            print('')
    else:
        if com <= 20 and goukei == 21:
            print('ブラックジャック!!!')
            print('コンピューターのカードは' + str(com) + 'でした')
            print('あなたの勝ちです!!1')
        elif com >= 22 and goukei <= 21:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('あなたの勝ちです!!2')
        elif com <= goukei and goukei <= 20:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('あなたの勝ちです!!3')
        elif goukei <= 20 and com >= 22:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('あなたの勝ちです!!4')
        elif com == 21 and goukei == 21:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('同点です5')
        elif com == goukei:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('同点です6')
        elif com >= 22 and goukei >= 22:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('同点です7')
        elif com >= goukei and com <= 21:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('あなたの負けです8')
        elif com >= goukei:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('あなたの負けです9')
        elif com <= goukei:
            print('コンピューターのカードは' + str(com) + 'でした')
            print('あなたの負けです10')
        else:
            print('判定できません10')
    x = input('終わりです。enterをおしてください')
blackJack()