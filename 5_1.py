#вывести первые N чисел, кратные M и больше K
n = int(input('Write n: '))
m = int(input('Write m: '))
k = int(input('Write k: '))
k += 1
number = 0
list1 = []
while number <= n:
    if not k % m:
        list1.append(k)
        number = number + 1
        k *= m
 print(list1)