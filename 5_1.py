#вывести первые N чисел, кратные M и больше K
n = int(input('Write n: '))
m = int(input('Write m: '))
k = int(input('Write k: '))
number = 0
list1 = []
while number <= n:
    list1.append(k)
    k = k + m


   if k % m:
       number += 1
       list1.append (k)
print(list1)