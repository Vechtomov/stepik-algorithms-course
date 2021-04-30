import sys, queue

def task(size, packets):
    n = len(packets)
    if n == 0: 
        return []
    packets = [(p[0], p[1], i) for i, p in enumerate(packets)]
    # print(packets)
    buffer = queue.Queue(size)
    next_packet_ind = 1
    result = [-1] * n
    current_packet = packets[0]
    buffer.put(current_packet)
    current_time = current_packet[0]
    # сначала считываем все одновременные пакеты, отбрасываем те, что не влезли в буфер
    # обрабатываем 1 пакет в буфере, увеличиваем текущее время, записываем в результат
    # считываем новый пакет; если его время меньше текущего, отбрасываем его, иначе добавляем в конец буфера
    while next_packet_ind < n or not buffer.empty():
        if next_packet_ind < n:
            new_packet = packets[next_packet_ind]
            if new_packet[0] <= current_time:
                if new_packet[0] == current_time and not buffer.full():
                    buffer.put_nowait(new_packet)
                next_packet_ind += 1
                continue
            elif buffer.empty():
                buffer.put_nowait(new_packet)
                current_time = new_packet[0]
                next_packet_ind += 1
                continue
        if not buffer.empty():
            current_packet = buffer.get_nowait()
            result[current_packet[2]] = current_time
            current_time += current_packet[1]
    return result

def main():
    def read_arr(s):
        return list(map(int, (s.split())))
    reader = (s for s in sys.stdin)
    size, n = read_arr(next(reader))
    packets = []
    for _ in range(n):
        arr, dur = read_arr(next(reader))
        packets.append((arr, dur))
    result = task(size, packets)
    print(len(result))
    # print(*result)

def test():
    from utils import are_equal
    method = task

    def simple_tests():
        are_equal(method(1, []), [])
        are_equal(method(1, [(0, 0)]), [0])
        are_equal(method(1, [(1, 0)]), [1])
        are_equal(method(1, [(1, 1)]), [1])
        are_equal(method(2, [(0, 1),(0, 1)]), [0, 1])
        are_equal(method(1, [(0, 1),(0, 1)]), [0, -1])
        are_equal(method(2, [(0, 0),(0, 1)]), [0, 0])
        are_equal(method(2, [(0, 1),(2, 1)]), [0, 2])
        are_equal(method(2, [(0, 1),(1, 1)]), [0, 1])
        are_equal(method(2, [(0, 2),(1, 1)]), [0, -1])
        are_equal(method(2, [(0, 2),(4, 1),(4, 1)]), [0, 4, 5])
        are_equal(method(1, [(0, 2),(4, 2),(5, 1)]), [0, 4, -1])
        are_equal(method(1, [(0, 2),(4, 2),(6, 1)]), [0, 4, 6])
        
    simple_tests()

    print('all tests succeeded')

def performance():
    from utils import timed_min
    data = generate_test_data()
    generate_test_file(data)
    print(timed_min(task, *data, n_iter=2))
    
def generate_test_data():
    size = 10**2
    n = 10**5
    return size, [(i, 2) for i in range(0, n)]

def generate_test_file(data):
    from utils import generate_test_file as generate
    packets = [f'{p[0]} {p[1]}\n' for p in data[1]]
    generate('packet_handler_test.txt', [f'{data[0]} {len(packets)}\n'] + packets)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if(mode == 'performance'): performance()
    elif(mode == 'test'): test()
    else: 
        from utils import timed_min
        print(timed_min(main, n_iter=1))