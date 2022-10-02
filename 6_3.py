#Дан список чисел и на вход поступает число N, необходимо сместить список на указанное число,
# #пример [1,2,3,4,5,6,7], N=3, ответ [5,6,7,1,2,3,4]
number = input('Write number N: ')
list1 = [1, 2, 3, 4, 5, 6, 7]
def move_index(list):
    list(map(move_index(list1), list1))
    print(list1)

move_index(list1)


    #for i in range (i+number):




        #arr = list(map(int, input().split()))
       # w = arr[-1]
       # for i in range(n - 1, 0, -1):
        #    arr[i] = arr[i - 1]
        #arr[0] = w
        #print(*arr)