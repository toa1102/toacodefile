import random
import time
print('')
coment = input('スタート')
print('')
point = 500
timer = 0
for i in range(5):
    nomber1 = random.randint(1,9)
    nomber2 = random.randint(1,9)
    nomber3 = random.randint(1,9)
    goukei = nomber1 + nomber2 + nomber3
    print((str(nomber1) + ' + ' + str(nomber2) + ' + ' + str(nomber3)))
    # 時間計測開始
    time_sta = time.time()
    anser = int(input('答え：'))
    # 時間計測終了
    time_end = time.time()
    # 経過時間（秒）
    tim = time_end- time_sta
    if anser == goukei and tim <= 1.5:
        print('excellent!!')
        point = point
        print(round(tim, 1))
    elif anser == goukei and tim <= 5:
        print('true')
        point = point - round(tim, 1)
        print(round(tim, 1))
    else:
        print('fail')
        point = point - 100 - round(tim, 1)
        print(round(tim, 1))
print('score : ' + str(round(point, 2)))
print('Time : ' + str(tim))
coment = input('finish')