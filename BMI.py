print("あなたの体重を教えてください。")
taijyu=int(input())
print("あなたの身長を教えてください。")
shintyou=int(input())
bmi=taijyu*10000//shintyou**2
print("あなたのBMIは" + str(bmi) + "です。")
print("判定は")
if bmi < 18.5:
    print("低体重です。病院に行くことを検討しましょう。")
elif 18.5 <= bmi < 25:
    print("普通体重です。この維持につとめましょう。")
elif 25 <= bmi < 30:
    print("肥満度1です。いま成人病への扉を開けてしまいました。")
elif 30 <= bmi < 35:
    print("肥満度は2です。立派な成人病です。")
    print('dvは犯罪です。病院以外で外に出ないでください')
elif 35 <= bmi < 40:
    print("肥満度は3です。入院まであと１歩です。")
    print('dvは犯罪です。病院以外で外に出ないでください')
else:
    print("肥満度4です。肥満・脂身・成人病です。")
    print('入院しましょう。')
    print('dvは犯罪です。病院以外で外に出ないでください')
