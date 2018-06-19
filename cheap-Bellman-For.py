def BellmanFord(l, E, V, s):
    dist = [99999]*V
    dist[0] = 0
    
    for x in range(V-1):
        for (source, destination, distance) in l:#reducing an edge V-1 times
            if dist[source]+distance<dist[destination]:
                dist[destination] = dist[source]+distance
    return dist


l = []

V, E = 4,4
print("Enter the edges, source, destination and length of the edge")
for x in range(E):
    s, d, dist = [int(x) for x in input().split(" ")]
    l.append((s,d,dist))
    
result = BellmanFord(l, E, V, 0)
print(result)
