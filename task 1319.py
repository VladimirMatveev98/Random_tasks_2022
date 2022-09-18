import re

"""Переставить и вывести на экран слова заданного предложения
в соответствии с ростом доли согласных в этих словах"""
#in progress
consonat = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п',
            'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


words = []
keys = []
test_message = "Таким образом, постоянное обеспечение нашей деятельности..."
ratio = {}
c = 0
i = 0
priority = float(0)
res = str()

#message = str(input("Введите предложение: "))
message = test_message
print(message)
message = message.lower()
message = re.split(r'[ ,-.!?:;"]', message)

for word in message:
    if len(word) != 0:
        for letter in word:
            if letter in consonat:
                c = c + 1
        priority = c / len(word)
        #print (priority)
        ratio[i] = priority
        words.append(word)
        priority = 0
        c = 0
        i += 1

print(ratio)
print(words)

for key in ratio:
    print ("%s -> %s" % (key, ratio[key]))

#print (res)
