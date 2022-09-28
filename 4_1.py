#заполнить список степенями числа 2 (от 2^1 до 2^n)
n = int(input('Write n: '))
list4_1 = [2**i for i in range(1, n+1)]
print(list4_1)
