import sys

def knapsackBU(max_weight, weights):
    weights_len, max_weights_len = len(weights) + 1, max_weight + 1
    d = [[float('inf')] * max_weights_len for _ in range(weights_len)]
    for i in range(weights_len): d[i][0] = 0
    for i in range(max_weights_len): d[0][i] = 0
    for i in range(1, weights_len):
        for j in range (1, max_weights_len):
            weight = weights[i-1]
            d[i][j] = max(d[i-1][j], d[i-1][j-weight] + weight if j >= weight else 0)
    return d[weights_len-1][max_weights_len-1]

def knapsackTD(max_weight, weights):
    weights_len, max_weights_len = len(weights) + 1, max_weight + 1
    d = [[float('inf')] * max_weights_len for _ in range(weights_len)]
    for i in range(weights_len): d[i][0] = 0
    for i in range(max_weights_len): d[0][i] = 0
    def D(i,j):
        if d[i][j] == float('inf'):
            weight = weights[i-1]
            rest_weight = j - weight
            results = [D(i-1,j)]
            if rest_weight >= 0:
                results.append(D(i-1, rest_weight) + weight)
            d[i][j] = max(results)
        return d[i][j]
    return D(weights_len - 1, max_weights_len-1)

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    w, _ = read_arr(next(reader))
    weights = read_arr(next(reader))
    result = knapsackBU(w, weights)
    print(result)

def test():
    from utils import are_equal
    method = knapsackBU
    are_equal(method(5,[1,2,3]), 5)
    are_equal(method(1,[0]), 0)
    are_equal(method(1,[0,1]), 1)
    are_equal(method(1,[1]), 1)
    are_equal(method(2,[1,1]), 2)
    are_equal(method(3,[1,2,1]), 3)
    are_equal(method(4,[1,2,1]), 4)
    are_equal(method(1,[2]), 0)
    are_equal(method(2,[3,4]), 0)
    are_equal(method(1,[1,2,3]), 1)
    are_equal(method(2,[1,2,3]), 2)
    are_equal(method(3,[1,2,3]), 3)
    are_equal(method(4,[1,2,3]), 4)
    are_equal(method(6,[1,2,3]), 6)
    are_equal(method(7,[1,2,3,100]), 6)
    are_equal(method(4,[1,2,4]), 4)
    are_equal(method(4,[1,2,5]), 3)
    are_equal(method(10,[1,8,4]), 9)
    print('all tests succeeded')

def performance():
    from utils import timed_min
    data = generate_test_data()
    generate_test_file(data)
    print(timed_min(knapsackBU, data[0], data[2], n_iter=2))
    
def generate_test_data():
    import random
    w = 10**4
    n = 300
    return w, n, [random.randint(0, 10**5) for _ in range(n+1)]

def generate_test_file(data):
    from utils import generate_test_file as generate
    weights = ' '.join(map(str, data[2]))
    generate('knapsack_test.txt', [f'{data[0]} {data[1]}\n'] + [weights])

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    else: 
        from utils import timed_min
        print(timed_min(main, n_iter=1))