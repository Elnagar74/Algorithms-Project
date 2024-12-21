def heapify(heap, n, i):
   mx, l, r = i, (2 * i) + 1, (2 * i) + 2

   if l < n and heap[i] < heap[l]:
      mx = l

   if r < n and heap[mx] < heap[r]:
      mx = r

   if mx != i:
      heap[i],heap[mx] = heap[mx],heap[i]
      heapify(heap, n, mx)

def heapSort(heap):
   n = len(heap)

   for i in range(n, -1, -1): #Build Max Heap
      heapify(heap, n, i)

   for i in range(n-1, 0, -1):
      heap[i], heap[0] = heap[0], heap[i]
      heapify(heap, i, 0)


arr = list(map(int, input("Hello, Enter The Array: ").split()))
print('-----------------------------------------------')
print(f"The Array Before Applying Heap Sort: {arr}")
print('-----------------------------------------------')
heapSort(arr)
print(f"The Array After Applying Heap Sort: {arr}")
