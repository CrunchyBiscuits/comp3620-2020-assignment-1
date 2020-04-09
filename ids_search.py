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
    s0 = problem.get_initial_state()
    answer = {s0: ""}
    visited = {s0: 0}

    while True:
        result = recursive_dls(s0, problem, visited, bound, answer, 0)
        bound += 1
        if result != "fail" and result != "cutoff":
            return result


def recursive_dls(state, problem: SearchProblem, visited, bound, answer, depth):
    cutoff_occurred = False
    visited[state] = depth
    if problem.goal_test(state):
        return answer[state].split()
    elif depth == bound:
        return "cutoff"
    else:
        for successor, action, cost in problem.get_successors(state):
            if successor not in visited.keys() or visited[successor] > depth:
                answer[successor] = answer[state] + " " + str(action)
                visited[successor] = depth + 1
                result = recursive_dls(successor, problem, visited, bound, answer, depth+1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != "fail":
                    return result
    if cutoff_occurred:
        return "cutoff"
    else:
        return "fail"
