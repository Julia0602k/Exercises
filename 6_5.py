#Дан список чисел, надо его развернуть
# без использования reverse и функции reversed,
# а так же дополнительного списка и среза

list1 = [1, 2, 3, 4, 5, 6, 7]
def func_reverse1(list):
    n = int(len(list))
    i = 1
    for i in range(i, n+1, -1):
        print(list)

func_reverse1(list1)




