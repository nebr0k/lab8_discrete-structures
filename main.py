def dfs(graph, start):
    visited = set()
    stack = [start]
    dfs_number = {start: 0}
    dfs_counter = 1
    print("vertex\tDFS \tStack")
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            dfs_number[vertex] = dfs_counter
            dfs_counter += 1
            stack.extend(graph[vertex] - visited)
        print(f"{vertex}\t\t{dfs_number[vertex]}\t\t{stack}")

if __name__ == '__main__':
    graph = {}
    filename = input("Enter graph file name: ")
    with open(filename) as f:
        for line in f:
            v1, v2 = map(int, line.split())
            if v1 not in graph:
                graph[v1] = set()
            if v2 not in graph:
                graph[v2] = set()
            graph[v1].add(v2)
            graph[v2].add(v1)


    start_vertex = int(input("Enter start vertex: "))


    dfs(graph, start_vertex)




