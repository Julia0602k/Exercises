n = int(input('Write number N: '))
numbers = list()
for i in range(1, n + 1):
    if not i % 2:
        numbers.append(i ** 2)
print(numbers)

