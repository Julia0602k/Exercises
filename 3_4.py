number1 = str(input('Write a first number:'))
number2 = str(input('Write a second number:'))
number3 = str(input('Write a third number:'))

summa_negative = number1.startswith('-') + number2.startswith('-') + number3.startswith('-')
summa_positive = 3 - summa_negative
print('Answer is:\n', '\tpositive:', summa_positive, '\n\tnegative:', summa_negative)

# Variant 2
number1 = int()
number2 = int()
number3 = int()
summa_positive1 = (number1 > 0) + (number2 > 0) + (number3 > 0)
summa_negative1 = 3 - summa_positive1
print('Answer is:\n', '\tpositive:', summa_positive1, '\n\tnegative:', summa_negative1)



