### A bag is a set and an integer
class Bag(set):
    def __init__(self, *args):
        super().__init__(*args)
        self.frequency = 0
        self.order = 0
        self.index = 0
    def __del__(self, *args):
        super().__init__( *args)
    def union(self, *args):
        tmp = super().union( *args)
        return Bag(tmp)

class Bags(dict):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    def delete_bag(self, bag):
        if bag.index in self:
            del(self[bag.index])
    def add_bag(self, bag):
        bag.index = self.counter
        self[self.counter] = bag
        self.counter += 1


class Words(dict):
    def __init__(self, *args):
        super().__init__(self, *args)
        self.Bags = Bags()

    def add_empty_word(self, word):
        word= word.lower()
        if word in self:
            return
        bag = Bag({word})
        self.sset(word, [bag, 0])
        self.Bags.add_bag(bag)

    def combine_bags(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if word1 in self:
            bag1 = self.sget(word1)[0]
        else:
            raise Exception()
        if word2 in self:
            bag2 = self.sget(word2)[0]
        else:
            raise Exception()
        new_bag = bag1.union(bag2)
        self.Bags.add_bag(new_bag)
        for x in new_bag:
            self.sget(x)[0] = new_bag
        self.Bags.delete_bag(bag1)
        self.Bags.delete_bag(bag2)

    def sset(self, key, value):
        self[key.lower()] = value

    def sget(self, key):
        return self[key.lower()]
