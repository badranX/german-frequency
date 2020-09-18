from functools import total_ordering
from grammar import Part
from CaseInsensitiveDict import CaseInsensitiveDict

@total_ordering
class Bag():
    #TODO, the hash value is the first integer representation of "word" from *args. Is this reasonable?
    def __init__(self, *args):
        self.set = set(*args)
        self.frequency = 0
        self.order = 0
        self.hash = args[0][0]
    def __lt__(self, other):
        return self.frequency < other.frequency
    def union(self, other):
        #TODO should I call del(self.set or other)
        tmp = other.set
        self.set = self.set.union(tmp)

    def __hash__(self):
        #it assumes that Bags is a partition of the words
        #Thus any word is uniqu to the set
        #These words are ints
        return self.hash
    def __iter__(self):
        return iter(self.set)


class Bags():
    def __init__(self, *args):
        super().__init__(*args)
        self.list = None
        self.set = set()
        self.counter = 0
    def discard(self, bag):
        self.set.discard(bag)
    def add(self, bag):
        self.set.add(bag)
    #add to bag1 and discard bag2
    #TODO better design ppl will miss bag2 is discarded
    def unite(self,bag1, bag2):
        bag1.union(bag2)
        self.discard(bag2)
    #After loading frequencies
    def load_order(self):
        if self.set:
            tmp = sorted(list(self.set), key= lambda v: v.frequency , reverse = True)
            counter = 1
            for x in tmp:
                x.order = counter
                counter += 1
            self.list = tmp
            del(self.set)
        else:
            pass
            #TODO check for bugs
            #order has been done
    def __contains__(self, item):
        if self.set:
            return item in self.set
        if self.list:
            return item in self.list
    def get_top(self, num):
        tmp = self.list
        #TODO
        #if self.set:
        #    tmp = sorted(list(self.set), key= lambda v: v.frequency , reverse = True)
        return tmp[0:num]
    #Reduce the sise of Bags to "new_size", leaves the most frequent ones
    def resize(self, new_size):
        tmp = self.list
        self.list = tmp[0:new_size]
        del(tmp)
    

class Words():
    #3 dictionaries d,indexer, and reversed_indexer. Handling them via Words() is the right way to gurantee case-insensitivity and keeping the keys with the right case. Apple will be saved Apple but apple will return what Words["Apple"] return
    def __init__(self, *args):
        super().__init__(*args)
        self.indexer = {}
        #reversed_indexer will be populated after calling resize_respect_freq() for fast reverse indexing in method word()
        self.reversed_indexer = {}
        self.d = {}
        self.Bags = Bags()
        self.counter = 0
    
    def __contains__(self,  key):
        if isinstance(key, int):
            return key in self.d
        else:
            return key in self.indexer

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.d[key]
        else:
            return self.d[self.indexer[key]]

    def __setitem__(self, key, val):
        if isinstance(key, int) :
            assert(key in self.d)
            self.d[key] = val
        else:
            #key = key.lower()
            if key in self.indexer: 
                self.d[self.indexer[key]] = val
            else:
                self.indexer[key] = self.counter
                self.d[self.counter] = val
                self.counter += 1

    def add_empty(self, word):
        assert(not isinstance(word, int))
        assert(word not in self)
        self[word] = None
        bag = Bag([self.indexer[word]])
        self[word] =  [bag, False, 0]
        self.Bags.add(bag)

    def part_of_speach(self, word):
        return self[word][1]
    def set_speach_part(self,word):
        self[word][1] = True

    def combine_bags(self, word1, word2):
        #word1_lower = word1.lower()
        #word2_lower = word2.lower()
        
        #if word1_lower == word2_lower: #this is not needed but a small optemization
        #    return
        #TODO warning two equal words cause a bug
        if word1 in self:
            bag1 = self[word1][0]
        else:
            raise Exception("it's a bag, so it should be indexed before calling this")
        if word2 in self:
            bag2 = self[word2][0]
        else:
            raise Exception()
        #TODO this has no need sofar
        if not bag1 or not bag2:
            raise Exception("one of the bag is None")
        if bag1 == bag2:
            return
        #bag2 will be delete from Bags after unite
        self.Bags.unite(bag1, bag2)
        for x in bag1.set:
            self[x][0] = bag1

    #TODO change word to str or somehting
    #returns the string of the word. The key in self.indexer from the value
    def word(self, key):
        #using Python 3.7 gurantees for the "dict"to have ordered keys
        if len(self.reversed_indexer) > 0:
            return self.reversed_indexer[key]
        return list(self.indexer.keys())[key]
    def bag_to_str(self, key):
        l = list(self.indexer.keys())
        return {l[i] for i in self[key][0].set}

    def bag(self, key):
        return self[key][0]
    def frequency(self, key):
        return self[key][2]

    #populate frequency values ,. afte that it calls Bags.load_order to change self.Bags to list of ordered by frequency
    def load_frequencies(self, from_file, out_notfound_file):
        with open(from_file, 'r') as f:
            with open(out_notfound_file, 'w') as tmp_file:
                for line in f:
                    line = line.strip()
                    words = line.split(' ')
                    if len(words) == 1:
                        print(words[0], " has no frequency")
                        continue
                    word = words[0]
                    frequency = int(words[1])
                    #TODO check for multiple occurence...don't remove already registerd frequency
                    if word in self:
                        self[word][0].frequency += frequency #the frequency belong to the set
                        self[word][2] = frequency
                    else:
                        tmp_file.write(word + '\t' + str(frequency) + "\n")
            self.Bags.load_order()


    #TODO is this obselet?
    def get_most_frequent_in_bag(self, bag):
        maximum = -1
        result = None
        for x in bag.set:
            frequency = self.frequency(x)
            if frequency > maximum:
                maximum = frequency
                result = x
            return (x, maximum)

    #TODO must be used only after ordering by frequency
    def resize_respect_freq(self, new_size):
        reverse_map = dict((reversed(item) for item in self.indexer.items()))
        for bag in self.Bags.list[new_size :]:
            for key in bag.set:
                #TODO bags are disjoint and key should exist in self.d
                if key not in self.d and key not in reverse_map:
                    continue
                tmp = reverse_map[key]
                if tmp in self.indexer:#TODO IMPORTANT: this is a bug it should exist
                    del self.indexer[tmp]
                del self.d[key]
                del reverse_map[key]
            del bag
        self.Bags.resize(new_size)
        self.reversed_indexer =reverse_map  
