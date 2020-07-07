import re

from dataclasses import dataclass
from typing import List
@dataclass
class WordStat():
    def __init__(self, word, frequency, order, overall_order =0, components=None):
        self.frequency = frequency
        self.order = order
        self.overall_order =  overall_order
        self.components = components
        self.word = word

class Parser():
    def __init__(self, dictionary):
        self.d = dictionary

    def search_binded_words(self, word):
        word = word.lower()
        if len(word) < 8:
            return None, None, None
        #assuming word is at least 4 char long
        for i in range(4, len(word)-3):
            erst = word[0:i]
            second = word[i:]
            #TODO what if both are possible
            if second[0] == 's' and erst in self.d and second[1:] in self.d:
                return (erst, second[1:], True)
            if erst in self.d and second in self.d:
                return (erst, second, False)
        return None, None, None

    def search_dict(self, word):
        word = word.lower()
        erst, second, _ = self.search_binded_words(word)
        if word not in self.d and not erst: #last implies not second
            return None

        components_order = 0
        components = None
        freq = 0
        order = 0
        if word in self.d:
            freq = self.d.bag(word).frequency
            order = self.d.bag(word).order

        if erst and second:
            erst_stat = WordStat( erst, self.d.bag(erst).frequency, self.d.bag(erst).order)
            second_stat = WordStat(second, self.d.bag(second).frequency, self.d.bag(second).order) 
            components = [erst_stat, second_stat]
            components_order = max(erst_stat.order, second_stat.order) 

        wordstat = WordStat(word, freq, order, components=components)
        if order == 0 or components_order == 0:
            wordstat.overall_order = max(components_order, wordstat.order)
        else:
            wordstat.overall_order = min(components_order, wordstat.order)
        return wordstat

    def parse (self, input_file, output_file):
        recognized = set()
        unrecognized = set()
        with open(input_file, 'r') as f:
                for line in f:
                    words = re.split('\W+', line)
                    words = list(set(words))
                    for w in words:
                        stats = self.search_dict(w)
                        if stats:
                            order = stats.overall_order
                            if stats.components:
                                w = w + " : " + stats.components[0].word + " , " + stats.components[1].word
                            recognized.add((w, order))
                        else:
                            unrecognized.add(w)
        with open(output_file, 'w') as f_out:
            ordered_words = sorted(recognized, key=lambda v: v[1], reverse = True)
            for w in ordered_words:
                f_out.write(w[0] + ' ' + str(w[1]) + '\n')
            for w in unrecognized:
                f_out.write(w + ' ' + '!!!!!!' + '\n')
