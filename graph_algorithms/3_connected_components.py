# Find connected components in undirected graph

def explore(u):
    marked.append(u)
    components[u] = comp
    for e in edges:
        if e[0] == u:
            v = e[1]
            if v not in marked:
                explore(v)


def connected_components(nodes):
    global comp
    for n in nodes:
        if n not in marked:
            comp += 1
            explore(n)


if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('G', 'A'), ('B', 'D'), ('C', 'E'), ('E', 'G'), ('H', 'I')]
    marked = []
    comp = 0
    components = dict()
    connected_components(nodes)
    print(components)
