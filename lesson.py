n = int(input('Write N'))
numbers = list()
for i in range(1, n):
    if not i % 2:
        numbers.append(i ** 2)
print(numbers)
