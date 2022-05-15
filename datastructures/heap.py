from heapq import heapify, heappop, heappush

class MinHeap():
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int((i-1)/2)

    def insert_key(self, k):
        heappush(self.heap, k)

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decrease_key(self, i, new_val):
        self.heap[i]  = new_val
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # if parent value is more than new value, swap
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.pop()

    def pop(self):
        return heappop(self.heap)

    def get_min(self):
        return self.heap[0]

def main():
    input_str = input("array to heapify: ")
    input_arr = input_str.split(",")
    heapify(input_arr)
    print(input_arr[0])

    min_heap = MinHeap()
    min_heap.insert_key(7)
    min_heap.insert_key(2)
    min_heap.insert_key(-9)
    min_heap.insert_key(100)
    min_heap.insert_key(5)
    print(min_heap.pop())
    print(min_heap.get_min())
    print(min_heap.get_min())
    print(min_heap.heap)
    min_heap.decrease_key(3, 0)
    print(min_heap.heap)
    min_heap.delete_key(2)
    print(min_heap.heap)

if __name__ == "__main__":
    main()
