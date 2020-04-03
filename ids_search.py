"""
    Enter your details below:

    Name: Zheyuan Zhang
    Student ID: u6870923
    Email: zheyuan.zhang@anu.edu.au
"""

from typing import List
from frontiers import Stack
from search_problems import SearchProblem


def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """

    # *** YOUR CODE HERE ***
    bound = 0
    while True:
        result = dls(problem, bound)
        bound += 1
        if type(result) != bool:
            return result


def dls(problem: SearchProblem, bound):
    s0 = problem.get_initial_state()
    frontier = Stack()
    frontier.push((s0, 0))
    visited = [s0]
    return recursive_dls(problem, frontier, visited, bound)


def recursive_dls(problem: SearchProblem, frontier, visited, bound):
    cutoff_occurred = False
    if frontier.is_empty():
        return True
    state, depth = frontier.pop()
    if problem.goal_test(state):
        answer = []
        node = visited[-1]
        for path in reversed(visited):
            for successor, action, cost in problem.get_successors(path):
                if successor == node:
                    node = path
                    answer.append(action)
        answer.reverse()
        return answer
    elif depth == bound:
        return True
    else:
        for successor, action, cost in problem.get_successors(state):
            if successor not in visited:
                frontier.push((successor, depth+1))
                visited.append(successor)
            result = recursive_dls(problem, frontier, visited, bound)
            if result and type(result) == bool:
                cutoff_occurred = True
            else:
                return result
        if cutoff_occurred:
            return True




