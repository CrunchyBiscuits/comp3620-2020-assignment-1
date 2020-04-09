# heuristics.py
# ----------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

""" This class contains heuristics which are used for the search procedures that
    you write in search_strategies.py.

    The first part of the file contains heuristics to be used with the algorithms
    that you will write in search_strategies.py.

    In the second part you will write a heuristic for Q4 to be used with a
    MultiplePositionSearchProblem.
"""

from typing import Tuple

from search_problems import (MultiplePositionSearchProblem,
                             PositionSearchProblem)

Position = Tuple[int, int]
YellowBirds = Tuple[Position]
State = Tuple[Position, YellowBirds]


# -------------------------------------------------------------------------------
# A set of heuristics which are used with a PositionSearchProblem
# You do not need to modify any of these.
# -------------------------------------------------------------------------------


def null_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The null heuristic. It is fast but uninformative. It always returns 0"""

    return 0


def manhattan_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The Manhattan distance heuristic for a PositionSearchProblem."""

    return abs(pos[0] - problem.goal_pos[0]) + abs(pos[1] - problem.goal_pos[1])


def euclidean_heuristic(pos: Position, problem: PositionSearchProblem) -> float:
    """The Euclidean distance heuristic for a PositionSearchProblem"""

    return ((pos[0] - problem.goal_pos[0]) ** 2 + (pos[1] - problem.goal_pos[1]) ** 2) ** 0.5


# Abbreviations
null = null_heuristic
manhattan = manhattan_heuristic
euclidean = euclidean_heuristic


# -------------------------------------------------------------------------------
# You have to implement the following heuristics for Q4 of the assignment.
# It is used with a MultiplePositionSearchProblem
# -------------------------------------------------------------------------------

# You can make helper functions here, if you need them


def bird_counting_heuristic(state: State,
                            problem: MultiplePositionSearchProblem) -> float:
    position, yellow_birds = state
    heuristic_value = 0

    """ *** YOUR CODE HERE *** """
    heuristic_value = len(yellow_birds)
    return heuristic_value


bch = bird_counting_heuristic


def every_bird_heuristic(state: State,
                         problem: MultiplePositionSearchProblem) -> float:
    position, yellow_birds = state
    heuristic_value = 0

    """ *** YOUR CODE HERE *** """
    # # MST
    # node_count = len(yellow_birds) + 1
    #
    # # set the nodes in MST
    # u_ds = [position]
    # for yellow_bird in yellow_birds:
    #     u_ds.append(yellow_bird)
    # v_ds = u_ds
    #
    # # create adjacency matrix
    # edges = {}
    # for u in u_ds:
    #     for v in v_ds:
    #         if u == v:
    #             continue
    #         else:
    #             edges[(u, v)] = problem.maze_distance(u, v)
    #
    # # create mst
    # current_node = u_ds[0]
    # visited = [current_node]
    # min_distance = 1000
    # for _ in range(node_count - 1):
    #     temp_node = None
    #     for a, b in edges.keys():
    #         if a == current_node and b not in visited:
    #             if edges[(a, b)] < min_distance:
    #                 min_distance = edges[(a, b)]
    #                 temp_node = b
    #     current_node = temp_node
    #     visited.append(current_node)
    #     heuristic_value += min_distance
    #
    # return heuristic_value

    if yellow_birds:
        heuristic_value += problem.maze_distance(position, yellow_birds[0])
        for i in range(len(yellow_birds) - 1):
            heuristic_value += problem.maze_distance(yellow_birds[i], yellow_birds[i+1])

    return heuristic_value

every_bird = every_bird_heuristic
