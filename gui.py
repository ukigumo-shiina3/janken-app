import tkinter as tk # asでエイリアスをつける

root = tk.Tk() # rootがウィンドウを示している
root.geometry("200x200")

frame = tk.Frame(master=root) #rootのウィンドウの上にフレームを配置する
frame.pack(expand=True, fill='both') # フレームをウィンドウに配置する。expand=True, fill='both'で親のrootの大きさに合わせる。

button = tk.Button(frame, text='Button', command=root.destroy)
button.place(x=80, y=80)

root.mainloop()  #イベントループを開始します。これにより、ウィンドウが表示され、ユーザーの操作を待ちます。ボタンがクリックされたらcommand=root.destroyが実行される