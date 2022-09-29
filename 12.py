text = input('Write a text: ')
text1 = list(filter(lambda x: x.isdigit(), text))
print(text1)
text1 = list(map(int, text1))
print(sum(text1))



