"""
    Enter your details below:

    Name: Zheyuan Zhang
    Student ID: u6870923
    Email:zheyuan.zhang@anu.edu.au
"""

from typing import Callable, List
from frontiers import PriorityQueue
from search_problems import SearchProblem


def solve(problem: SearchProblem, heuristic: Callable) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """

    # *** YOUR CODE HERE ***
    s0 = problem.get_initial_state()
    frontier = PriorityQueue()
    frontier.push(s0, 0.0)
    gn = {s0: 0.0}
    visited = []
    answer = {s0: ""}
    goal = s0
    while not frontier.is_empty():
        travel = frontier.pop()
        if problem.goal_test(travel):
            goal = travel
        for successor, action, cost in problem.get_successors(travel):
            if successor not in visited:
                visited.append(successor)
                fn = gn[travel] + heuristic(successor, problem)
                frontier.push(successor, fn)
                answer[successor] = answer[travel]+" "+str(action)
                gn[successor] = fn

    return answer[goal].split()
