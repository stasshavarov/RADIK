with open('text_1_var_14') as file:
    lines = file.readlines()

text = ''.join(lines)
a = ['!', '?', ',', '.', '\n', '  ']

for symbol in a:
    text = text.replace(symbol, ' ')

text = text.split()
dict = {}

for word in text:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

with open('text_1_otvet_var_14', 'w') as file:
    for word, count in sorted(dict.items(), key = lambda x: x[1], reverse = True):
        file.write(word + ' ' + str(count) + '\n')