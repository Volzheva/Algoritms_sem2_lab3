import time
import os, psutil

t_start = time.perf_counter()
process = psutil.Process(os.getpid())

f = open('input.txt', 'r')
num_vertices, num_edges = map(int, f.readline().split())
graph = [[] for _ in range(num_vertices)]
in_degrees = [0] * num_vertices
for _ in range(num_edges):
    start, end = map(int, f.readline().split())
    graph[start - 1].append(end - 1)
    in_degrees[end - 1] += 1

no_incoming_vertices = []
for i in range(num_vertices):
    if in_degrees[i] == 0:
        no_incoming_vertices.append(i)

result = []
while no_incoming_vertices:
    vertex = no_incoming_vertices.pop()
    result.append(vertex + 1)
    for neighbor in graph[vertex]:
        in_degrees[neighbor] -= 1
        if in_degrees[neighbor] == 0:
            no_incoming_vertices.append(neighbor)

t = open('output.txt', 'w+')
for vertex in result:
    t.write(str(vertex) + ' ')


print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
