# finding strongly connected components in Directed graph

def previsit(v):
    global count
    count += 1
    visit_nums[v]['pre'] = count


def postvisit(v):
    global count
    count += 1
    visit_nums[v]['post'] = count


def explore(u, edges):
    marked.append(u)
    visit_nums[u] = dict()
    visit_nums[u]['comp'] = comp
    previsit(u)
    for e in edges:
        if e[0] == u:
            v = e[1]
            if v not in marked:
                explore(v, edges)
    postvisit(u)


def dfs(nodes, edges_reversed):
    global count
    for n in nodes:
        if n not in marked:
            explore(n, edges_reversed)


def reverse(edges):
    rev = []
    for e in edges:
        rev.append((e[1], e[0]))
    return rev


def scc(nodes, edges_original):
    global comp, visit_nums, marked, count
    comp = 0
    # reverse graph G(r)
    edges_reversed = reverse(edges_original)
    # find pre-visit and post-visit on G(r)
    dfs(nodes, edges_reversed)
    # decreasing order of post-visit on G(r)
    topological_sorted_nodes = sorted(visit_nums, key=lambda x: (visit_nums[x]['post']), reverse=True)
    marked = []
    visit_nums = dict()
    count = 0
    # for each node in topologically sorted node, explore actual graph(G) and assign components
    for n in topological_sorted_nodes:
        if n not in marked:
            comp += 1
            explore(n, edges_original)
    print(visit_nums)


if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges_original = [('C', 'D'), ('D', 'G'), ('G', 'C'), ('D', 'A'), ('A', 'B'), ('B', 'F'), ('F', 'E'), ('E', 'A')]
    marked = []
    count = 0
    visit_nums = dict()
    scc(nodes, edges_original)
