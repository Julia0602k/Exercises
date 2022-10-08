#Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних - один из соседей - число, с противоположной стороны списка
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers)):
    if i != len(numbers) - 1:
        print(numbers[i-1] + numbers[i+1])
    else:
        print(numbers[i-1] + numbers[0])
