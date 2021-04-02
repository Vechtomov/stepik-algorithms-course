import operator
def get_dots(all_segments):
    sorted_segments = sorted(all_segments, key=operator.itemgetter(1))
    result = [sorted_segments[0][1]]
    for beg, end in sorted_segments:
        if (beg > result[-1]):
            result.append(end)
    return result

def main():
    n = int(input())
    all_segments = []
    for i in range(n):
        all_segments.append(tuple(map(int, input().split())))
    dots = get_dots(all_segments)
    print(len(dots))
    print(' '.join(map(str, dots)))

if __name__ == "__main__":
    f = open('optimize_dots_test.txt', 'r')
    input = f.readline
    main()
    f.close()
