class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

class NamedCounter(Counter):
    def __init__(self, name):
        super().__init__()
        self.name = name

c1 = Counter()
c2 = NamedCounter("First")
c3 = Counter()
c4 = NamedCounter("Second")

print(Counter.count)