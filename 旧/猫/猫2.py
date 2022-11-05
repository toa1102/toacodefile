import random
aaa = random.randint(100,999)
aa2 = str(aaa)[::-1]
print('')
a1 = input('start')
print('')
print('Code = ' + aa2)
print('')
key = int(input('please write key : '))
if key == aaa:
    print('')
    name = input('Please write your name :')
    print('')
    print('hello' + name)
    print('')
    print('Please select a language')
    print('')
    genngo = int(input('1 日本語 2 English 3 عربي : '))
    if genngo == 1:
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
    elif genngo == 2:
        kazu = int(input('How many cats'))
        def neko1():
            namae = input('Please enter the name of the cat:')
            omosa = int(input('Please enter the weight of the cat as an integer:'))
            if omosa >= 3:
                print(namae + 'Is obese')
            else:
                print(namae + 'Is normal weight')
        for i in range(kazu):
            neko1()
        finito = input('thank you')
    elif genngo == 3:
        kazu = int(input('كم قطة هناك'))
        def neko1():
            namae = input('')
            omosa = int(input('الرجاء إدخال وزن القط في صورة عدد صحيح:'))
            if omosa >= 3:
                print(namae + 'يعاني من السمنة')
            else:
                print(namae + 'وزن طبيعي')
        for i in range(kazu):
            neko1()
        finito = input('أدخل دخول')
    else:
        print('errer')
else:
    aa3 = input('The key is different')
    aa3 = input('thank you')