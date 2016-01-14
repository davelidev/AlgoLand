# http://www.careercup.com/question?id=15422849

def _solution(lst, start, end):
    if start < end - 2:
        skip_edges = _solution(lst, start + 1, end - 1)
        left = lst[start] + min([_solution(lst, start + 2, end), skip_edges])
        right = lst[end - 1] + min([skip_edges, _solution(lst, start, end - 2)])
        return lst[start] if left == max(left, right) else lst[end - 1]
    elif start == end - 1:
        return lst[start]
    elif start == end - 2:
        return max(lst[start], lst[end - 1])


def solution(lst):
    return _solution(lst, 0, len(lst))