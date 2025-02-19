import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_index = {}  # Stores value -> index mapping
        self.values = []  # Stores values for O(1) getRandom()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the value was not present.
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_index:
            return False  # Value already exists
        
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the value was present.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index:
            return False  # Value not in set
        
        # Swap with the last element for O(1) removal
        last_val = self.values[-1]
        index = self.val_to_index[val]
        self.values[index] = last_val
        self.val_to_index[last_val] = index

        # Remove last element
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.values)
