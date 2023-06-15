f = open('input.txt')
t = open('output.txt', 'w')
n = int(f.readline())
sides = {}
for i in range(n):
    v1 = f.readline()
    sides[v1] = []
    k = int(f.readline())
    for j in range(k):
        v2 = f.readline()
        sides[v1].append(v2)
    edge = f.readline()
for u in sides:
    visited = []
    parent = {}
    cur_node = u
    node_found = 1
    node_completed = 0
    while True:
        visited.append(cur_node)
        flag = False
        found = False
        for i in sides[cur_node]:
            if i == u:
                t.write('YES\n')
                found = True
                break
            if i not in visited:
                parent[i] = cur_node
                cur_node = i
                node_found += 1
                flag = True
                break
        if found:
            break
        if not flag:
            node_completed += 1
            if node_found == node_completed:
                break
            cur_node = parent[cur_node]
    if not found:
        t.write('NO\n')