#withキーワードを使うとf.close()を書かなくてもファイルを閉じれる。閉じ忘れの防止になるのでwithを使う
with open('sample.txt', mode='w') as f:
    f.write('Good Morning!\n')
    f.write('Good Morning!\n')
    f.write('Good Morning!\n')