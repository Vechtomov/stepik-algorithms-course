def get_result(total_volume, items):
    sorted_items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)
    result, volume, i = 0, 0, 0
    while volume < total_volume and i < len(items):
        p, v = sorted_items[i]
        left_volume = total_volume - volume
        possible_v = min(left_volume, v)
        volume += possible_v
        result += p * possible_v / v
        i += 1
    return result

def read_two_numbers():
    return tuple(map(int, input().split()))

def main():
    n, total_volume = read_two_numbers()
    items = [read_two_numbers() for i in range(n)]
    result = get_result(total_volume, items)
    print("{:.3f}".format(result))

if __name__ == "__main__":
    f = open('continuous_backpack_test.txt', 'r')
    input = f.readline
    main()
    f.close()
