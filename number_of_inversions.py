import sys

class Arr():
    def __init__(self, arr):
        self.arr = arr
        self.index = 0
    
    def is_finished(self):
        return self.index == len(self.arr)
    
    def get_current(self):
        return self.arr[self.index]

    def pop(self):
        res = self.get_current()
        self.index += 1
        return res

    def __len__(self):
        return len(self.arr) - self.index

def fast_merge(first, second):
    f_ind, s_ind = 0, 0
    result, inversions = [], 0
    
    f_is_finished, s_is_finished = False, False

    while True:
        f_is_finished, s_is_finished = f_ind == len(first), s_ind == len(second)
        if(f_is_finished and s_is_finished): break
        f_item = None if f_is_finished else first[f_ind]
        s_item = None if s_is_finished else second[s_ind]
        if(f_is_finished): result.append(s_item); s_ind += 1
        elif(s_is_finished or f_item <= s_item): result.append(f_item); f_ind += 1
        else: result.append(s_item); s_ind += 1; inversions += len(first) - f_ind
    return result, inversions

def merge(arr1, arr2):
    first, second = Arr(arr1), Arr(arr2)
    result, inversions = [], 0
    def add(item):
        result.append(item.pop())

    while not (first.is_finished() and second.is_finished()):
        if(first.is_finished()): add(second)
        elif(second.is_finished()): add(first)
        elif(first.get_current() <= second.get_current()): add(first)
        else: add(second); inversions += len(first)
    return result, inversions

def merge_sort(arr):
    l, r = 0, len(arr) - 1
    if(l == r): return arr, 0
    m = l + (r - l) // 2 
    first, inv1 = merge_sort(arr[l:m+1])
    second, inv2 = merge_sort(arr[m+1:r+1])
    res, inv = fast_merge(first, second)
    return res, inv1 + inv2 + inv

def test():
    from utils import timed_min
    # assert merge_sort([2, 3, 9, 2, 9])[1] == 2
    # assert merge_sort([4, 3, 2, 1])[1] == 6
    # assert merge_sort([4, 3, 2, 5, 1])[1] == 7
    # assert merge_sort([1])[1] == 0
    # assert merge_sort([1, 2, 3])[1] == 0
    arr = list(reversed(range(100000)))
    print(timed_min(merge_sort, arr))

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    next(reader)
    arr = read_arr(next(reader))
    _, inversions = merge_sort(arr)
    print(inversions)

if __name__ == "__main__":
    # main()
    test()