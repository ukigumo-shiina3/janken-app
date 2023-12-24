class Animal:

    # count = 0 #クラス変数→そのクラスのみで認識される変数

    def __init__(self,kind,age):
        #__init__→特殊なメソッド（特殊メソッドまたはマジックメソッドとも呼ばれる）
        #クラスのインスタンスが作成されたときに自動的に呼び出されるメソッド
        #クラスのコンストラクタとして知られ、新しいオブジェクトの初期化を行うために使用されます。
        #少なくとも1つの引数（通常はself）を取ります。
        #selfは、クラスのインスタンス自体を指す特別な引数で、インスタンス変数を設定したり、初期化コードを実行したりするために使用されます。
        #__init__メソッドは2つの引数を取ります：kindとage。
        #このメソッドは、新しいオブジェクトが作成されたときにkindとageの値を受け取り、それぞれの値をインスタンス変数self.kindとself.ageに格納します。
        # このようにして、新しいオブジェクトの初期状態を設定できます。
        self.kind = kind
        self.age = str(age) + '歳'
        # Animal.count += 1


    def cry(self): #メソッドを定義。引数はselfを使用する。
        print('私は' + self.kind + 'です')

        # pochi = Animal("犬", 5)
        # tama = Animal("猫", 3)
        # print(pochi.kind, pochi.age)
        # print(tama.kind, tama.age)
        # print(Animal.count)

        # pochi.cry()
        # tama.cry()

class Dog(Animal):
    pass

class Cat(Animal):

    def __init__(self, kind, age,color):
        super().__init__(kind, age) #親クラスのAnimalにkindとageを渡す
        self.color = color #親クラスにはcolorを渡せないので自分のところで定義しておく

    def cry(self):
        print('にゃー' + self.kind +'色は' + self.color + "だにゃー")
    
#     def run(self):
#         print('駆け回ります')

pochi = Dog('秋田犬',8)
pochi.cry()

tama = Cat('ハチワレ', 3, '白')
tama.cry()