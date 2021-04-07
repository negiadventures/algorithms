# bfs to find distance from nodes

def bfs(nodes, edges):
    dist = dict()
    for n in nodes:
        dist[n] = {'dist': -1}
    q = ['S']
    dist['S']['dist'] = 0
    while len(q) != 0:
        u = q.pop()
        for e in edges:
            if u == e[0]:
                v = e[1]
            elif u == e[1]:
                v = e[0]
            else:
                continue
            if dist[v]['dist'] == -1:
                q.append(v)
                dist[v]['dist'] = dist[u]['dist'] + 1
    print(dist)


if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'S']
    edges = [('E', 'D'), ('E', 'S'), ('D', 'S'), ('S', 'A'), ('S', 'C'), ('A', 'B'), ('C', 'B')]
    bfs(nodes, edges)
