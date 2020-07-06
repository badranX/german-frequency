from ibag import *

%time
fm = "./data/DE_morph_dict.txt"
tfm = "./data/DE_morph_testing.txt"
d = Words()
HEAD_WORD = None
HEAD_BAG = None
with open(tfm, 'r') as f:
    counter = 1 #  making 0 == unkown
    for line in f:
        line = line.strip()
        words = line.split(' ')
        word = words[0]
        if word not in d:
            d.add_empty(word)
        if len(words) == 1:
            HEAD_WORD = word
            d[word][1] = counter
        if len(words) > 1:
            d.combine_bags(HEAD_WORD, word)
        counter += 1


## FREQUENCY LIST for Humans ##
frequency_file = "./data/de_full_opensubtitle.txt"
not_found_file = "./data/not_found_words.txt"
d.load_frequencies(frequency_file, not_found_file)


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



## Test
with open("./data/text.txt", 'r') as f:
    text = f.read()
print(text)

def get_bind_words(word, dictionary):
    erst = ""
    end = word
    for c in word:
       erst += c


         
import re
with open("./data/test.txt", 'w') as f:
    words = re.split('\W+', text)
    words = list(set(words))
    ordered_words = []
    unrecognized = []
    for w in words:
        order = 0
        if w in d:
            order = d[w][0].order
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
