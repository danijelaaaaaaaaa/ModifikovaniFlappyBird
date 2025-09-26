from board import FlappyBirdBoard
from problem_definition import FlappyBirdState, FlappyBirdAction, FlappyBirdActionsFunction, \
                       FlappyBirdResultFunction,FlappyBirdGoalTestFunction, FlappyBirdStepCostFunction
from search_algorithms.problem import Problem
from search_algorithms.bfs import BFS
from search_algorithms.ucs import UCS

from examples import boards

def solve(algorithm):
    print(f"Running {algorithm.__class__.__name__} algorithm...")
    total_cost = 0
    state = initial_state

    actions =  algorithm.search()
    if actions is None:
        print("There is no solution")
        return
    
    for action in actions:
        print(action) 
        new_state = result_function.result(state, action)
        total_cost += step_cost_function.cost(state, action, new_state)
        state = new_state
        print(new_state)
    print(f"Total amount of the jumps: {total_cost}")

if __name__ == "__main__":
    for b in boards:
        board = b
        initial_state = FlappyBirdState(board)
        actions_function = FlappyBirdActionsFunction()
        result_function = FlappyBirdResultFunction()
        goal_test = FlappyBirdGoalTestFunction()
        step_cost_function = FlappyBirdStepCostFunction()
        problem = Problem(initial_state, actions_function, result_function, goal_test, step_cost_function)
        solve(BFS(problem))
        solve(UCS(problem))
    