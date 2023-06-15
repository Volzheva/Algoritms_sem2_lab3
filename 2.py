import time
import os, psutil


def ToDict(count_peaks, ribs):
    ribsDict = dict()
    for i in range(count_peaks):
        currRibs = []
        for j in range(len(ribs)):
            if ribs[j][0] == i + 1:
                currRibs.append(ribs[j][1])
            elif ribs[j][1] == i + 1:
                currRibs.append(ribs[j][0])
        ribsDict[i + 1] = currRibs
    return ribsDict


def DFS(start, verts):
    Visited[start] = True
    verts.append(start)
    for u in ribsDict[start]:
        if not Visited[u]:
            DFS(u, verts)
    return verts


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("input.txt")
m = open("output.txt", "w")
count_peaks, count_ribs = f.readline().split()
ribs = []
for each in range(int(count_ribs)):
    rib1, rib2 = f.readline().split()
    ribs.append([int(rib1), int(rib2)])

ribsDict = ToDict(int(count_peaks), ribs)
Visited = [False] * (int(count_peaks) + 1)
comps = list()

for i in range(1, int(count_peaks) + 1):
    if not Visited[i]:
        comps.append(DFS(i, list()))

m.write(str(len(comps)))

f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
