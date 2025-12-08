"""
--- Part Two ---
The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?

Your puzzle answer was 3926518899.


"""

import heapq

with open("input.txt", "r") as f:
    lines = f.readlines()
    points = []
    for line in lines:
        points.append(list(map(int, line.strip().split(","))))

    N = len(points)
    heap = []

    for i in range(N):
        x1, y1, z1 = points[i]
        for j in range(i + 1, N):
            x2, y2, z2 = points[j]
            distance = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            heapq.heappush(heap, (distance, i, j))

    def ufind(x):
        if parent[x] != x:
            parent[x] = ufind(parent[x])
        return parent[x]

    def uunion(x, y):
        parentx = ufind(x)
        parenty = ufind(y)
        if parentx != parenty:
            parent[parentx] = parenty

    parent = [i for i in range(N)]
    connections_made = 0
    target_connections = N - 1

    while heap:
        distance, i, j = heapq.heappop(heap)
        if ufind(i) != ufind(j):
            uunion(i, j)
            connections_made += 1
            if connections_made == target_connections:
                x1 = points[i][0]
                x2 = points[j][0]
                result = x1 * x2
                break

    print(result)
