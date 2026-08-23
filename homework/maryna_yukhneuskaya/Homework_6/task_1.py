text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

words = text.split()

new_words = []

for word in words:
    if word[-1] == ',' or word[-1] == '.':
        punctuation = word[-1]
        word = word[:-1]
        word = word + 'ing' + punctuation
    else:
        word = word + 'ing'

    new_words.append(word)

result = ' '.join(new_words)

print(result)