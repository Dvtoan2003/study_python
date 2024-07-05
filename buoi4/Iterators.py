my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator))  # In ra 1
print(next(my_iterator))  # In ra 2
print(next(my_iterator))  # In ra 3


class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

counter = Counter(1, 3)
for number in counter:
    print(number) 