import os, psutil
import time
import collections


def find_min_path(elements_graph, start: str, end: str):
    len_map = dict()
    queue_name = collections.deque()
    len_map[start] = 0
    queue_name.append(start)
    while len(queue_name) != 0:
        curr_v = queue_name.popleft()
        if curr_v == end:
            return len_map[curr_v]
        if curr_v in elements_graph:
            for next_elem in elements_graph[curr_v]:
                if next_elem not in len_map:
                    len_map[next_elem] = len_map[curr_v] + 1
                    queue_name.append(next_elem)
    return -1


if __name__ == '__main__':
    t_start = time.perf_counter()
    process = psutil.Process(os.getpid())
    f = open('input.txt', 'r')
    n = int(f.readline())
    elements_graph = dict()
    for i in range(n):
        inp_str = f.readline().strip().split(" -> ")
        if inp_str[0] not in elements_graph:
            elements_graph[inp_str[0]] = [inp_str[1]]
        else:
            elements_graph[inp_str[0]].append(inp_str[1])
    fr_element = f.readline().strip()
    to_elem = f.readline().strip()
    t = open('output.txt', 'w+')
    t.write(str(find_min_path(elements_graph, fr_element, to_elem)))


print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
