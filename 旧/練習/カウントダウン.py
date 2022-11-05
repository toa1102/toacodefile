#カウントダウン
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
        print('')
        print('沖ノ鳥島までミサイル発射します。')
        print('北緯12度25分31.9768秒 東経136度4分52.1430秒 より、')
        print('北緯20度25分31.9768秒 東経136度4分52.1430秒準備完了!!')
        from time import sleep
        target_time = 20
        def up_timer(secs):
            for i in range(12,secs):
                print('北緯' + str(i) + '度25分31.9768秒 東経136度4分52.1430秒')
                sleep(1)
            print('')
            print("沖ノ鳥島撃破完了!!")
            print('全ての任務が完了しました')
        up_timer(target_time)
    else:
        print('パスコードが間違っています')
        print('サービスが利用できません。')
else:
    print('パスコードが間違っています')
    print('サービスが利用できません。')
owari = input('ご利用ありがとうございました。enterで退出してください')