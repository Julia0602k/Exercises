n = int(input('Write N: '))
#list1 = []
#for i in range(n + 1):
#    if not i % 2:
#        list1.append(i ** 2)
#print(list1)

list1 = [i ** 2 for i in range(2, n+1) if not i%2]
print(list1)
