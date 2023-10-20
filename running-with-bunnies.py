def solution(times, times_limit):
    count = len(times)
    buns = count - 2  # number of bunnies
    if buns == 0:
        return []

    # use Floyd Warshall Algorithm to find the shortest path from one node to every other
    for u in range(count):
        for i in range(count):
            for j in range(count):
                times[i][j] = min(times[i][u] + times[u][j], times[i][j])

    # check graph for a negative cycle
    # if such, then we can grind time and get every bunny
    for q in range(count):
        if times[q][q] < 0:
            return [q for q in range(buns)]

    # if no negative cycle found, then just simply bfs through every possible path
    # this approach will work, because max number of bunnies is equal to 5
    def bfs(curr=times_limit, took=list(), index=0, vis=[True] + [False] * (count - 1), ans=[]):
        # break if current timer is under thw lower bound, or we have reached the end with negative timer
        if curr <= -999 or (index + 1 == count and curr < 0):
            return ans
        # update the answer if we reached the end with positive timer and more bunnies then before
        if curr >= 0 and index + 1 == count and took and len(ans) < len(took):
            return sorted(list(took[:]))
        # brute-force to every bunny
        for i, v in enumerate(times[index]):
            # skip start position and current index
            if i == 0 or i == index:
                continue
            # move to next unvisited node
            if not vis[i]:
                vis[i] = True
                ans = bfs(curr - v, took + [i - 1], i, vis, ans)
                vis[i] = False
        return ans
    # return answer excluding the last exit index
    return bfs()[:-1]

