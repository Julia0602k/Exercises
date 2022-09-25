number1 = int(input('Write a first number:'))
number2 = int(input('Write a second number:'))
number3 = int(input('Write a third number:'))

answer_negative = int(0)
if number1 < 0:
    answer_negative = answer_negative + 1
if number2 < 0:
    answer_negative = answer_negative + 1
if number3 < 0:
    answer_negative = answer_negative + 1
answer_positive = 3 - answer_negative

print('Answer is:\n', '\tpositive:', answer_positive, '\n', '\tnegative:', answer_negative)
