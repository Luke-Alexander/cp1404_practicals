"""Luke Alexander"""
text = input('Text: ')
text = text.lower().split(' ')
text_bank = {}
longest_word = ()

for word in text:
    if len(word)>len(longest_word):
        longest_word = word
    if word in text_bank:
        text_bank[word] = text_bank[word] + 1
    else:
        text_bank[word] = 1

for word in sorted(text_bank):
    print("{:{}} = {}".format(word, len(longest_word), text_bank[word]))