import random

hands = ['グー', 'チョキ', 'パー']
win, draw, lose = '勝ち', 'あいこ', '負け'
rules = {
    (0,0): draw, (0,1): win, (0,2): lose,
    (1,0): lose, (1,1):draw , (1,2): win,
    (2,0): win, (2,1): lose, (2,2): draw
}

while True: #無限ループを止めることができないようにする。無限にじゃんけんする。
    my_hand = int(input(
    '''0〜2の数字を入力してください。
    0: グー, 1: チョキ, 2: パー
    >>>''')) #トリプルクォーテーションを使うことで、改行を含む長い文字列を簡単に記述することができる。
    enemy_hand = random.randint(0,2)

    my_hand_str = hands[my_hand]
    enemy_hand_str = hands[enemy_hand]
    print('自分: ' + my_hand_str + '相手: '+ enemy_hand_str)

    result = rules[(my_hand, enemy_hand)]
    print(result)

    if enemy_hand != my_hand:
        break