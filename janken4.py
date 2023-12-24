hands = ['グー', 'チョキ', 'パー']

my_input = input('0〜2の数字を入力してください>>>')
#inputの引数はそのままターミナルに出力される。入力されない場合はそのまま止まる。
print(my_input)
i = input(my_input)
hand = hands[i]
print(hand)