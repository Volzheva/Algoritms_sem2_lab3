import tracemalloc
import time

t_start = time.perf_counter()
tracemalloc.start()

f = open('input.txt')
num_villages = int(f.readline())
buses = [[] for _ in range(num_villages+1)]
start_village, end_village = map(int, f.readline().split())
num_routes = int(f.readline())
for i in range(num_routes):
    source_village, departure_time, dest_village, arrival_time = map(int, f.readline().split())
    buses[source_village].append((departure_time, dest_village, arrival_time))

INF = float('inf')
arrival_times = [INF] * (num_villages+1)
arrival_times[start_village] = 0
visited = [False] * (num_villages+1)

while True:
    min_time = INF
    for i in range(1, num_villages+1):
        if not visited[i] and arrival_times[i] < min_time:
            min_time = arrival_times[i]
            min_village = i
    if min_time == INF:
        break
    current_village = min_village
    visited[current_village] = True
    for departure_time, next_village, arrival_time in buses[current_village]:
        if arrival_times[current_village] <= departure_time and arrival_time <= arrival_times[next_village]:
            arrival_times[next_village] = arrival_time

t = open('output.txt', 'w')
if arrival_times[end_village] == INF:
    t.write('-1')
else:
    t.write(str((arrival_times[end_village])))
print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())
