import bag
bags = bag.Bag()
bags.add_bag({"wow"},3)


import pickle
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
def load_object(filename):
    with open(filename, 'rb') as input:
        tech_companies = pickle.load(input)
        return tech_companies

## A set is an arry of 2 elements one is a set and the other is an integer
def add_word_to_set(dictionary, SET, new_word, counter):
    if new_word in dictionary:
        new_SET = dictionary[new_word][0]
    else:
        new_SET = [{new_word}, 0]
        dictionary[new_word]= [new_SET, counter, 0]
    SET[0] = SET[0].union(new_SET[0])
    for x in new_SET[0]:
        dictionary[x][0] = SET

###create bags###

d = {}
HEAD_WORD = None
HEAD_SET = None
BAGS = []
with open("./data/DE_morph_dict.txt", 'r') as f:
    counter = 1 #  making 0 == unkown
    for line in f:
        line = line.strip()
        words = line.split(' ')
        word = words[0]
        if len(words) == 1:
            if word in d:
                HEAD_SET = d[word][0]
                d[word][1] = counter
            else:
                HEAD_SET = [{word}, 0]
                d[word] = [HEAD_SET, counter, 0]
        if len(words) > 1:
            add_word_to_set(d, HEAD_SET, word, counter)
        counter += 1

### Dictionary of words and FREQUENCY ###

d = {}
HEAD_WORD = None
with open("./data/DE_morph_dict.txt", 'r') as f:
    counter = 1 #  making 0 == unkown
    for line in f:
        line = line.strip()
        words = line.split(' ')
        word = words[0]
        if len(words) == 1:
            if word in d:
                d[word][1] = counter
            else:
                d[word] = [ counter, 0]
        if len(words) > 1:
            continue
        counter += 1

### reading frequency file ###
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
                d[word][1] = frequency
            elif word.lower() in d:
                d[word.lower()][1] += frequency
            elif word.capitalize() in d:
                d[word.capitalize()][1] += frequency
            else:
                tmp_file.write(word + '\t' + str(frequency) + "\n")

## Saving unmatched words
with open("./data/not_matched_words.txt", 'w') as tmp_file:
    for k in d:
        if d[k][1] == 0:
            tmp_file.write(k + '\n')



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
                d[word][0][1] += frequency #the frequency belong to the set
            elif word.lower() in d:
                d[word.lower()][1] += frequency
            elif word.capitalize() in d:
                d[word.capitalize()][1] += frequency
            else:
                tmp_file.write(word + '\t' + str(frequency) + "\n")

#convert frequency to number order
def mean_val(dictionary):
    counter = 0
    for x in dictionary:
       counter += dictionary[x][0][1] 
    return counter/len(dictionary)

def varianc_val(dictionary, mean):
    counter = 0
    for x in dictionary:
        counter += (mean
