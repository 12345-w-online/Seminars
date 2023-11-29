def ordering_heap(heap:list, index:int) -> list:
    next_index_left = index * 2 + 1
    next_index_right = index * 2 + 2
    while ((next_index_left <= len(heap) - 1) and heap[index] < heap[next_index_left]) or\
          ((next_index_right <= len(heap) - 1) and heap[index] < heap[next_index_right]):
        if (len(heap) -  1 < next_index_right) or heap[next_index_left] >= heap[next_index_right]:
            heap[index], heap[next_index_left] = heap[next_index_left], heap[index]
            index = next_index_left
        else:
            heap[index], heap[next_index_right] = heap[next_index_right], heap[index]
            index = next_index_right
        next_index_left = index * 2 + 1
        next_index_right = index * 2 + 2
    return heap


my_heap = list(map(int, input().split()))
for index in range(int(len(my_heap) / 2) + 1, -1, -1):
    my_heap = ordering_heap(my_heap, index)

print(*my_heap)