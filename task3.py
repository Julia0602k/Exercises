number = int(input('Write N: '))
st = 0
while 2 ** st <= number:
    st += 1
print(st-1)
