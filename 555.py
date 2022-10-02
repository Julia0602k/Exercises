n = int(input('Write N: '))
list1 = []
for i in range(n + 1):
    if not i % 2:
        list1.append(i ** 2)