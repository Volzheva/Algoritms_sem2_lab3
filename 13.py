


def count_connected_components(n_rows, n_cols, grid):
    visited = set()
    stack = []
    count = 0

    for i in range(n_rows * n_cols):
        if i not in visited and grid[i // n_cols][i % n_cols] == "#":
            count += 1
            stack.append(i)
            while stack:
                x = stack.pop()
                if x not in visited:
                    visited.add(x)
                    row, col = x // n_cols, x % n_cols
                    for dx, dy in ((0, 1),
                                   (0, -1),
                                   (1, 0),
                                   (-1, 0)):
                        nx, ny = row + dx, col + dy
                        if 0 <= nx < n_rows and 0 <= ny < n_cols and grid[nx][ny] == "#":
                            stack.append(nx * n_cols + ny)

    return count


def main():


    f = open("input.txt", "r")
    n_rows, n_cols = map(int, f.readline().split())
    grid = [f.readline().strip() for _ in range(n_rows)]

    count = count_connected_components(n_rows, n_cols, grid)
    t = open("output.txt", "w")
    t.write(str(count))



if __name__ == "__main__":
    main()
