from collections import deque
import time
import tracemalloc

t = time.process_time()
tracemalloc.start()


def half_graph(u):
    global sides, total_colors
    search_queue = deque()
    search_queue.append((u, 0))
    print(search_queue)
    visited = []
    while search_queue:
        cur_node, color = search_queue.popleft()
        if cur_node not in visited:
            total_colors[cur_node] = color
            visited.append(cur_node)
            for node in sides[cur_node]:
                if color == 0:
                    search_queue.append((node, 1))
                else:
                    search_queue.append((node, 0))
        elif total_colors[cur_node] != color:
            return 0
    return 1


f = open('input.txt')
n, m = map(int, f.readline().split())
sides = {}
for i in range(n + 1):
    sides[i] = []
for i in range(m):
    v1, v2 = map(int, f.readline().split())
    sides[v1].append(v2)
    sides[v2].append(v1)

total_colors = [None] * (n + 1)
d = open('output.txt', 'w')
d.write(str(half_graph(1)))

print('Время работы: %s секунд' % (time.process_time() - t))
print('Затраты памяти:', float(tracemalloc.get_tracemalloc_memory()) / (2** 20), 'мб')