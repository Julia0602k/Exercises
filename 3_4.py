number1 = bool(input('Write a first number:'))
number2 = bool(input('Write a second number:'))
number3 = bool(input('Write a third number:'))
summa_positive = int()
summa_positive = number1 + number2 + number3
summa_negative = 3 - summa_positive
print('Answer is:\n', '\tpositive:', summa_positive, '\n\tnegative:', summa_negative)




#Variant 2
answer_negative = int(0)
if number1 < 0:
    answer_negative = answer_negative + 1
if number2 < 0:
    answer_negative = answer_negative + 1
if number3 < 0:
    answer_negative = answer_negative + 1
answer_positive = 3 - answer_negative
print('Answer is:\n', '\tpositive:', answer_positive, '\n\tnegative:', answer_negative)
