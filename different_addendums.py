def get_different_addendums(n):
    result, i = [], 1
    while n > 0:
        addendum = i if n - i > i else n
        n -= addendum
        result.append(addendum)
        i += 1
    return result

def read_number():
    return int(input())

def main():
    n = read_number()
    addendums = get_different_addendums(n)
    print(len(addendums))
    print(' '.join(map(str, addendums)))

if __name__ == "__main__":
    main()
