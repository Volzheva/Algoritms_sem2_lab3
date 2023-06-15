import time
import tracemalloc

t = time.process_time()
tracemalloc.start()


def labirint(k, path, sides):
    room_cur = 1
    for i in range(k):
        color = path[i]
        flag = False
        for vertex, side in sides[room_cur]:
            if side == color:
                room_cur = vertex
                flag = True
                break
        if not flag:
            return 'INCORRECT'
    return str(room_cur)

f = open('input.txt')
n, m = map(int, f.readline().split())
sides = {}
for i in range(1, n+1):
    sides[i] = []
for _ in range(m):
    u, v, c = map(int, f.readline().split())
    sides[u].append([v, c])
    sides[v].append([u, c])
k = int(f.readline())
path = list(map(int, f.readline().split()))

d = open('output.txt', 'w')
d.write(labirint(k, path, sides))


print('Время работы: %s секунд' % (time.process_time() - t))
print('Затраты памяти:', float(tracemalloc.get_tracemalloc_memory()) / (2** 20), 'мб')