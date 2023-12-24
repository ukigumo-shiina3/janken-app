gu, choki, pa = "グー", "チョキ","パー" #変数に値を代入するための記法。タプルの分割代入
win, draw, lose = "勝ち", "あいこ","負け"

my_hand = choki
enemy_hand = gu

if my_hand == enemy_hand:
    print(draw)
elif (my_hand == gu and enemy_hand == choki) or \
    (my_hand == pa and enemy_hand == gu) or \
        (my_hand == choki and enemy_hand == pa):
    print(win)
else:
    print(lose)


