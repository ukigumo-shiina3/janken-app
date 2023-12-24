with open('sample.txt', mode='r+') as f: #'r+'で読み書き両用のモードになる
    print(f.tell()) #tellのファイルポインターでtxtダイルが何文字あるか教えてくれる #txtファイルの先頭は0
    data = f.read()
    print(f.tell()) #txtファイルの合計文字数は42
    f.write('Goog morning!!\n')
    print(f.tell())
    f.seek(0) #n番目の位置にポインターを移動させる
    data2 = f.read()
    print(data2) #前回のポインターの位置が変わっていないため空白で出力される