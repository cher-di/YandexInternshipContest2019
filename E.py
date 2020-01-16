if __name__ == '__main__':
    n, m = (int(i) for i in input().split())
    graph = dict()
    for i in range(m):
        u, v, w = (int(i) for i in input().split())
        edge = frozenset((u, v))
        w_curr = graph.get(edge, None)
        if w_curr is None:
            graph[edge] = w
        else:
            graph[edge] = min(graph[edge], w)

    team_a, team_b = set(), set()
    edges = sorted(graph.keys(), key=lambda x: graph[x])
    for edge in edges:
        u, v = edge
        if (u in team_a and v in team_a) or (u in team_b and v in team_b):
            continue

        if u in team_a:
            if v not in team_b:
                team_b.add(v)
        elif u in team_b:
            if v not in team_a:
                team_a.add(v)
        else:
            if v in team_a:
                team_b.add(u)
            elif v in team_b:
                team_a.add(u)
            else:
                team_a.add(u)
                team_b.add(v)

    edges.reverse()
    min_edge = 10 ** 5
    for edge in edges:
        u, v = edge
        if (u in team_a and v in team_a) or (u in team_b and v in team_b):
            min_edge = graph[edge]

    print(max(min_edge, ))
