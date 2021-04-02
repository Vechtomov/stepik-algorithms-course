import sys
import math

class PriorityQueue():
    def __init__(self, comparisonFunc = None, arr = []):
        self.arr = arr
        self.comparisonFunc = comparisonFunc if comparisonFunc else lambda x: x

    def insert(self, value):
        self.arr.append(value)
        self._siftUp(len(self.arr) - 1)
        print(self.arr)

    def pop(self):
        value = self.arr[0]
        self.arr[0] = self.arr[len(self.arr) - 1]
        del self.arr[len(self.arr) - 1]
        if(len(self.arr) > 1): self._siftDown(0)
        return value

    def _siftUp(self, index):
        if(index == 0): return
        parent_index = int(math.ceil(index / 2)) - 1
        parent_val, val = self.arr[parent_index], self.arr[index]
        if(self.arr[parent_index] >= self.arr[index]): return 
        self.arr[parent_index], self.arr[index] = val, parent_val
        self._siftUp(parent_index)

    def _siftDown(self, index):
        indexes = [index, 2 * index + 1, 2 * index + 2]
        values = [(i, self.arr[i]) for i in indexes if i < len(self.arr)]
        max_value_index, max_value = max(values, key=lambda x: x[1])
        if(len(values) < 2 or max_value_index == index): return
        self.arr[index], self.arr[max_value_index] = max_value, self.arr[index]
        self._siftDown(max_value_index)


def test():
    q = PriorityQueue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    assert q.pop() == 3
    assert q.pop() == 2
    assert q.pop() == 1


def main():
    reader = (s for s in sys.stdin)
    n = int(next(reader))
    queue = PriorityQueue()
    for _i in range(n):
        splitted = next(reader).split()
        if (len(splitted) == 1): print(queue.pop())
        else: queue.insert(int(splitted[1]))
    
if __name__ == "__main__":
    # main()
    test()