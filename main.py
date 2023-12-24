def is_even(num):
    return num % 2 == 0

nums = map(int, ['1','2','3'])
even_nums = filter(is_even,nums) #trueになったものだけを残す #第一引数: 関数
print(list(even_nums))

