def binary_search(arr, item):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r-l)//2
        if(arr[mid] == item): return mid
        elif(arr[mid]>item): r = mid - 1
        else: l = mid + 1
    return -1

def test():
    assert binary_search([1,2,3], 4) == -1

    import random
    for n in range(1,6):
        arr = [i for i in range(n)]
        print(arr)
        for i in range(n):
            assert binary_search(arr, i) == i

def main():
    import sys
    def read_arr(s):
        _, *l = list(map(int, (s.split())))
        return l
    reader = (s for s in sys.stdin)
    arr = read_arr(next(reader))
    check_arr = read_arr(next(reader))
    results = [binary_search(arr, i) for i in check_arr]
    results = [r + 1 if r > -1 else r for r in results]
    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()
    # test()