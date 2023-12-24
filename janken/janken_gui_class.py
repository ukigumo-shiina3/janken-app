import random
import tkinter as tk
from PIL import Image, ImageTk

GU, CHOKI, PA = 'グー', 'チョキ', 'パー'
hands = ['GU', 'CHOKI', 'PA']
WIN, DRAW, LOSE = '勝ち', 'あいこ', '負け'
rules = {
    (0,0): DRAW, (0,1): WIN, (0,2): LOSE,
    (1,0): LOSE, (1,1):DRAW , (1,2): WIN,
    (2,0): WIN, (2,1): LOSE, (2,2): DRAW
}

class View: #画面表示に責任を持つクラス
    def __init__(self):
        #self は、そのクラスのインスタンス自体を指し示します。
        self.gu_image = Image.open('img/gu.png').convert('RGB').resize((100,100))
        self.gu_image = ImageTk.PhotoImage(self.gu_image, master=root)
        #インスタンス変数にするためにselfをつける。
        #Viewの所有物とするために
        #インスタンス→クラス（Class）の設計に基づいて作成された具体的なデータ構造
        #クラスが設計図であるのに対して、インスタンスはその実体を表現します。

        self.choki_image = Image.open('img/choki.png').convert('RGB').resize((100,100))
        self.choki_image = ImageTk.PhotoImage(self.choki_image, master=root)

        self.pa_image = Image.open('img/pa.png').convert('RGB').resize((100,100))
        self.pa_image = ImageTk.PhotoImage(self.pa_image, master=root)

        self.images = [self.gu_image, self.choki_image, self.pa_image]

        self.gu_label = tk.Label(root, image=self.gu_image)
        self.gu_label.place(x=20,y=200)

        self.choki_label =tk.Label(root, image=self.choki_image)
        self.choki_label.place(x=160,y=200)

        self.pa_label = tk.Label(root, image=self.pa_image)
        self.pa_label.place(x=300,y=200)

        self.gu_button = tk.Button(root, text='グー')
        self.gu_button.place(x=55, y=320)

        self.choki_button = tk.Button(root, text='チョキ')
        self.choki_button.place(x=190, y=320)

        self.pa_button = tk.Button(root, text='パー')
        self.pa_button.place(x=335, y=320)

        self.enemy_label = tk.Label(root, image=self.gu_image)
        self.enemy_label.place(x=160, y=20)
        self.text_label = tk.Label(root, text='最初はグー！じゃんけん！')
        self.text_label.place(x=140,y=140)

        self.retry_button = tk.Button(root, text='リトライ')

    def reset(self):
        self.retry_button.place_forget()
        #place_forget→非表示にするメソッド

    def display(self,enemy, result):
        self.enemy_label.configure(image=self.images[enemy])
        #configure→ウィジェット（ボタン、ラベル、エントリなどのGUIコンポーネント）の属性やオプションを変更するためのメソッド
        if result == DRAW:
            self.text_label.configure(text='あいこ')
        elif result == WIN:
            self.text_label.configure(text='勝ち!')
        else:
            self.text_label.configure(text='負け！')

    def show_retry(self):
        self.retry_button.place(x=185, y=360)
        self.gu_button['state'] = tk.DISABLED
        self.choki_button['state'] = tk.DISABLED
        self.pa_button['state'] = tk.DISABLED

        self.enemy_label.configure(image=self.images[0])
        self.text_label.configure(text='最初はグー！じゃんけん！')

class Application(tk.Frame): #じゃんけんの処理に責任を持つクラス

    def __init__(self, master=None):
        #master→Tkinterアプリケーションのルートウィンドウ（またはメインウィンドウ）を表すオブジェクト。
        super().__init__(master)
        master.geometry('420x400')
        master.title('じゃんけんゲーム')

        self.view = View()

        self.view.gu_button['command'] = lambda: self.judge(0)
        self.view.choki_button['command'] = lambda: self.judge(1)
        self.view.pa_button['command'] = lambda: self.judge(2)
        #lambda→無名関数を１行でかける(下のpress_guと無名関数の内容は一緒だが、無名関数の方が１行でかける)
        #lambdaを外している状態だと、()で関数が呼び出されるので、lambdaの関数をつけた方がいい
        # def press_gu():
        # judge(0)
        self.view.retry_button['command'] = self.retry


    def judge(self, my_hand):
        enemy = random.randint(0,2)
        result = rules[(my_hand,enemy)]
        self.view.display(enemy,result)
        if result != DRAW:
            self.view.show_retry()

    def retry(self):
        self.view.reset()

root = tk.Tk()
app = Application(master=root)
app.mainloop()