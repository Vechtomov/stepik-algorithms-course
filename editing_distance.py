import sys

def editing_distance_recursive(a,b):
    a_len, b_len = len(a) + 1, len(b) + 1
    d = [[float('inf')] * a_len for _ in range(b_len)]
    def recursive(i,j):
        if d[j][i] != float('inf'): return d[j][i]
        if i == 0: d[j][i] = j
        elif j == 0: d[j][i] = i
        else:
            insert = recursive(i-1,j) + 1
            deletion = recursive(i,j-1) + 1
            change = recursive(i-1,j-1) + (0 if a[i-1] == b[j-1] else 1)
            d[j][i] = min(insert, deletion, change)
        return d[j][i]
    return recursive(a_len - 1, b_len - 1)

def editing_distance(a,b):
    a_len, b_len = len(a) + 1, len(b) + 1
    d = [[float('inf')] * a_len for _ in range(b_len)]
    for i in range(a_len): d[0][i] = i
    for i in range(b_len): d[i][0] = i
    for i in range(1, a_len):
        for j in range(1, b_len):
            insert = d[j][i-1] + 1
            deletion = d[j-1][i] + 1
            change = d[j-1][i-1] + (0 if a[i-1] == b[j-1] else 1)
            d[j][i] = min(insert, deletion, change) 
    return d[b_len - 1][a_len - 1]

def main():
    reader = (s for s in sys.stdin)
    a = next(reader)
    b = next(reader)
    result = editing_distance_recursive(a, b)
    print(result)

def test():
    from utils import are_equal
    # method = editing_distance
    method = editing_distance_recursive
    are_equal(method('a','a'), 0)
    are_equal(method('a','b'), 1)
    are_equal(method('abc','ab'), 1)
    are_equal(method('abc','bc'), 1)
    are_equal(method('abcd','bc'), 2)
    are_equal(method('abcde','beda'), 3)
    are_equal(method('editing','distance'), 5)
    print('all tests succeeded')

def performance():
    from utils import timed_min
    data = generate_test_data()
    generate_test_file(data)
    print(timed_min(editing_distance, *data, n_iter=2))
    
def generate_test_data():
    import random
    n = 100
    def rand_char(): return chr(random.randint(ord('a'),ord('z')))
    def rand_string(): 
        return ''.join([rand_char() for _ in range(n)])
    return rand_string(), rand_string()

def generate_test_file(data):
    from utils import generate_test_file as generate
    generate('editing_distance_test.txt', [f'{data[0]}\n'] + [f'{data[1]}\n'])

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    else: 
        from utils import timed_min
        print(timed_min(main, n_iter=1))