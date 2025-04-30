import heapq

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    return [heapq.heappop(h) for _ in range(len(h))]

def min_cost(cables):
    if not cables:
        return 0
    
    elif len(cables) == 1:
        return 0
    
    else:
        cabl_sorted = heap_sort(cables)
        print(cabl_sorted)
        cost = cabl_sorted[0] + cabl_sorted[1]
        new_cables = cabl_sorted[2:]
        new_cables.append(cost)
        return cost + min_cost(new_cables)
    

if __name__ == "__main__":
    cables = [15,3,4,10,12,8]
   

    print(min_cost(cables))

