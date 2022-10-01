#вывести первые N чисел, кратные M и больше K
n = int(input('Write n: '))
m = int(input('Write m: '))
k = int(input('Write k: '))
number = 0
while number <= n:
    k += 1
    if not k % m:
        number = number + 1
        print(k)


