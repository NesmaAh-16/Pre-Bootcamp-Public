class Underscore:
    def map(self, iterable, callback):
        new_list = []
        for item in iterable:
            new_list.append(callback(item))
        return new_list

    def find(self, iterable, callback):

        for item in iterable:
            if callback(item):
                return item
        return None 

    def filter(self, iterable, callback):

        new_list = []
        for item in iterable:
            if callback(item):
                new_list.append(item)
        return new_list

    def reject(self, iterable, callback):

        new_list = []
        for item in iterable:
            if not callback(item):
                new_list.append(item)
        return new_list

_ = Underscore() 


print("Map result:   ", _.map([1, 2, 3], lambda x: x * 2))
print("Find result:  ", _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))
print("Filter result:", _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
print("Reject result:", _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))