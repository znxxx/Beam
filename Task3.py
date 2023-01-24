class LRUcache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.values = {}

    def get(self,key):
        if key not in self.values:
            return -1
        else:
            requested = self.values.pop(key)
            return requested
    def put(self,key,value):
        if key in self.values:
            self.values[key] = value
        else:
            if len(self.values) < self.capacity:
                self.values[key] = value
            else:
                leftmost = list(self.values.keys())[0]
                self.values.pop(self.values[leftmost])
                self.values[key] = value

#This code time complexity of both method is Big-O(1) because there is only if-else statements
