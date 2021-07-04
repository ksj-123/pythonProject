# what is the most freq. used word in Shakespeares' sonnets?
# filter prevers and other trash
import pprint
filter_words = ['we ', 'they ', 'you ', 'i ', 'as ', 'to ', 'me ', 'are ']


def filter_word(all_text, word):
    return all_text.replace(word, '')


count = {}

with open("sonnets.txt", 'r') as sonnets:
    all_sonnets = sonnets.read()
    all_sonnets = all_sonnets.lower()
    for word in filter_words:
        all_sonnets = filter_word(all_sonnets, word)

    for word in all_sonnets.split(" "):
        count[word] = count.get(word, 0) + 1

print(sorted(count.items(), key=lambda x: -x[1]))
# print(all_sonnets)
#pprint.pprint(count)
