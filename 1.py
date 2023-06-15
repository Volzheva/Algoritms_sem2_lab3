import time
import os, psutil


def existPath(count_edges, count_peaks, edges, u, v):
    mat = [[False for i in range(count_peaks)]
           for j in range(count_peaks)]

    for i in range(count_edges):
        mat[edges[i][0]][edges[i][1]] = True

    for k in range(count_peaks):
        for i in range(count_peaks):
            for j in range(count_peaks):
                mat[i][j] = (mat[i][j] or mat[i][k] and mat[k][j])

    if (u >= count_peaks or v >= count_peaks):
        return False

    if (mat[u][v]):
        return True

    return False


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
count_peaks, count_edges = f.readline().split()
edges = []
for each in range(int(count_edges)):
    edg1, edg2 = f.readline().split()
    edges.append([int(edg1) - 1, int(edg2) - 1])
    edges.append([int(edg2) - 1, int(edg1) - 1])
u, v = f.readline().split()
u, v = int(u) - 1, int(v) - 1


if existPath(int(count_edges) * 2, int(count_peaks), edges, u, v) or existPath(int(count_edges) * 2, int(count_peaks), edges, v, u):
    m.write("1")
else:
    m.write("0")

f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
