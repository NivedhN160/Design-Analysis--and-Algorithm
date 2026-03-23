# Huffman Coding Tree Construction.
import heapq
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_huffman_tree(text):
    freq_map = {}
    for ch in text:
        freq_map[ch] = freq_map.get(ch, 0) + 1
    heap = []
    for ch, freq in freq_map.items():
        heapq.heappush(heap, Node(ch, freq))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]
def generate_codes(root, current_code="", codes={}):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
        return
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes
text = input("Enter text to encode: ")
root = build_huffman_tree(text)
codes = generate_codes(root)
print("Huffman Codes:")
for ch, code in codes.items():
    print(f"{ch}: {code}")