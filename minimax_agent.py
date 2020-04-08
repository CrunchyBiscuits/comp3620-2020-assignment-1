# minimax_agent.py
# --------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

"""
    Enter your details below:

    Name: Zheyuan Zhang
    Student ID:u6870923
    Email:zheyuan.zhang@anu.edu.au
"""

from typing import Tuple

from agents import Agent
from game_engine.actions import Directions
from search_problems import AdversarialSearchProblem

Position = Tuple[int, int]
Positions = Tuple[Position]
State = Tuple[int, Position, Position, Positions, float, float]


class MinimaxAgent(Agent):
    """ The agent you will implement to compete with the black bird to try and
        save as many yellow birds as possible. """

    def __init__(self, max_player, depth="2"):
        """ Make a new Adversarial agent with the optional depth argument.
        """
        self.max_player = max_player
        self.depth = int(depth)

    def evaluation(self, problem: AdversarialSearchProblem, state: State) -> float:
        """
            (MinimaxAgent, AdversarialSearchProblem,
                (int, (int, int), (int, int), ((int, int)), number, number))
                    -> number
        """
        player, red_pos, black_pos, yellow_birds, score, yb_score = state

        # *** YOUR CODE GOES HERE ***
        # calculate the maze distance of red_pos and black_pos
        red_black_distance = problem.maze_distance(red_pos, black_pos)
        if red_black_distance == 0:
            score -= yb_score

        # Give weight to each maze distance of red and black position
        # The reason why give 0.5 to black_pos is for reducing the punishment for the same yellow bird
        # I wish the red bird become more positive to struggle for the same yellow bird
        for yellow_bird in yellow_birds:
            # reward
            score += yb_score * (1 / problem.maze_distance(red_pos, yellow_bird))
            # punishment
            score -= yb_score * (0.5 / problem.maze_distance(black_pos, yellow_bird))

            # red_distance = problem.maze_distance(red_pos, yellow_bird)
            # black_distance = problem.maze_distance(black_pos, yellow_bird)
            # # reward
            # score += yb_score * (0.5 * self.depth / red_distance / red_distance)
            # # punishment
            # score -= yb_score * (0.5 * self.depth / black_distance / black_distance)

        return score

    def maximize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> Tuple[float, str]:
        """ This method should return a pair (max_utility, max_action).
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """

        # *** YOUR CODE GOES HERE ***
        if problem.terminal_test(state) or current_depth == self.depth:
            return self.evaluation(problem, state), Directions.STOP
        max_utility = float('-inf')
        max_action = None
        for next_state, action, _ in problem.get_successors(state):
            temp_utility = self.minimize(problem, next_state, current_depth+1, alpha, beta)
            if max_utility < temp_utility:
                max_utility = temp_utility
                max_action = action
                alpha = max_utility

            if beta <= alpha:
                break
        return max_utility, max_action

    def minimize(self, problem: AdversarialSearchProblem, state: State,
                 current_depth: int, alpha=float('-inf'), beta=float('inf')) -> float:
        """ This function should just return the minimum utility.
            The alpha and beta parameters can be ignored if you are
            implementing minimax without alpha-beta pruning.
        """

        # *** YOUR CODE GOES HERE ***
        if problem.terminal_test(state) or current_depth == self.depth:
            return self.evaluation(problem, state)
        min_utility = float('inf')
        for next_state, action, _ in problem.get_successors(state):
            min_utility = min(min_utility, self.maximize(problem, next_state, current_depth+1, alpha, beta)[0])
            beta = min_utility

            if beta <= alpha:
                break
        return min_utility

    def get_action(self, game_state):
        """ This method is called by the system to solicit an action from
            MinimaxAgent. It is passed in a State object.

            Like with all of the other search problems, we have abstracted
            away the details of the game state by producing a SearchProblem.
            You will use the states of this AdversarialSearchProblem to
            implement your minimax procedure. The details you need to know
            are explained at the top of this file.
        """
        # We tell the search problem what the current state is and which player
        # is the maximizing player (i.e. who's turn it is now).
        problem = AdversarialSearchProblem(game_state, self.max_player)
        state = problem.get_initial_state()
        utility, max_action = self.maximize(problem, state, 0)
        print("At Root: Utility:", utility, "Action:",
              max_action, "Expanded:", problem._expanded)
        return max_action
