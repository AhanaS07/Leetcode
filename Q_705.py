#Design HashSet
#Hash Table

class MyHashSet(object):

    def __init__(self):
        self.data = set()

    def add(self, key):
        self.data.add(key)    

    def remove(self, key):
        self.data.discard(key)
        
    def contains(self, key):
        return key in self.data
