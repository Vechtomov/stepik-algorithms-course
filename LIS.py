import sys

def LISBottomUp(arr, compare):
    d = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if(compare(arr[i], arr[j]) and d[j] >= d[i]):
                d[i] = d[j] + 1
    return max(d)

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    read_arr(next(reader))
    arr = read_arr(next(reader))
    result = LISBottomUp(arr, lambda x,y: x%y == 0)
    print(result)

def test():
    from utils import are_equal
    compare = lambda x,y: x%y == 0
    are_equal(LISBottomUp([1], compare), 1)
    are_equal(LISBottomUp([1,1], compare), 2)
    are_equal(LISBottomUp([1,2], compare), 2)
    are_equal(LISBottomUp([1,2,1,1], compare), 3)
    are_equal(LISBottomUp([2,3], compare), 1)
    are_equal(LISBottomUp([2,4], compare), 2)
    are_equal(LISBottomUp([1,2,3,4], compare), 3)
    are_equal(LISBottomUp([1,3,2,3,4], compare), 3)

if __name__ == "__main__":
    main()
    # test()