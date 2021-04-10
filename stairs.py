import sys

def stairsTD(weights):
    d = [float('inf')] * (len(weights) + 1)
    def D(i):
        if d[i] == float('inf'):
            if i <= 0: d[i] = 0
            else:
                one = D(i - 1) + weights[i - 1]
                second = D(i - 2) + weights[i - 1]
                d[i] = max(one, second)
        return d[i]
    return D(len(weights))
    
def stairsBU(weights):
    n = len(weights)
    d = [0,0]
    for i in range(2,n+2):
        d.append(max(d[i - 1], d[i - 2]) + weights[i - 2])
    return d[-1]

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    next(reader)
    weights = read_arr(next(reader))
    result = stairsBU(weights)
    print(result)

def test():
    from utils import are_equal
    method = stairsBU
    are_equal(method([1]), 1)
    are_equal(method([-1]), -1)
    are_equal(method([-2, -1]), -1)
    are_equal(method([1, 2]), 3)
    are_equal(method([2, -1]), 1)
    are_equal(method([-1, 2, 1]), 3)
    are_equal(method([-1, 2, -1, 2, -100]), -96)
    print('all tests succeeded')

def performance():
    from utils import timed_min
    data = generate_test_data()
    generate_test_file(data)
    print(timed_min(stairsBU, data, n_iter=2))
    
def generate_test_data():
    import random
    n = 10**2
    return [random.randint(-10**4, 10**4) for _ in range(n)]

def generate_test_file(data):
    from utils import generate_test_file as generate
    generate('stairs_test.txt', [f'{len(data)}\n'] + [' '.join(map(str, data))])

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    else: 
        from utils import timed_min
        print(timed_min(main, n_iter=1))