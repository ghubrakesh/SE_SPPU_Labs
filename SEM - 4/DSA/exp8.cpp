#include <iostream>
#include <vector>
using namespace std;

const int SIZE = 10;

class Heap {
public:
    int arr[SIZE];
    int length;

    Heap() {
        length = 0;
    }

    int getParentNode(int index) {
        return (index - 1) / 2;
    }

    void createHeap(int index) {
        if (index == 0) {
            return;
        }
        int parentIndex = getParentNode(index);
        if (arr[index] > arr[parentIndex]) {
            swap(arr[index], arr[parentIndex]);
            createHeap(parentIndex);
        }
    }

    void insert(int data) {
        if (length == SIZE) {
            cout << "Heap is full." << endl;
        } else {
            arr[length] = data;
            createHeap(length);
            length++;
        }
    }

    void display() {
        for (int i = 0; i < length; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    int getMax() {
        return arr[0];
    }

    int getMin() {
        if (length == 0) {
            cout << "Heap is empty." << endl;
            return -1;
        }
        int minVal = arr[0];
        for (int i = 0; i < length; i++) {
            if (arr[i] < minVal) {
                minVal = arr[i];
            }
        }
        return minVal;
    }
};

int main() {
    Heap heap;
    heap.insert(10);
    heap.insert(120);
    heap.insert(90);
    heap.insert(40);
    heap.insert(80);
    heap.insert(20);
    heap.insert(60);
    heap.insert(30);

    cout << "Marks: ";
    heap.display();
    cout << "Max: " << heap.getMax() << endl;
    cout << "Min: " << heap.getMin() << endl;

    return 0;
}
