f = open('sample.txt', mode='w') #'w'はwrite書き込みモード 'a'はadd追加モード
f.write('Good morning \n') #引数にファイルに書き込む文字列を書く。再度文字列変えて出力すると、上書きされる。
f.close() #開いたファイルを閉じる。ファイルが開きっぱなしだとPCのメモリが食われてオーバーヘッドになる

# print(f)
# print(type(f))