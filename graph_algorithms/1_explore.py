# Explore and mark nodes in a graph

def explore(u):
    marked.append(u)
    for e in edges:
        if e[0] == u:
            v = e[1]
            if v not in marked:
                explore(v)


if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('G', 'A'), ('B', 'D'), ('C', 'E'), ('E', 'G'), ('H', 'I')]
    marked = []
    explore('A')
    print(marked)
