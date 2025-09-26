from typing import List, Tuple

class FlappyBirdBoard:
    
    def __init__(self, board: List[List[int]], num_rows: int, num_columns: int) -> None:
        """Initializes the board.
        
        Args:
            board (List[List[int]]): The board.
            num_rows (int): The number of rows.
            num_columns (int): The number of columns.
        """
        self.board = board
        self.num_rows = num_rows
        self.num_columns = num_columns

    def __eq__(self, other: object) -> bool:
        """Checks if the given object is equal to this object.
        
        Args:
            other (object): The other object.
        """
        return isinstance(other, FlappyBirdBoard) and self.board == other.board and self.num_rows == other.num_rows and self.num_columns == other.num_columns
    
    def __hash__(self) -> int:
        """Returns the hash value of this object.
        
        Returns:
            int: The hash value of this object.
        """
        return hash(str(self.board))
    
    def __str__(self) -> str:
        """Returns the string representation of the board.
        
        Returns:
            str: The string representation of the board.
        """
        result = "-" * (2 * self.num_columns + 1) + "\n"
        for row in self.board:
            result += "|"
            result += " ".join([cell for cell in row]) + "|\n"
        result += "-" * (2 * self.num_columns + 1)
        return result
    
    def clone(self) -> "FlappyBirdBoard":
        """Returns a clone object of the board.
        
        Returns:
            FlappyBirdBoard: A clone of the board.
        """
        return FlappyBirdBoard([row[:] for row in self.board], self.num_rows, self.num_columns)
    
    def get_value(self, row: int, column: int) -> int:
        """Returns the value at the given position on the board.
        
        Args:
            row (int): The row.
            column (int): The column.
            
        Returns:
            int: The value at the given position on the board.
        """
        return self.board[row][column]
    
    def set_value(self, row: int, column: int, value: str) -> None:
        """Sets the value at the given position on the board.
        
        Args:
            row (int): The row.
            column (int): The column.
            value (int): The value.
        """
        self.board[row][column] = value
    
    def get_bird_position(self) -> Tuple[int,int]:
        """ Returns the position of the bird on a board. """
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if self.board[i][j] == "O":
                    return i, j
        return None
