def explore(u, comp):
    marked.append(u)
    components[u] = comp
    for e in edges:
        v = 0
        if e[0] == u:
            v = e[1]
        elif e[1] == u:
            v = e[0]
        if v in nodes and v not in marked:
            explore(v, comp)


def connected_components(nodes):
    comp = 0
    for n in nodes:
        if n not in marked:
            comp += 1
            explore(n, comp)


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 8, 9]
    edges = [(1, 2), (2, 3), (3, 4), (7, 1), (2, 4), (3, 5), (5, 7), (8, 9)]
    marked = []
    components = dict()
    connected_components(nodes)
    print(components)
