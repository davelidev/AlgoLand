def _solution(graph, x, y, max_x, max_y):
    if x < max_x - 1 and y < max_y - 1:
        right = _solution(graph, x + 1, y, max_x, max_y)
        down = _solution(graph, x, y + 1, max_x, max_y)
        if right[0] > down[0]:
            return [right[0] + graph[x][y], min(right[1], graph[x][y])]
        else:
            return [down[0] + graph[x][y], min(down[1], graph[x][y])]
    elif x < max_x - 1:
        pre_path = _solution(graph, x + 1, y, max_x, max_y)
        return [pre_path[0] + graph[x][y], min(pre_path[0], graph[x][y])]
    elif y < max_y - 1:
        pre_path = _solution(graph, x, y + 1, max_x, max_y)
        return [pre_path[0] + graph[x][y], min(pre_path[0], graph[x][y])]
    else:
        # x, y is equivalent to the right down element.
        return [graph[x][y], graph[x][y]]


def solution(graph):
    assert len(graph) != 0 and len(graph[0]) != 0
    return _solution(graph, 0, 0, len(graph), len(graph[0]))[1]


graph = [
    [3, 2],
    [1, 4]
]
# print solution(graph)
# prints 2
