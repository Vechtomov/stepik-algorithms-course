import operator

def get_result(s):
    frequencies = {}
    for ch in s: frequencies[ch] = frequencies.setdefault(ch, 0) + 1
    sorted_freq = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)
    codes = []
    for item in sorted_freq:
        if (len(codes) == 0): res = '0'
        else:
            prev_value = codes[-1][1]
            res = prev_value[:-1] + '1' if len(codes) == len(sorted_freq) - 1 else '1' + prev_value
        codes.append((item[0], res))
    codes = dict(codes)
    return codes, ''.join([codes[ch] for ch in s])

def main():
    codes, encoded_s = get_result(input())
    print(len(codes), len(encoded_s))
    for key, code in codes.items(): print(f'{key}: {code}')
    print(encoded_s)

if __name__ == "__main__":
    f = open('haffman_test.txt', 'r')
    input = f.readline
    main()
    f.close()
