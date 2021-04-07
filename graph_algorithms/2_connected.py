# Check if a graph is connected

def explore(u):
    marked.append(u)
    for e in edges:
        if e[0] == u:
            v = e[1]
            if v not in marked:
                explore(v)


def is_connected(nodes):
    explore('A')
    for n in nodes:
        if n not in marked:
            return "Not Connected"
    return "Connected"


if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('G', 'A'), ('B', 'D'), ('C', 'E'), ('E', 'G'), ('H', 'I')]
    marked = []
    print(is_connected(nodes))
