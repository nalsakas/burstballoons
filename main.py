def burstballoons(a:list[int]):

    # determine all possible sequnces and corresponding values.
    def dfs(items:list[int], total_sum, processed):
        if not items:
            return [[total_sum, processed]]
        
        collect = []
        for i in range(len(items)):
            item_current = items[i]
            item_prev = 1 if i < 1 else items[i - 1]
            item_next = 1 if i > len(items) - 2 else items[i + 1]
            item_sum = item_prev * item_current * item_next
            
            items_filtered = list(filter(lambda x: x != item_current, items))
            res = dfs(items_filtered, total_sum + item_sum, [*processed, item_current])
            collect = [*res, *collect]
        return collect
    
    # Determine max value and max sequence
    max_val = 0
    max_sequence = None
    for k in dfs(a, 0, []):
        #print(k)
        if k[0] > max_val:
            max_val = k[0]
            max_sequence = k[1]

    return max_val, max_sequence

a = [1, 2, 3, 4]
b = [4, 1, 3, 2]
print(burstballoons(a))
print(burstballoons(b))