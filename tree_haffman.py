class PriorityQueue():
    def __init__(self, comparisonFunc, arr = []):
        self.arr = arr
        self.comparisonFunc = comparisonFunc

    def insert(self, value):
        self.arr.append(value)

    def extract_min(self):
        value = min(self.arr, key=self.comparisonFunc)
        index = self.arr.index(value)
        del self.arr[index]
        return value

    def __len__(self):
        return len(self.arr)

class Node():
    def __init__(self, value, children):
        self.children = children
        self.value = value
    
    def add(self, node):
        self.children.append(node)
        
def get_haffman_codes(s):
    freq = {}
    for ch in s: freq[ch] = freq.setdefault(ch, 0) + 1
    
    nodes = [Node(x, []) for x in freq.items()]
    queue = PriorityQueue(comparisonFunc=lambda x: x.value[1], arr=nodes)
    n = len(nodes)
    for _ in range(0, n - 1):
        node1 = queue.extract_min()
        node2 = queue.extract_min()
        newnode = Node((None, node1.value[1] + node2.value[1]), [node1, node2])
        queue.insert(newnode)
    
    def process_node(node, prev_value):
        if(len(node.children) == 0): return [(node.value[0], prev_value)]
        result = []
        for i in range(0, len(node.children)):
            result = result + process_node(node.children[i], prev_value + str(i))
        return result
    
    root = queue.extract_min()
    leafs = process_node(root, "" if len(root.children) > 0 else "0")
    return dict(leafs)

def encode_string(s, codes):
    return ''.join([codes[ch] for ch in s])

def main():
    s = input()
    codes = get_haffman_codes(s)
    encoded_string = encode_string(s, codes)
    
    print(len(codes), len(encoded_string))
    for key, code in codes.items(): print(f'{key}: {code}')
    print(encoded_string)

if __name__ == "__main__":
    f = open('tree_haffman_test.txt', 'r')
    input = f.readline
    main()
    f.close()
