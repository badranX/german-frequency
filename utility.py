import pickle
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
def load_object(filename):
    with open(filename, 'rb') as input:
        tech_companies = pickle.load(input)
        return tech_companies


def get_bind_words(word, dictionary):
    if len(word) < 8:
        return None
    #assuming word is at least 4 char long
    for i in range(5, len(word)-5):
        erst = word[0:i]
        second = word[i:]
        if second[0] == 's' and erst in dictionary and second in dictionary:
            return (erst, second[1:])
        if erst in dictionary and second in dictionary:
            return (erst, second)
    return None


#mean and variance
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

