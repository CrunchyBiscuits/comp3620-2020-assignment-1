"""
    Enter your details below:

    Name: Zheyuan Zhang
    Student ID: u6870923
    Email: zheyuan.zhang@anu.edu.au
"""

from typing import List

from search_problems import SearchProblem
from frontiers import Queue


def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """

    # *** YOUR CODE HERE ***
    s0 = problem.get_initial_state()
    q = Queue()
    q.push(s0)
    visited = [s0]
    answer = {s0: ""}
    # add a flag here to optimize the expand if we reach the goal, then do not need to expand anymore.
    flag = True
    # bfs search, use visited list to store the place we travel
    while flag:
        travel = q.pop()
        for successor, action, cost in problem.get_successors(travel):
            if problem.goal_test(successor):
                visited.append(successor)
                flag = False
                break
            if successor not in visited:
                visited.append(successor)
                q.push(successor)


    return answer
