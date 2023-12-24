nums = [i for i in range(10)]
nums #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [1, 2, 3, 4, 5]
even_squared_numbers = [num ** 2 for num in numbers if num % 2 == 0] # ifの状態が残った上で初期化される

print(even_squared_numbers)  # [4, 16]