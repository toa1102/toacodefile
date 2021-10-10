from じゃんけん2 import jyanken


kazu = int(input('猫のかずを数字で入力してください'))
def neko1():
    namae = input('猫の名前を入力してください　:')
    omosa = int(input('猫の体重を整数で入力してください　:'))
    if omosa >= 3:
        print(namae + 'は肥満です')
    else:
        print(namae + 'は正常な体重です')
for i in range(kazu):
    neko1()
finito = input('終わりですenterを入力してください')
