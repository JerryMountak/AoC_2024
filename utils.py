class Direction:
    """A class representing a direction in a 2D grid.

    Raises:
        ValueError: If the grid coordinates are not integers.

    Returns:
        Direction: The direction object.
    """
    # Predefined class-level constants for directions
    Up = None
    Down = None
    Left = None
    Right = None
    _directions = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def turn_clockwise(self):
        # Get the index of the current direction and move to the next one clockwise
        index = Direction._directions.index(self)
        return Direction._directions[(index + 1) % 4]

    def turn_counterclockwise(self):
        # Get the index of the current direction and move to the next one counterclockwise
        index = Direction._directions.index(self)
        return Direction._directions[(index - 1) % 4]

    def __eq__(self, other):
        return isinstance(other, Direction) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Direction({self.x}, {self.y})"
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def move(self, other):
        # Check if other contains two integers
        if all(isinstance(item, int) for item in other):
            return (self.x + other[0], self.y + other[1])
        else:
            raise ValueError("Can only add directions with two integers")


# Define the directions and set up the circular list
Direction.Up = Direction(-1, 0)
Direction.Down = Direction(1, 0)
Direction.Left = Direction(0, -1)
Direction.Right = Direction(0, 1)
Direction._directions = [Direction.Up, Direction.Right, Direction.Down, Direction.Left]


def get_neighbors(grid, x, y, value=None):
    """Get the neighbors of a cell in a 2D grid.

    Args:
        grid (list[list[int]]): The 2D grid.
        x (int): The x coordinate of the cell.
        y (int): The y coordinate of the cell.

    Returns:
        list[int]: The neighbors of the cell.
    """
    neighbors = []
    for dir in [Direction.Up, Direction.Right, Direction.Down, Direction.Left]:
        dx, dy = dir.x, dir.y
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            if not value:
                neighbors.append((x+dx, y+dy, grid[x + dx][y + dy]))
            elif grid[x + dx][y + dy] == value:
                neighbors.append((x+dx, y+dy, grid[x + dx][y + dy]))

    return neighbors