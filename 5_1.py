#вывести первые N чисел, кратные M и больше K
n = int(input('Write n: '))
m = int(input('Write m: '))
k = int(input('Write k: '))
k = m
number = 0
list1 = []
while number <= n:
   if k % m:
       number += 1
       list1.append (k)
print(list1)