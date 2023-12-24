number = 1
number2 = 1.0
greeting = 'こんにちは'
is_ok = True

print(number, type(number))
print(number2, type(number2))
print(greeting, type(greeting))
print(is_ok, type(is_ok))

print(2 > 1)
print(1 > 2)

print(True)
# print(true)

5 + True #6 Trueは1と認識される
5 * False #6 Falseは0と認識される

bool(1) #True
bool(120) #True
bool(-120)#True
bool(0)#False

'Mika'[-1] #a