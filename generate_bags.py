from bag import *

d = Words()
HEAD_WORD = None
HEAD_BAG = None
with open("./data/DE_morph_dict.txt", 'r') as f:
    counter = 1 #  making 0 == unkown
    for line in f:
        line = line.strip()
        words = line.split(' ')
        word = words[0]
        if word not in d:
            d.add_empty_word(word)
        if len(words) == 1:
            HEAD_WORD = word
            d.sget(word)[1] = counter
        if len(words) > 1:
            d.combine_bags(HEAD_WORD, word)
        counter += 1


## FREQUENCY LIST for Humans ##

with open("./data/de_full_opensubtitle.txt", 'r') as f:
    with open("./data/not_found_words.txt", 'w') as tmp_file:
        for line in f:
            line = line.strip()
            words = line.split(' ')
            if len(words) == 1:
                print(words[0], " has no frequency")
                continue
            word = words[0]
            frequency = int(words[1])
            #TODO check for multiple occurence...don't remove already registerd frequency
            if word in d:
                d.sget(word)[0].frequency += frequency #the frequency belong to the set
            else:
                tmp_file.write(word + '\t' + str(frequency) + "\n")

#convert frequency to number order
def mean_val(bags):
    counter = 0
    for x in bags.values():
       counter += x.frequency 
    return counter/len(bags)

def varianc_val(bags, mean):
    counter = 0
    for x in bags.values():
        counter += (x.frequency - mean)**2
    return counter/len(bags)


## Adding order number for each bag
d.Bags = sorted(d.Bags.values(), key= lambda v: v.frequency , reverse = True)
counter = 1
for x in sbags:
    x.order = counter
    counter += 1

## Test
with open("./data/text.txt", 'r') as f:
    text = f.read()
print(text)

import re
with open("./data/test.txt", 'w') as f:
    words = re.split('\W+', text)
    words = list(set(words))
    ordered_words = []
    unrecognized = []
    for w in words:
        w = w.lower()
        order = 0
        if w in d:
            order = d.sget(w)[0].order
            ordered_words.append([w, order])
        else:
            unrecognized.append(w)
    ordered_words = sorted(ordered_words, key=lambda v: v[1], reverse = True)
    for w in ordered_words:
        f.write(w[0] + ' ' + str(w[1]) + ' \n')
    for w in unrecognized:
        f.write(w + ' ' + '!!!!!!' + ' \n')

#top 5000 words
with open("./data/5000.txt", 'w') as f:
    counter = 0
    for x in d.Bags:
        f.write(next(iter(x)) + '\n')
        counter += 1
        if counter > 5000:
            break
