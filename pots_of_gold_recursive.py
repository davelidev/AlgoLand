# http://www.careercup.com/question?id=15422849
# Pots of gold game: Two players A & B. There are pots of gold arranged in a line,
# each containing some gold coins (the players can see how many coins are there in each
# gold pot - perfect information). They get alternating turns in which the player can pick
# a pot from one of the ends of the line. The winner is the player which has a higher number
# of coins at the end. The objective is to "maximize" the number of coins collected by A,
# assuming B also plays optimally. A starts the game. 
# 
# The idea is to find an optimal strategy that makes A win knowing that B is playing
# optimally as well. How would you do that? 
# 
# At the end I was asked to code this strategy!

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
