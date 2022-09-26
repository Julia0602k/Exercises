number = int(input('Write N: '))
st = 1
while 2 ** st <= number:
    st = st + 1
st -= 1
print(st)
