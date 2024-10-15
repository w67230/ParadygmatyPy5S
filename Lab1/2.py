from collections import deque

def bfsSciezka(graph, start, end):
    queue = deque([[start]]);
    visited = set();

    while queue:
        path = queue.popleft();
        node = path[-1]; # ostatni wierzcholek w sciezce
        if node == end:
            return path;

        if node not in visited:
            for nei in graph.get(node, []):
                newPath = list(path);
                newPath.append(nei);
                queue.append(newPath);
            visited.add(node);

    return None;