import sys

def lds(arr):
    d = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] <= arr[j] and d[j] >= d[i]:
                d[i] = d[j] + 1
    max_ind = 0
    for i in range(1, len(d)):
        if d[i] > d[max_ind]: max_ind = i

    result = [max_ind]
    ind = max_ind
    for i in reversed(range(max_ind)):
        if d[i] == d[ind] - 1 and arr[i] >= arr[ind]:
            result.append(i)
            ind = i

    return list(reversed(result))

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    read_arr(next(reader))
    arr = read_arr(next(reader))
    result = lds(arr)
    print(len(result))

def test():
    from utils import are_equal
    are_equal(lds([1]), [0])
    are_equal(lds([1,1,3]), [0,1])
    are_equal(lds([2,1]), [0,1])
    are_equal(lds([3,2,4,1]), [0,1,3])
    are_equal(lds([3,2,1,100,10,9,90,20,19,80,130,140,70,150,160,60]), [3,6,9,12,15])
    print('all tests succeeded')

def performance():
    from utils import timed_min
    data = generate_test_data()
    generate_test_file(data)
    print(timed_min(lds, data, n_iter=2))
    
def generate_test_data():
    import random
    n = 10 ** 4
    max_number = 10 ** 9
    return [random.randint(0 , max_number) for _ in range(n)]

def generate_test_file(arr):
    from utils import generate_test_file as generate
    generate('LDS_test.txt', [f'{len(arr)}\n'] + [' '.join(map(str, arr))])

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    else: 
        from utils import timed_min
        print(timed_min(main, n_iter=1))