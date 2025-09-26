from typing import List

from search_algorithms.interfaces import State, Action, ActionsFunction, ResultFunction, GoalTestFunction, StepCostFunction
from board import FlappyBirdBoard

class FlappyBirdState(State):
    def __init__(self, board: FlappyBirdBoard) -> None:
        self.board = board
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, FlappyBirdState) and self.board == other.board

    def __hash__(self) -> int:
        return hash(self.board)
    
    def __str__(self) -> str:
         return str(self.board)
    
class FlappyBirdAction(Action): 
    def __init__(self, jump: bool) -> None: #jump true if the player decides to jump with the bird
        self.jump = jump
    
    def __str__(self) -> str:
        return "up" if self.jump else "down"

class FlappyBirdActionsFunction(ActionsFunction):
    def actions(self, state: FlappyBirdState) -> List[FlappyBirdAction]:
        actions = []
        row, column = state.board.get_bird_position()
        column += 1 #the bird will always move to the right
        #for the jump
        if row - 1 >= 0 and column < state.board.num_columns and state.board.get_value(row-1,column) == " ":
            actions.append(FlappyBirdAction(True))

        #fall
        if row + 1 < state.board.num_rows and column < state.board.num_columns and state.board.get_value(row+1,column) == " ": 
            actions.append(FlappyBirdAction(False))

        return actions
    
class FlappyBirdResultFunction(ResultFunction):
    def result(self, state: FlappyBirdState, action: FlappyBirdAction) -> FlappyBirdState:
        new_board = state.board.clone()
        #updating the bird's position and deleting the previous one
        row, column = new_board.get_bird_position() 
        new_board.set_value(row, column," ") #deleted
        if action.jump: #bird jumped
            new_row = row - 1
        else:
            new_row = row + 1
        new_column = column + 1 #always moves to the right
        new_board.set_value(new_row, new_column,"O")
        return FlappyBirdState(new_board)
    
class FlappyBirdGoalTestFunction(GoalTestFunction): #goal is to reach the end of a board (column - 1)
    def is_goal_state(self, state: FlappyBirdState) -> bool:
        row, column = state.board.get_bird_position() 
        return column == state.board.num_columns - 1
    
class FlappyBirdStepCostFunction(StepCostFunction):
    def cost(self, state: FlappyBirdState, action: FlappyBirdAction, state1: FlappyBirdState) -> float:
        return 1.0 if action.jump else 0.0
