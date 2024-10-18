import pygame

from game import Game

SCREEN_SIZE = WIDTH, HEIGHT = 400, 800

if __name__ == "__main__":
    # Initalize the game.
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    fps = 3

    window_closed = False
    game = Game(screen)

    # Black screen. Text message to user...
    while not window_closed:
        screen.fill((0, 0, 0))

        if game.is_over:
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

    # Display score to the user.

    # Close window when user quits.
