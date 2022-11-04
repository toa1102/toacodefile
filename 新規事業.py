import random
for i in range(5):
    nomber1 = random.randint(1,9)
    nomber2 = random.randint(1,9)
    nomber3 = random.randint(1,9)
    goukei = nomber1 + nomber2 + nomber3
    print((str(nomber1) + ' + ' + str(nomber2) + ' + ' + str(nomber3)))
    anser = int(input('答え：'))
    if anser == goukei:
        print('true')
    else:
        print('fail')

    coment = input()
coment = input('finish')