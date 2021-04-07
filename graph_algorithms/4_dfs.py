# dfs, topological sort, component

def previsit(v):
    global count
    count += 1
    visit_nums[v]['pre'] = count


def postvisit(v):
    global count
    count += 1
    visit_nums[v]['post'] = count


def explore(u):
    marked.append(u)
    visit_nums[u] = dict()
    visit_nums[u]['comp'] = comp
    previsit(u)
    for e in edges:
        if e[0] == u:
            v = e[1]
            if v not in marked:
                explore(v)
    postvisit(u)


def dfs(nodes):
    global count, comp
    for n in nodes:
        if n not in marked:
            comp += 1
            explore(n)


if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('G', 'A'), ('B', 'D'), ('C', 'E'), ('E', 'G'), ('H', 'I')]
    marked = []
    comp = 0
    count = 0
    visit_nums = dict()
    dfs(nodes)
    print(visit_nums)
    topological_order = sorted(visit_nums, key=lambda x: (visit_nums[x]['post']), reverse=True)
    print('Topologically Sorted nodes:', topological_order)
