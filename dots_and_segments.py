import sys
import random

# def quick_sort(arr, l, r):
#     if(l >= r): return arr
#     if(l + 1 == r): 
#         if(arr[l] > arr[r]): arr[l], arr[r] = arr[r], arr[l]
#         return arr
#     ind = random.randint(l, r)
#     x = arr[ind]
#     arr[l], arr[ind] = arr[ind], arr[l]
#     bound = l
#     for i in range(l+1,r+1):
#         if(arr[i] <= x): 
#             bound += 1
#             arr[bound], arr[i] = arr[i], arr[bound]
#     arr[l], arr[bound] = arr[bound], arr[l]
#     quick_sort(arr, l, bound - 1)
#     quick_sort(arr, bound + 1, r)
#     return arr

def quick_sort_eliminated(arr, l, r):
    while l < r:
        if(l + 1 == r): 
            if(arr[l] > arr[r]): arr[l], arr[r] = arr[r], arr[l]
            return arr
        ind = random.randint(l, r)
        x = arr[ind]
        arr[l], arr[ind] = arr[ind], arr[l]
        bound = l
        for i in range(l+1,r+1):
            if(arr[i] <= x): 
                bound += 1
                arr[bound], arr[i] = arr[i], arr[bound]
        arr[l], arr[bound] = arr[bound], arr[l]
        if(bound - l < r - bound): 
            quick_sort_eliminated(arr, l, bound - 1)
            l = bound + 1
        else:
            quick_sort_eliminated(arr, bound + 1, r)
            r = bound - 1

def binary_search_max_condition(arr, condition):
    l,r = 0, len(arr)-1
    result = -1
    counter = 0
    while l<=r:
        mid = l + (r-l)//2
        if(condition(arr[mid])): l, result = mid + 1, mid
        else: r = mid - 1
        counter += 1
    return result

def get_dots_belonging(segments, dots):
    l, r = 0, len(segments) - 1
    begins, ends = [], []
    for beg,end in segments: begins.append(beg); ends.append(end)
    quick_sort_eliminated(begins, l, r)
    quick_sort_eliminated(ends, l, r)
    result = []
    for d in dots:
        first_begin = binary_search_max_condition(begins, lambda x: x <= d)
        first_end = binary_search_max_condition(ends, lambda x: x < d)
        result.append(0 if first_begin == -1 else abs(first_begin - first_end))
    return result

def simple_implementation(segments, dots):
    result = []
    for d in dots:
        counter = 0
        for begin, end in segments:
            if(begin <= d and d <= end): counter += 1
        result.append(counter)
    return result

def ends_implementation(segments, dots):
    result = []
    for d in dots:
        begins = 0
        not_ends = 0
        for begin, end in segments:
            if(begin<=d): begins += 1
            if(end < d): not_ends += 1
        result.append(abs(begins - not_ends))
    return result

def test():
    from utils import perf_test
    import random
    
    implementation = get_dots_belonging
    assert implementation([[0,5],[7,10]], [1]) == [1]
    assert implementation([[1,3],[2,4]], [0,1,2,3,4,5]) == [0,1,2,2,1,0]
    assert implementation([[1,5],[2,6],[3,4],[0,7]], [0,1,2,3,4,5,6,7,8]) == [1,2,3,4,4,3,2,1,0]
    assert implementation([[0,2],[8,10]],[1,3,5,8]) == [1,0,0,1]
    print('all tests succeded')

    n = 50000
    def gen_segments():
        result = [[i,i+random.randint(i, i+n)] for i in range(n)]
        random.shuffle(result)
        return result
    segments = gen_segments()
    dots = range(n)
    print(perf_test(implementation, segments, dots, n_iter=5))
    
def test_quick_sort():
    sort = quick_sort_eliminated
    assert sort([1], 0, 0) == [1]
    assert sort([2,1], 0, 1) == [1,2]
    assert sort([2,1,3], 0, 2) == [1,2,3]
    assert sort([3,2,1,4], 0, 3) == [1,2,3,4]
    assert sort([3,2,1,1], 0, 3) == [1,1,2,3]

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    n, m = read_arr(next(reader))
    segments = [read_arr(next(reader)) for _ in range(n)] 
    dots = read_arr(next(reader))
    print(' '.join([str(i) for i in get_dots_belonging(segments, dots)]))

if __name__ == "__main__":
    # main()
    test()
    # test_quick_sort()