name = input('What is you name?')
age = input('How old are you?')
city = input('Where are you from?')

#variant1
text1 = 'Hello, %s!' % (name)
text2 = 'Your age are %s.' % (age)
text3 = 'You live in %s.' % (city)
print(text1, text2, text3)

#variant2
text_var2 = 'Hello, {}! Your age are {}. Your live in {}.'.format(name, age, city)
print(text_var2)

#variant3
text_var3 = f'Hello, {name}! Your age are {age}. Your live in {city}.'
print(text_var3)






