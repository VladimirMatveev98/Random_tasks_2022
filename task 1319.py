import re

"""Переставить и вывести на экран слова заданного предложения
в соответствии с ростом доли согласных в этих словах"""

consonat = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п',
            'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

test_message = "Таким образом, постоянное обеспечение нашей деятельности..."
ratio = {}
c = 0
priority = float(0)
res = str()

#message = str(input("Введите предложение: "))
message = test_message
message = message.lower()
message = re.split(r'[ ,-.!?:;"]', message)

for word in message:
    if len(word) != 0:
        for letter in word:
            if letter in consonat:
                c = c + 1
        priority = c / len(word)
        ratio[priority] = word
        priority = 0
        c = 0

keys = list(ratio.keys())
keys.sort()

for key in keys:
    word = ratio[key]
    res = res + word + ' '

print (res)
