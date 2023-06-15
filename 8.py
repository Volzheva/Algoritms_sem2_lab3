from collections import deque
import time
import tracemalloc

t = time.process_time()
tracemalloc.start()


def short_path(u, v):
    global sides
    min_path = float('inf')
    search_queue = deque()
    search_queue.append((u, 0, None))
    while search_queue:
        cur_node, path, parent = search_queue.popleft()
        if cur_node == v:
            if path < min_path:
                min_path = path
        else:
            for node in sides[cur_node]:
                if node[0] != parent:
                    search_queue.append((node[0], path + node[1], cur_node))
    if min_path == float('inf'):
        return -1
    return min_path

f = open('input.txt')
n, m = map(int, f.readline().split())
sides = {}
for i in range(n+1):
    sides[i] = []
for i in range(m):
    v1, v2, l = map(int, f.readline().split())
    flag = False
    for node in sides[v1]:
        if node[0] == v2 and l < node[1]:
            node[1] = l
            flag = True
    if not flag:
        sides[v1].append([v2, l])
    for node in sides[v1]:
        if node[0] == v2 and l < node[1]:
            node[1] = lflag = False
        if flag:
            sides[v2].append([v1, l])
u, v = map(int, f.readline().split())


d = open('output.txt', 'w')
d.write(str(short_path(u, v)))


print('Время работы: %s секунд' % (time.process_time() - t))
print('Затраты памяти:', float(tracemalloc.get_tracemalloc_memory()) / (2** 20), 'мб')