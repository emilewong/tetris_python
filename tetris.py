import pygame

from game import Game

"""Main entry point for the Tetris game application.

This module initializes the Pygame environment, sets up the game window,
and runs the main game loop that handles user input, game updates, and rendering.
"""

# Screen dimensions (width, height) in pixels
SCREEN_SIZE = WIDTH, HEIGHT = 400, 800

if __name__ == "__main__":
    """Initialize and run the Tetris game.

    Sets up Pygame, creates the game window, and starts the main game loop.
    Handles window events, user input, game state updates, and rendering.
    """
    # Initialize Pygame and game components
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    fps = 3

    window_closed = False
    game = Game(screen)

    # Main game loop - runs until window is closed
    while not window_closed:
        screen.fill((0, 0, 0))

        if game.is_over:
            # Game over state - display start prompt and last score
            font = pygame.font.SysFont("Calibri", 18, True, False)
            text = font.render("Press enter to start the game", True, (255, 255, 255))
            screen.blit(text, (80, HEIGHT // 2 + 40))

            if game.score is not None:
                score_text = font.render(
                    f"Last score: {game.score}", True, (255, 255, 255)
                )
                screen.blit(score_text, (80, HEIGHT // 2 + 80))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_closed = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game.reset()
        else:
            # Active game state - handle input, update and render game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_closed = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game.rotate()

                    elif event.key == pygame.K_LEFT:
                        game.move_left()

                    elif event.key == pygame.K_RIGHT:
                        game.move_right()

                    elif event.key == pygame.K_DOWN:
                        game.move_down()

            game.update()
            game.render()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

    # Clean up Pygame resources before exiting
    pygame.quit()
