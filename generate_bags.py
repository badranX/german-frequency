from ibag import *
from utility import *
import grammar
import re
from CaseInsensitiveDict import CaseInsensitiveDict
#####Load Data

%timeit
fm = "./data/DE_morph_dict.txt"
tfm = "./data/DE_morph_testing.txt"
d = Words()
HEAD_WORD = None
important_parts = {
        "V" ,
    "ADJ",
    "ADV",
    "NN" } 

with open(fm, 'r') as f:
    isIch = True
    counter = 1 #  making 0 == unkown
    for line in f:
        line = line.strip()
        words = re.split('\W+', line) #TODO '[A-Za-z]+'
        word = words[0]
        if len(words)>2:
            if words[1] == "NNP":
                continue
        if word not in d:
#            if 'ich' in d:
#                if d['ich'][0] in d.Bags.set and isIch:
#                    print("WE FOUND ICH")
#                    isIch = False
#                if d['ich'][0] not in d.Bags.set and not isIch:
#                    print("WE lost ich")
#                    print("At word : " , word)
#                    isIch = True
            d.add_empty(word)
        if len(words) == 1:
            HEAD_WORD = word
            if word.isupper():
                word_l = word.lower()
                if word_l in d:
                    d.combine_bags(word, word_l)
            else:
                word_c = word.capitalize()
                if word_c in d:
                    d.combine_bags(word, word_c)
        if len(words) > 1:
            if words[1] in important_parts:
                d.set_speach_part(HEAD_WORD)
            d.combine_bags(HEAD_WORD, word)
        counter += 1


### Load FREQUENCY  ###

frequency_file = "./data/de_full_opensubtitle.txt"
not_found_file = "./data/not_found_words.txt"
d.load_frequencies(frequency_file, not_found_file)


### Test ####TODO bug
import parsing
pars = parsing.Parser(d)

pars.parse("./data/text.txt", "./data/test.txt")

#Restrict analysis to top 5000 words. The

#TODO this must be done after ordering by frequency 
d.resize_respect_freq(6000)

#top 5000 words
with open("./data/5000.txt", 'w') as f:
    ordered_list = d.Bags.get_top(5000)
    counter = 0
    print (counter)
    for bag in ordered_list:
        max_freq = -1
        most_freq_word = None
        for w in bag:
            freq = d[w][2]
            if freq > max_freq:
                most_freq_word = w
                max_freq = freq
        f.write(d.word(most_freq_word) + '\n')
        counter += 1
        if counter > 5000:
            break


def rank_sentence(sentence, translation):
    #TODO removed: re.findall("[A-Za-z]+", sentence) 
    #TODO \W+ can consider some charachters as words like maybe _. check that!
    words = re.split('\W+', sentence)
    translated_words = re.split('\W+', translation)
    max_order = 0
    intersection = set(words) & set(translated_words)
    for w in words:
        if w in d:
           order = d[w][0].order
           if order > max_order:
               max_order = order
        elif len(w) > 3 and w not in intersection:
            #reaching hear means the sentence contains unrecognized word (not in the list) and it's not proper noun
            return None
    return max_order


#TODO this corpora location is unusual
corpus_subtitles = "./data/corpus/corpus_subtitle/opensup_moses/OpenSubtitles.de-en.de"
subtitles_rankin = "./data/corpus/corpus_subtitle/opensup_moses/ranking.de"
en_corpus_subtitles = "./data/corpus/corpus_subtitle/opensup_moses/OpenSubtitles.de-en.en"
corpus_subtitles_outfolder = "./data/corpus/corpus_subtitle/opensup_moses/output/"
subtitles= corpus_subtitles, subtitles_rankin, en_corpus_subtitles, corpus_subtitles_outfolder
#
corpus_paraCrawl = "./data/corpus/corpus_paraCrawl/ParaCrawl.de-en.de"
paraCrawl_ranking = "./data/corpus/corpus_paraCrawl/ranking.de"
en_corpus_paraCrawl = "./data/corpus/corpus_paraCrawl/ParaCrawl.de-en.en"
corpus_outfolder_paraCrawl = "./data/corpus/corpus_paraCrawl/output" 
paraCrawl = corpus_paraCrawl, paraCrawl_ranking, en_corpus_paraCrawl, corpus_outfolder_paraCrawl
#
corpus_EUbooks = "./data/corpus/corpus_EUbooks/EUbookshop.de-en.de"
EUbooks_ranking = "./data/corpus/corpus_EUbooks/ranking.de"
en_corpus_EUbooks = "./data/corpus/corpus_EUbooks/EUbookshop.de-en.en"
corpus_outfolder_EUbooks =  "./data/corpus/corpus_EUbooks/output"
EUBooks = corpus_EUbooks, EUbooks_ranking, en_corpus_EUbooks, corpus_outfolder_EUbooks
import os

fsentences, frank_sentences , f_eng_sentences , f_output_folder = paraCrawl
#
#Find a sentence
with open(fsentences, 'r') as f:
    with open(f_eng_sentences, 'r') as f_eng:
        line_counter = 0
        for line in f:
            line_counter += 1
            eng_line = f_eng.readline()
            rank = rank_sentence(line, eng_line)
            if rank:
                with open(os.path.join(f_output_folder, str(rank) + ".exmp"), 'a') as fout:
                    fout.write(line) #new-line 
                    fout.write(str(line_counter) + "|" + eng_line) #new-line 
        
#TODO 
f_word_data_output= "./data/output/"

for bag in self.Bags.list:
    for key in bag.set:
        order = d[key][0].order
        with open(os.path.join(f_word_data_output,str(order)+ ".word" , 'w') as f:
                f.write(


