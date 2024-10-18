import pygame

from piece import Piece


class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.score = None
        self.is_over = True
        self.current_piece = None
        self.grid = None
        self.grid_colors = None

    # Reset.
    def reset(self):
        self.is_over = False
        self.score = 0.0
        self.grid = [[0, 0] * 10 for i in range(20)]
        self.grid_colors = [[None] * 10 for i in range(20)]
        self.current_piece = Piece()

    # Move left.
    def move_left(self):
        can_move_left = True

        for row, col in self.current_piece.global_coords:
            if col <= 0 or self.grid[row][col - 1] > 0.0:
                can_move_left = False

        if can_move_left:
            self.current_piece.center_col -= 1

    # Move right.
    def move_right(self):
        can_move_right = True

        for row, col in self.current_piece.global_coords:
            if col >= 9 or self.grid[row][col + 1] > 0.0:
                can_move_right = False

        if can_move_right:
            self.current_piece.center_col += 1

    # Move down.
    def move_down(self):
        can_move_down = True

        for row, col in self.current_piece.global_coords:
            if row >= 19 or self.grid[row + 1][col] > 0.0:
                can_move_down = False

        if can_move_down:
            self.current_piece.center_row += 1

    # Rotate.
    def rotate(self):
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


    # Update.
    def update(self):
        self.move_down()
        self._try_land_piece()
        self._clear_rows()

        if sum(self.grid[0]) > 0.0:
            self.is_over = True

    # Render.
    def render(self):
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
        

