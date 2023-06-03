class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ChainingDictionary:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        chain = self.table[index]

        for item in chain:
            if item.key == key:
                item.value = value
                return

        chain.append(KeyValuePair(key, value))

    def find(self, key):
        index = self._hash_function(key)
        chain = self.table[index]

        for item in chain:
            if item.key == key:
                return item.value

        return None

    def delete(self, key):
        index = self._hash_function(key)
        chain = self.table[index]

        for i, item in enumerate(chain):
            if item.key == key:
                chain.pop(i)
                return

    def display(self):
        for index, chain in enumerate(self.table):
            print(f"Index {index}: ", end="")
            for item in chain:
                print(f"[{item.key}: {item.value}]", end=" -> ")
            print("None")


class ChainingDictionaryWithReplacement:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        if self.table[index] is None:
            self.table[index] = KeyValuePair(key, value)
        else:
            while self.table[index].key != key:
                index = (index + 1) % self.size

            self.table[index].value = value

    def find(self, key):
        index = self._hash_function(key)

        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value

            index = (index + 1) % self.size

        return None

    def delete(self, key):
        index = self._hash_function(key)

        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index] = None
                return

            index = (index + 1) % self.size

    def display(self):
        for index, item in enumerate(self.table):
            if item is not None:
                print(f"Index {index}: [{item.key}: {item.value}]")
            else:
                print(f"Index {index}: None")





# ChainingDictionary example
dictionary = ChainingDictionary(10)

dictionary.insert("apple", 5)
dictionary.insert("banana", 7)
dictionary.insert("orange", 3)
dictionary.insert("grape", 2)

print(dictionary.find("apple"))  # Output: 5
print(dictionary.find("grape"))  # Output: 2
print(dictionary.find("melon"))  # Output: None
