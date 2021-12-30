import random
print('ミニバトルを始めます')
a = input('名前を入力してください : ')
print(a + 'さんこんにちは')
def batoru():
    print('-----------------------------------------------')
    print('スライムが1匹現れた❕❕')
    print('-----------------------------------------------')
    print(a + 'の攻撃')
    aa = int(input('0~5までの好きな数字を入力してください'))
    aaa = random.randint(0, 5)
    if aaa == aa:
        print('クリティカルヒット❕❕')
        print(a + 'の勝ちです')
    else:
        print('攻撃失敗')
        print('スライムの攻撃')
        aa = int(input('0~5までの好きな数字を入力してください'))
        aaa = random.randint(0, 5)
        if aaa == aa:
            print('防御成功❕❕')
            print(a + 'の攻撃')
            aa = int(input('0~5までの好きな数字を入力してください'))
            aaa = random.randint(0, 5)
            if aaa == aa:
                print('クリティカルヒット❕❕')
                print(a + 'の勝ちです')
            else:
                print('攻撃失敗')
                print('スライムの攻撃')
                aa = int(input('0~5までの好きな数字を入力してください'))
                aaa = random.randint(0, 5)
                if aaa == aa:
                    print('防御成功❕❕')
                    print(a + 'の攻撃')
                    aa = int(input('0~5までの好きな数字を入力してください'))
                    aaa = random.randint(0, 5)
                    if aaa == aa:
                        print('クリティカルヒット❕❕')
                        print(a + 'の勝ちです')
                    else:
                        print('攻撃失敗')
                else:
                    print('防御失敗')
                    print(a + 'の攻撃')
                    aa = int(input('0~5までの好きな数字を入力してください'))
                    aaa = random.randint(0, 5)
                    if aaa == aa:
                        print('クリティカルヒット❕❕')
                        print(a + 'の勝ちです')
                    else:
                        print('攻撃失敗')
        else:
            print('防御失敗')
            print(a + 'の攻撃')
            aa = int(input('0~5までの好きな数字を入力してください'))
            aaa = random.randint(0, 5)
            if aaa == aa:
                print('クリティカルヒット❕❕')
            else:
                print('攻撃失敗')
                print('スライムの攻撃')
                aa = int(input('0~5までの好きな数字を入力してください'))
                aaa = random.randint(0, 5)
                if aaa == aa:
                    print('防御成功❕❕')
                    print(a + 'の攻撃')
                    aa = int(input('0~5までの好きな数字を入力してください'))
                    aaa = random.randint(0, 5)
                    if aaa == aa:
                        print('クリティカルヒット❕❕')
                        print(a + 'の勝ちです')
                    else:
                        print('攻撃失敗')
                else:
                    print('防御失敗')
                    print('Game over')
import random
print('ミニバトルを始めます')
a = input('名前を入力してください : ')
print(a + 'さんこんにちは')
print('-----------------------------------------------')
print('スライムが1匹現れた❕❕')
print('-----------------------------------------------')
print(a + 'の攻撃')
aa = int(input('0~5までの好きな数字を入力してください'))
aaa = random.randint(0, 5)
if aaa == aa:
    print('クリティカルヒット❕❕')
    print(a + 'の勝ちです')
    batoru()
else:
    print('攻撃失敗')
    print('スライムの攻撃')
    aa = int(input('0~5までの好きな数字を入力してください'))
    aaa = random.randint(0, 5)
    if aaa == aa:
        print('防御成功❕❕')
        print(a + 'の攻撃')
        aa = int(input('0~5までの好きな数字を入力してください'))
        aaa = random.randint(0, 5)
        if aaa == aa:
            print('クリティカルヒット❕❕')
            print(a + 'の勝ちです')
            batoru()            
        else:
            print('攻撃失敗')
            print('スライムの攻撃')
            aa = int(input('0~5までの好きな数字を入力してください'))
            aaa = random.randint(0, 5)
            if aaa == aa:
                print('防御成功❕❕')
                print(a + 'の攻撃')
                aa = int(input('0~5までの好きな数字を入力してください'))
                aaa = random.randint(0, 5)
                if aaa == aa:
                    print('クリティカルヒット❕❕')
                    print(a + 'の勝ちです')
                    batoru()
                else:
                    print('攻撃失敗')
            else:
                print('防御失敗')
                print(a + 'の攻撃')
                aa = int(input('0~5までの好きな数字を入力してください'))
                aaa = random.randint(0, 5)
                if aaa == aa:
                    print('クリティカルヒット❕❕')
                    print(a + 'の勝ちです')
                    batoru()
                else:
                    print('攻撃失敗')
    else:
        print('防御失敗')
        print(a + 'の攻撃')
        aa = int(input('0~5までの好きな数字を入力してください'))
        aaa = random.randint(0, 5)
        if aaa == aa:
            print('クリティカルヒット❕❕')
            print(a + 'の勝ちです')
        else:
            print('攻撃失敗')
            print('スライムの攻撃')
            aa = int(input('0~5までの好きな数字を入力してください'))
            aaa = random.randint(0, 5)
            if aaa == aa:
                print('防御成功❕❕')
                print(a + 'の攻撃')
                aa = int(input('0~5までの好きな数字を入力してください'))
                aaa = random.randint(0, 5)
                if aaa == aa:
                    print('クリティカルヒット❕❕')
                    print(a + 'の勝ちです')
                    batoru()
                else:
                    print('攻撃失敗')
            else:
                print('防御失敗')
aaaa = int(input('終わりです　1と入力してください'))