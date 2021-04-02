import operator
def get_segments(all_segments):
    sorted_segments = sorted(all_segments, key=operator.itemgetter(1))
    last_pos = 0
    result = []
    for beg, end in sorted_segments:
        if (beg < last_pos): continue;
        last_pos = end
        result.append((beg, end))
    return result


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(tuple(map(int, input().split())))
    segments = get_segments(arr)
    print(len(segments))
    for beg, end in segments: print(beg, end)

if __name__ == "__main__":
    f = open('segments_test.txt', 'r')
    input = f.readline
    main()
    f.close()
