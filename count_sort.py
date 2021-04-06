import sys

def count_sort(elems, unique_count):
    counters = [0] * unique_count
    for elem in elems:
        counters[elem] += 1
    result = []
    for number in range(len(counters)):
        if(counters[number] != 0):
            for _ in range(counters[number]):
                result.append(number)
    return result

def count_sort_with_order(elems, unique_count):
    '''sort with saving order'''
    counters = [0] * unique_count
    for elem in elems:
        counters[elem] += 1
    for i in range(1, len(counters)):
        counters[i] += counters[i-1]
    result = [0] * len(elems)
    for i in reversed(range(len(elems))):
        elem = elems[i]
        result[counters[elem]-1] = elem
        counters[elem] -= 1
    return result

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    read_arr(next(reader))
    numbers = read_arr(next(reader))
    result = count_sort_with_order(numbers, 10)
    print(*result)

if __name__ == "__main__":
    main()