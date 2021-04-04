import sys
import random
from operator import itemgetter

def quick_sort_3(arr, l, r):
    if(l >= r): return arr
    if(l + 1 == r): 
        if(arr[l] > arr[r]): arr[l], arr[r] = arr[r], arr[l]
        return arr
    ind = random.randint(l, r)
    x = arr[ind]
    arr[l], arr[ind] = arr[ind], arr[l]
    lt_bound, eq_bound = l, l
    for i in range(l+1, r+1):
        if(arr[i] < x): 
            lt_bound += 1
            eq_bound += 1
            if(lt_bound == eq_bound): arr[lt_bound], arr[i] = arr[i], arr[lt_bound]
            else: arr[lt_bound], arr[i], arr[eq_bound] = arr[i], arr[eq_bound], arr[lt_bound]
        elif(arr[i] == x and eq_bound < r):
            eq_bound += 1
            arr[i], arr[eq_bound] = arr[eq_bound], arr[i]
    arr[l], arr[lt_bound] = arr[lt_bound], arr[l]
    quick_sort_3(arr, l, lt_bound - 1)
    quick_sort_3(arr, eq_bound + 1, r)
    return arr

def binary_search_max_le(arr, l, r, item):
    result = -1
    while l<=r:
        mid = (l+r)//2
        if(arr[mid] <= item): l, result = mid + 1, mid
        else: r = mid - 1
    return result
    
def binary_search_max_lt(arr, l, r, item):
    result = -1
    while l<=r:
        mid = (l + r)//2
        if(arr[mid] < item): l, result = mid + 1, mid
        else: r = mid - 1
    return result

def count_segments(dots, l, r, begins, b_l, b_r, ends, e_l, e_r):
    if(l > r): return
    mid = (l + r)//2
    item = dots[mid]
    begin = binary_search_max_le(begins, max(0, b_l), b_r, item[1])
    end = binary_search_max_lt(ends, max(0, e_l), e_r, item[1])
    item[2] = abs(begin - end)
    count_segments(dots, l, mid - 1, begins, b_l, begin, ends, e_l, end)
    count_segments(dots, mid + 1, r, begins, begin, b_r, ends, end, e_r)

def get_dots_belonging(segments, dots):
    l, r = 0, len(segments) - 1
    begins, ends = [], []
    for beg,end in segments: begins.append(beg); ends.append(end)
    quick_sort_3(begins, l, r)
    quick_sort_3(ends, l, r)
    dots_sorted = sorted([[i,dots[i],0] for i in range(len(dots))], key=itemgetter(1))
    count_segments(dots_sorted, 0, len(dots) - 1, begins, l, r, ends, l, r)
    return list(map(itemgetter(2), sorted(dots_sorted, key=itemgetter(0))))

def ass(actual, expected):
    try:
        assert actual == expected
    except:
        print(actual, expected)
        raise

def test():
    implementation = get_dots_belonging
    ass(implementation(\
        [[10, 10],[3, 9],[4, 5],[3, 6],[1, 8],[2, 2],[7, 10],[7, 8],[10, 10],[0, 9]],\
        [3,2,0,10,1,8,1,9,6,2]),\
            [4,3,1,3,2,5,2,3,4,3])
    ass(implementation([[0,5],[7,10]], [1]), [1])
    ass(implementation([[1,5],[2,6],[3,4],[0,7]], list(reversed([0,1,2,3,4,5,6,7,8]))), [0,1,2,3,4,4,3,2,1])
    ass(implementation([[1,3],[2,4]], [0,1,2,3,4,5]), [0,1,2,2,1,0])
    ass(implementation([[0,2],[8,10]],[1,3,5,8]), [1,0,0,1])
    print('all tests succeded')

def generate_test_data_random():
    import random
    n = 50000
    max_number = 1000000
    segments = []
    for _ in range(n):
        beg = random.randint(0, max_number) 
        end = random.randint(beg, max_number) 
        segments.append([beg, end])
    random.shuffle(segments)
    dots = [random.randint(0 , max_number) for _ in range(n)]
    random.shuffle(dots)
    return segments, dots

def performance():
    from utils import timed_min
    data = generate_test_data_random()
    generate_test_file(*data)
    print(timed_min(get_dots_belonging, *data, n_iter=5))
    
def generate_test_file(segments, dots):
    with open('dots_and_segments_test.txt','w') as file:
        file.writelines([f'{len(segments)} {len(dots)}\n'] + \
            [f'{beg} {end}\n' for beg,end in segments] + \
            [' '.join(map(str, dots))])

def test_quick_sort():
    sort = quick_sort_3
    ass(sort([1], 0, 0),[1])
    ass(sort([2,1], 0, 1),[1,2])
    ass(sort([2,1,1], 0, 2),[1,1,2])
    ass(sort([2,1,3], 0, 2),[1,2,3])
    ass(sort([3,2,1,4], 0, 3),[1,2,3,4])
    ass(sort([3,2,1,1], 0, 3),[1,1,2,3])
    ass(sort([3,2,1,3,1], 0, 4),[1,1,2,3,3])
    ass(sort([3,2,1,2,3,1], 0, 5),[1,1,2,2,3,3])
    print('all tests succeeded')

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    n, _ = read_arr(next(reader))
    segments = [read_arr(next(reader)) for _ in range(n)] 
    dots = read_arr(next(reader))
    result = get_dots_belonging(segments, dots)
    print(' '.join([str(i) for i in result]))
    counter = 0
    for i in result: counter += i
    print(counter)

if __name__ == "__main__":
    # main()
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    elif(mode == 'test_sort'): test_quick_sort()
    elif(mode == 'gen_test_file'): generate_test_file(*generate_test_data_random())
    else: 
        from utils import timed_min
        print(timed_min(main, n_iter=1))