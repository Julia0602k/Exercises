#Код Морзе для представления цифр и букв использует тире и точки.
#Напишите функцию для кодирования текстового сообщения в соответствии с кодом Морзе
text1 = input('Write a text: ')
dict_morze = {
    'a': '.-', 'b': '-...',
    'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....',
    'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.',
    's': '...', 't': '-',
    'u': '..-', 'v': '...-',
    'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '1': '.---', '2': '..---',
    '3': '...--', '4': '....-',
    '5': '.....','6': '-....',
    '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
    }
text1 = text1.lower()
list1 = text1.split(' ')
i = 0
def text_to_morse(text1):
    for i in list1(j):
        dict_morze.get(j)

text_to_morse(text1)

print(text1)