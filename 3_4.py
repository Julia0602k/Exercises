number1 = str(input('Write a first number:'))
number2 = str(input('Write a second number:'))
number3 = str(input('Write a third number:'))

summa_negative = int()
summa_positive = int()
summa_negative = number1.startswith('-') + number2.startswith('-') + number3.startswith('-')
summa_positive = 3 - summa_negative
print('Answer is:\n', '\tpositive:', summa_positive, '\n\tnegative:', summa_negative)



