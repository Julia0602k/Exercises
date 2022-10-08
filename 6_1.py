#Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def bin_number(number1: int) -> str:
    binary = ''
    while number1 > 1:
        binary += str(number1 % 2)
        number1 //= 2
    binary += str(number1)
    return binary[::-1]

print(bin_number(14))
