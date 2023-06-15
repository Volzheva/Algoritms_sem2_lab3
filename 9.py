def create_graph(n, m, edges, directed=False):
    graph = {i + 1: [] for i in range(n)}
    for edge in edges:
        u, v = map(int, edge.split()[:2])
        if len(edge.split()) == 3:
            w = int(edge.split()[2])
            graph[u] = [*graph[u], (v, w)] if u in graph.keys() else [(v, w)]
        else:
            graph[u] = [*graph[u], v] if u in graph.keys() else [v]
            if not directed:
                graph[v] = [*graph[v], u] if v in graph.keys() else [u]
    return graph


def has_negative_cycle(graph):
    dist = {v: 0 for v in graph}
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
    for u in graph:
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                return True
    return False

def measure_memory_and_time(func):
    import time
    import psutil
    import os
    def _wrapped(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        memory = psutil.Process(os.getpid()).memory_info().rss
        print(f"Memory usage: {memory // 1024 ** 2} megabytes")
        print(f"Time usage: {end_time - start_time} seconds")
        return result
    return _wrapped

def set_stdout(file: str = "output.txt"):
    try:
        import sys
        sys.stdout = open(file, 'wt', encoding='utf-8')
    except Exception as e:
        raise IOError(e)


@measure_memory_and_time
def main():
    set_stdout()
    with open('input.txt', 'rt', encoding='utf-8') as f:
        input = f.readline
        n, m = map(int, input().split())
        graph = create_graph(n, m, [input() for _ in range(m)], directed=True)
    print(1 if has_negative_cycle(graph) else 0)

if __name__ == '__main__':
    main()