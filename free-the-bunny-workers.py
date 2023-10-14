from itertools import combinations

def solution(num_buns, num_required):
    if num_required == 1: #base case for num_required==1
        return [[0] for x in range(num_buns)]
    if num_required == num_buns: #base case for num_required==num_buns
        return [[x] for x in range(num_buns)]
    ans=[[] for i in range(num_buns)]
    # number of keys needed, so that no matter which bunnies we choose, it will be at least one distinct key
    lengt=num_buns-num_required+1
    # the total number of keys will be combination from num_buns by num_required-1
    # beacause exactly num_required-1 bunnies will have unique keys, but still will not be able to open the door
    for x, y in enumerate(combinations(range(num_buns), lengt)):
        # y is bunnies that will have key x
        for buns in y:
            ans[buns].append(x)
    return ans




