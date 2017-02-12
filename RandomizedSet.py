class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.indices = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            self.indices[val] = len(self.elements)
            self.elements.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            ind = self.indices.pop(val)
            endVal = self.elements.pop()
            if val != endVal:
                self.indices[endVal] = ind
                self.elements[ind] = endVal
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.elements[random.randint(0, len(self.elements) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
