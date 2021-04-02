import sys
import random

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

def binary_search_max_condition(arr, l, r, condition):
    result = -1
    while l<=r:
        mid = l + (r-l)//2
        if(condition(arr[mid])): l, result = mid + 1, mid
        else: r = mid - 1
    return result

def get_dots_belonging(segments, dots):
    l, r = 0, len(segments) - 1
    begins, ends = [], []
    for beg,end in segments: begins.append(beg); ends.append(end)
    quick_sort_eliminated(begins, l, r)
    quick_sort_eliminated(ends, l, r)
    result = []
    first_begin = first_end = 0
    dots_sorted = sorted([(i,dots[i]) for i in range(len(dots))], key=lambda x: x[1])
    for d in dots_sorted:
        first_begin = binary_search_max_condition(begins, max(0, first_begin), r, lambda x: x <= d[1])
        first_end = binary_search_max_condition(ends, max(0, first_end), r, lambda x: x < d[1])
        result_count = abs(first_begin - first_end)
        result.append((d[0], result_count))
    return [x[1] for x in sorted(result, key=lambda x: x[0])]

def ass(actual, expected):
    try:
        assert actual == expected
    except:
        print(actual, expected)
        raise

def test():
    implementation = get_dots_belonging
    ass(implementation([[0,5],[7,10]], [1]), [1])
    ass(implementation([[1,3],[2,4]], [0,1,2,3,4,5]), [0,1,2,2,1,0])
    ass(implementation([[1,5],[2,6],[3,4],[0,7]], list(reversed([0,1,2,3,4,5,6,7,8]))), [0,1,2,3,4,4,3,2,1])
    ass(implementation([[0,2],[8,10]],[1,3,5,8]), [1,0,0,1])
    print('all tests succeded')

def performance():
    from utils import perf_test
    import random

    n = 50000
    def gen_segments():
        result = [[i,i+random.randint(i, i+n)] for i in range(n)]
        random.shuffle(result)
        return result
    segments = gen_segments()
    dots = list(range(n))
    random.shuffle(dots)
    print(perf_test(get_dots_belonging, segments, dots, n_iter=5))
    
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
    import sys
    mode = sys.argv[1] if len(sys.argv) else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    else: main()