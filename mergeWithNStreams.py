import heapq

def mergeFromNStreams(lists):
    heap = []
    indices = [0] * len(lists)
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i))
    merged = []
    while len(heap) > 0:
        elt, i = heapq.heappop(heap)
        merged.append(elt)
        indices[i] += 1
        if indices[i] < len(lists[i]):
            heapq.heappush(heap, (lists[i][indices[i]], i))
    return merged

lists = [[1, 2, 3, 8, 40, 50],
         [0, 2, 8, 11],
         [1, 19, 21, 30]]
print mergeFromNStreams(lists)