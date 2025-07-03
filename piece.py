from random import choice

"""Module containing Tetromino piece definitions and logic.

This module defines the geometric shapes and colors for Tetris pieces,
and provides the Piece class that manages individual piece behavior.
"""

GEOMETRY = [
    # Each sublist represents a Tetromino shape as relative coordinates
    # Format: [[row_offset, col_offset], ...] relative to center position

    [[0, 0], [-1, 0], [-1, 1], [0, 1]],  # O-shaped piece (Square)
    [[0, 0], [0, -1], [0, 1], [0, 2]],  # I-shaped piece (Bar)
    [[0, 0], [0, -1], [0, 1], [1, 0]],  # T-shaped piece
    [[0, 0], [0, 1], [0, -1], [-1, -1]],  # J-shaped piece (Left L)
    [[0, 0], [0, -1], [0, 1], [-1, 1]],  # L-shaped piece (Right L)
    [[0, 0], [-1, -1], [-1, 0], [0, 1]],  # S-shaped piece
    [[0, 0], [-1, 0], [0, -1], [-1, 1]],  # Z-shaped piece
]

COLOR = [
    # RGB color tuples for each Tetromino type

    (0, 238, 238),  # Clear Blue
    (23, 1, 232),  # Dark blue
    (0, 238, 33),  # Green
    (153, 0, 239),  # Purple
    (238, 0, 20),  # Red
    (237, 238, 42),  # Yellow
    (255, 215, 0),  # Orange
]


class Piece:
    """Class representing a Tetromino piece in the game.

    Manages piece position, shape, color, and coordinate calculations.

    Attributes:
        center_row (int): Row position of the piece's center
        center_col (int): Column position of the piece's center
        relative_coords (list): List of [row, col] offsets from center
        color (tuple): RGB color value for the piece
    """
    def __init__(self) -> None:
        """Initialize a new Tetromino piece with random shape and color.

        Starts at top-middle position of the game board (row 0, column 4).
        Randomly selects shape from GEOMETRY and color from COLOR.
        """
        self.center_row = 0
        self.center_col = 4
        self.relative_coords = choice(GEOMETRY)
        self.color = choice(COLOR)

    @property
    def global_coords(self):
        """Calculate absolute coordinates of the piece's blocks.

        Combines center position with relative coordinates to get
        the actual position of each block on the game board.

        Returns:
            list: List of [row, col] absolute coordinates
        """
        return [
            [row + self.center_row, col + self.center_col]
            for row, col in self.relative_coords
        ]
