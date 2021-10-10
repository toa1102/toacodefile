import utils
# randomモジュールを読み込んでください
import random

print('決闘をはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: ドラゴン, 1: xソード, 2: 龍)')
player_hand = int(input('数字で入力してください：'))

if utils.validate(player_hand):
    # randintを用いて0から2までの数値を取得し、変数computer_handに代入してください
    computer_hand = random.randint(0, 2)
    
    if player_name == '':
        utils.print_hand(player_hand)
    else:
        utils.print_hand(player_hand, player_name)
    
    utils.print_hand(computer_hand, '魔王')
    
    result = utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')