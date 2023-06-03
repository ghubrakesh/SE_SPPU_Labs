import heapq

# Example list of student marks
marks = [78, 92, 85, 76, 88, 90, 81]

# Create a min-heap and a max-heap
min_heap = marks.copy()
max_heap = [-mark for mark in marks]

heapq.heapify(min_heap)
heapq.heapify(max_heap)

# Retrieve the minimum and maximum marks
min_mark = heapq.heappop(min_heap)
max_mark = -heapq.heappop(max_heap)

print("Minimum marks:", min_mark)
print("Maximum marks:", max_mark)









# or






















# Example list of student marks
marks = [78, 92, 85, 76, 88, 90, 81]

# Manually implement min-heap and max-heap
def build_min_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(array, n, i)

def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)

def min_heapify(array, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] < array[smallest]:
        smallest = left

    if right < n and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, n, smallest)

def max_heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, n, largest)

# Build the min-heap and max-heap
build_min_heap(marks)
build_max_heap(marks)

# Retrieve the minimum and maximum marks
min_mark = marks[0]
max_mark = marks[-1]

print("Minimum marks:", min_mark)
print("Maximum marks:", max_mark)
