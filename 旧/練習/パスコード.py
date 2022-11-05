print('')
print('パスコード暗号は aot です。')
print('')
aaa = 'aot'
bbb = input('パスコードを入力してください　： ')
# 文字列[::-1]とすれば反転できる
rslt = aaa[::-1]
if rslt == bbb:
    print('認証しました。')
    print('')
    print('パスコード暗号は r1o1c:k2e3t です。')
    print('')
    aaa = 'rocket11:23'
    bbb = input('パスコードを入力してください　： ')
    if aaa == bbb:
        print('認証しました。')
        print('ロケット打ち上げ日：3/24　ロケット帰還日：10/24')
        print('ロケットasa の打ち上げ時間 am3 :20')
        print('ロケットhiruの打ち上げ時間 am11:23')
        print('ロケットyoruの打ち上げ時間 pm8 :48')
        print('ロケットasa の帰還時間　　 am3 :20')
        print('ロケットhiruの帰還時間　　 am11:23')
        print('ロケットyoruの帰還時間　　 pm8 :48')
    else:
        print('パスコードが間違っています')
        print('サービスが利用できません。')
else:
    print('パスコードが間違っています')
    print('サービスが利用できません。')
owari = input('ご利用ありがとうございました。enterで退出してください')