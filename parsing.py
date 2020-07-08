import re
from grammar import *

class WordStat():
    def __init__(self, word, frequency, order, overall_order =0, components=None):
        self.frequency=frequency
        self.order=order
        self.overall_order= overall_order
        self.components=components
        self.word=word

class Parser():
    def __init__(self, dictionary):
        self.d=dictionary
        self.grammar=Grammar(dictionary)

    def search_dict(self, word):
        word=word.lower()
        words = self.grammar.compose(word)
        if len(words) == 0:
            return word
        for w in words:
            if w in self.d:
                components, suffix =self.grammar.search_roots(word)
        if not components or len(components)!=0:
            if word in self.d:
                return order, []
            else:
                return None, None

        max_order_in_components=0
        for w in components:
            component_order =  self.d.bag(w).order
            if max_order_in_components < component_order:
                max_order_in_components=component_order

        if order == 0 or max_order_in_components == 0:
            return max(max_order_in_components, order) , components   
        else:
            return min(max_order_in_components, order), components   

    def parse (self, input_file, output_file):
        recognized=set()
        unrecognized=set()
        with open(input_file, 'r') as f:
                for line in f:
                    words=re.split('\W+', line)
                    words=list(set(words))
                    for w in words:
                        components, suffix = self.grammar.compose(w)
                        if w in self.d:
                            order = self.d.bag(w).order

                            max_order = 0
                            for c in components:
                                order_comp = self.d.bag(c).order
                                if max_order < order_comp:
                                    max_order = order_comp
                                order = min(max_order, order)
                            for s in components:
                                w=w + " : " + s 
                            recognized.add((w, order))
                        else:
                            unrecognized.add(w)
        with open(output_file, 'w') as f_out:
            ordered_words=sorted(recognized, key=lambda v: v[1], reverse=True)
            for w in ordered_words:
                f_out.write(w[0] + ' ' + str(w[1]) + '\n')
            for w in unrecognized:
                f_out.write(w + ' ' + '!!!!!!' + '\n')
