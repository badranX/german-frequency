from enum import Enum
Part =  {
    "ANYTHING" : 0,
    "V":1 ,
    "ADJ":2,
    "ADV":3      ,
    "ART" :4     ,
    "CARD"  :5   ,
    "CIRCP" :6  ,
    "CONJ"  :7   ,
    "DEMO"  :8   ,
    "INDEF" :9   ,
    "INTJ"  :10   ,
    "ORD"   :11   ,
    "NN"    :12   ,
    "NNP"   :13   ,
    "POSS"  :14   ,
    "POSTP" :15   ,
    "PRP"   :16   ,
    "PREP"  :17   ,
    "PREPART" : 18,
    "PROADV"  :19 ,
    "PRTKL"   :20 ,
    "REL" : 21,
    "TRUNC"  :22  ,
    "VPART"  :23  ,
    "WPADV" :24,
    "WPRO" :25,
    "ZU" : 26}

Part_tmp = (
    "ANYTHING",
    "V" ,
    "ADJ",
    "ADV"      ,
    "ART"      ,
    "CARD"     ,
    "CIRCP"   ,
    "CONJ"     ,
    "DEMO"     ,
    "INDEF"    ,
    "INTJ"     ,
    "ORD"      ,
    "NN"       ,
    "NNP"      ,
    "POSS"     ,
    "POSTP"    ,
    "PRP"      ,
    "PREP"     ,
    "PREPART",
    "PROADV"   ,
    "PRTKL"    ,
    "REL",
    "TRUNC"    ,
    "VPART"    ,
    "WPADV",
    "WPRO",
    "ZU")


class Morph():
    def __init__(self, word, *args):
        self.word = word
        for i in range(0,len(args),2):
            self.original = args[i]
            self.to = args[i+1]

class Grammar():
    def __init__(self, dictionary):
        self.d = dictionary
        self.__suffixes = {Morph("bar"),
                Morph("haft"), 
                Morph("isch"),
                Morph("lich"),
                Morph("loss"),
                Morph("reich"),
                Morph("voll")}
        self.__connectors = {"e", "n", "en", "ens", "er", "s", "es", ""}

    def search_suffix(self, word):
        word = word.lower()
        for suf in  self.__suffixes:
            if len(word) - len(suf.word) < 4:
                continue
            if word[-len(suf.word):] == suf.word and word[:-len(suf.word)] in self.d:
                return word[:-len(suf.word)] , suf.word
        return word, None


    def search_binded_words(self, word):
        word = word.lower()
        if len(word) < 8:
            return []
        #assuming word is at least 4 char long
        for i in range(4, len(word)-3):
            erst = word[0:i]
            second = word[i:]
            #possible_components=[] TODO Not yet implemented , but returning first element
            #TODO what if both are possible
            for con in self.__connectors:
                #don't consider words less than chars after deducting the connector
                if len(second) - len(con) < 4:
                    continue
                if second[:len(con)] == con and erst in self.d and second[len(con):] in self.d:
                    if  self.d.part_of_speach(erst) and  self.d.part_of_speach( second[len(con):]):
                        return [erst, second[len(con):]]
        return []
    def compose(self, word):
        word = word.lower()
        word, suffix = self.search_suffix(word)
        components = self.search_binded_words(word)
        return components, suffix

