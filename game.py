import pygame

from piece import Piece


class Game:
    """Main game class that manages Tetris gameplay mechanics.

    Attributes:
        screen (pygame.Surface): The Pygame surface to render on
        score (float): Current game score
        is_over (bool): Whether the game is over
        current_piece (Piece): The currently active Tetromino piece
        grid (list): 2D list representing the game board state
        grid_colors (list): 2D list storing colors for filled grid cells
    """
    def __init__(self, screen) -> None:
        """Initialize a new Tetris game instance.

        Args:
            screen (pygame.Surface): The Pygame surface to render on
        """
        self.screen = screen
        self.score = None
        self.is_over = True
        self.current_piece = None
        self.grid = None
        self.grid_colors = None

    def reset(self):
        """Reset the game to initial state, starting a new game.

        Resets score, creates new empty grid, and spawns first piece.
        """
        self.is_over = False
        self.score = 0.0
        self.grid = [[0, 0] * 10 for i in range(20)]
        self.grid_colors = [[None] * 10 for i in range(20)]
        self.current_piece = Piece()

    def move_left(self):
        """Move the current piece left if possible.

        Checks for collisions with grid boundaries or existing blocks.
        Only moves if there's space available to the left.
        """
        can_move_left = True

        for row, col in self.current_piece.global_coords:
            if col <= 0 or self.grid[row][col - 1] > 0.0:
                can_move_left = False

        if can_move_left:
            self.current_piece.center_col -= 1

    def move_right(self):
        """Move the current piece right if possible.

        Checks for collisions with grid boundaries or existing blocks.
        Only moves if there's space available to the right.
        """
        can_move_right = True

        for row, col in self.current_piece.global_coords:
            if col >= 9 or self.grid[row][col + 1] > 0.0:
                can_move_right = False

        if can_move_right:
            self.current_piece.center_col += 1

    def move_down(self):
        """Move the current piece down if possible.

        Checks for collisions with grid boundaries or existing blocks.
        Only moves if there's space available below.
        """
        can_move_down = True

        for row, col in self.current_piece.global_coords:
            if row >= 19 or self.grid[row + 1][col] > 0.0:
                can_move_down = False

        if can_move_down:
            self.current_piece.center_row += 1

    def rotate(self):
        """Rotate the current piece clockwise if possible.

        Checks for collisions after rotation. Only rotates if
        the new position would be valid (within bounds and no collisions).
        """
        new_coords = [[-col, row] for row, col in self.current_piece.relative_coords]
        new_global_coords = [
            [row + self.current_piece.center_row,
            col + self.current_piece.center_col]
            for row, col in new_coords
        ]

        for row, col in new_global_coords:
            if not 0 <= row < 20 or not 0 <= col < 10:
                return

        vals = [self.grid[row][col] for row, col in new_global_coords]

        if sum(vals) == 0.0:
            self.current_piece.relative_coords = new_coords


    def update(self):
        """Update game state for one frame.

        Automatically moves piece down, checks for completed lines,
        and detects game over conditions.
        """
        self.move_down()
        self._try_land_piece()
        self._clear_rows()

        if sum(self.grid[0]) > 0.0:
            self.is_over = True

    def render(self):
        """Render all game elements to the screen.

        Draws the current piece, all placed blocks, and the score display.
        """
        margin = 2
        width = self.screen.get_width() // 10
        height = self.screen.get_height() // 20

        for pr, pc in self.current_piece.global_coords:
            rect = [
                pc * width + margin,
                pr * height + margin,
                width - margin,
                height - margin,
            ]
            pygame.draw.rect(
                self.screen, self.current_piece.color, rect, border_radius=2
            )

        for row in range(20):
            for col in range(10):
                if self.grid[row][col]:
                    rect = [
                        col * width + margin,
                        row * height + margin,
                        width - margin,
                        height - margin,
                    ]
                    pygame.draw.rect(
                        self.screen, self.grid_colors[row][col], rect, border_radius=2
                    )

        font = pygame.font.SysFont('Calibri', 14, True, False)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        self.screen.blit(text,[10, 10])

    def _try_land_piece(self):
        try:
            # Land the piece.
            landed = False
            for row, col in self.current_piece.global_coords:
                if row >=19 or self.grid[row+1][col] > 0.0:
                    landed = True
                    break
            
            if landed:
                for row, col in self.current_piece.global_coords:
                    self.grid[row][col] = 1.0
                    self.grid_colors[row][col] = self.current_piece.color
                self.current_piece = Piece()

        except IndexError:
            return
        
    def _clear_rows(self):
        rows_to_delete = [i for i in range(20) if sum(self.grid[i]) == 10.0]
        self.grid = [self.grid[i] for i in range(20) if i not in rows_to_delete]
        self.grid_colors = [self.grid_colors[i] for i in range(20) if i not in rows_to_delete]

        for i in range(len(rows_to_delete)):
            self.grid.insert(0, [0.0] * 10)
            self.grid_colors.insert(0, [None] * 10)

        self.score += 10.0 * len(rows_to_delete)
        

