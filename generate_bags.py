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
            d[word][1] = counter
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
                d[word][0].frequency += frequency #the frequency belong to the set
            elif word.lower() in d:
                d[word.lower()][0].frequency += frequency
            elif word.capitalize() in d:
                d[word.capitalize()][0].frequency += frequency
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
sbags = sorted(d.Bags.values(), key= lambda v: v.frequency , reverse = True)

counter = 0
for x in sbags:
    x.order = counter
    counter += 1


## Test

with open("./data/test.txt", 'w') as f:
    text = "Es tut uns leid, dass die von Ihnen angeforderte Seite nicht verfügbar ist. Hier können Sie mit Stichworten nach dem gewünschten Inhalt suchen :"
    words = text.split(' ')
    for w in words:
        if w in d:
            f.write(w + ' ' + str(d[w][0].order) + '\n')
        elif w.capitalize() in d:
            f.write(w + ' ' + str(d[w.capitalize()][0].order) + '\n')
        elif w.lower() in d:
            f.write(w + ' ' + str(d[w.lower()][0].order) + '\n')
        else:
            f.write(w + ' ' + "!!!!!!!" + '\n')
