import sys

def calculator(n):
    if n == 1: return [1]
    d = [0] * (n + 1)
    for i in range(2, n + 1):
        prev_nums = []
        if i % 3 == 0:
            prev_nums.append(i // 3)
        if i % 2 == 0:
            prev_nums.append(i // 2)
        prev_nums.append(i - 1)
        results = [d[num] for num in prev_nums]
        d[i] = min(results) + 1
    numbers = [n]
    for i in reversed(range(2, n)):
        prev_number = numbers[-1]
        if d[i] + 1 == d[prev_number] and prev_number in (i + 1, i * 2, i * 3):
            numbers.append(i)
    numbers.append(1)
    return list(reversed(numbers))

def main():
    reader = (s for s in sys.stdin)
    n = int(next(reader))
    result = calculator(n)
    print(len(result) - 1)
    print(*result)

def test():
    from utils import are_equal
    def method(n):
        return len(calculator(n)) - 1
    are_equal(method(1), 0)
    are_equal(method(5), 3)
    are_equal(method(96234), 14)
    print('all tests succeeded')

def performance():
    from utils import timed_min
    data = generate_test_data()
    generate_test_file(data)
    print(timed_min(calculator, data, n_iter=2))
    
def generate_test_data():
    import random
    return random.randint(1, 10**5)

def generate_test_file(data):
    from utils import generate_test_file as generate
    generate('calculator_test.txt', [f'{data}\n'])

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    else: 
        from utils import timed_min
        print(timed_min(main, n_iter=1))