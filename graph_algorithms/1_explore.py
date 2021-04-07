# Explore and mark nodes in a graph

def explore(u):
    marked.append(u)
    for e in edges:
        v = 0
        if e[0] == u:
            v = e[1]
        elif e[1] == u:
            v = e[0]
        if v in nodes and v not in marked:
            explore(v)


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 8, 9]
    edges = [(1, 2), (2, 3), (3, 4), (7, 1), (2, 4), (3, 5), (5, 7), (8, 9)]
    marked = []
    explore(1)
    print(marked)
