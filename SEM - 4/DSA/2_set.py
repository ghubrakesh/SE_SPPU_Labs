class Set:
    def __init__(self):
        self.items = []

    def add(self, element):
        if element not in self.items:
            self.items.append(element)

    def remove(self, element):
        if element in self.items:
            self.items.remove(element)

    def contains(self, element):
        return element in self.items

    def size(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def intersection(self, other_set):
        intersection_set = Set()

        for item in self.items:
            if other_set.contains(item):
                intersection_set.add(item)

        return intersection_set

    def union(self, other_set):
        union_set = Set()

        for item in self.items:
            union_set.add(item)

        for item in other_set:
            union_set.add(item)

        return union_set

    def difference(self, other_set):
        difference_set = Set()

        for item in self.items:
            if not other_set.contains(item):
                difference_set.add(item)

        return difference_set

    def subset(self, other_set):
        for item in self.items:
            if not other_set.contains(item):
                return False

        return True
