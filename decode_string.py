def read_two_numbers():
    return tuple(map(int, input().split()))

def main():
    k, _ = read_two_numbers()
    codes = {}
    for _ in range(0,k):
        s = input()
        codes[s[3:-1]] = s[0]
    string = input()
    curr_str, result = "", ""
    for ch in string:
        curr_str += ch
        sym = codes.get(curr_str)
        if(sym): 
            result += sym
            curr_str = ""
    print(result)

if __name__ == "__main__":
    f = open('decode_string_test.txt', 'r')
    input = f.readline
    main()
    f.close()
