#вывести первые N чисел, кратные M и больше K
n = int(input('Write n: '))
m = int(input('Write m: '))
k = int(input('Write k: '))
k += 1
number = int()
list1 = ()
while number <= n:
   if k % m:
       number += 1
       list1.append(k)
print(list1)