import pygame


def draw_lines(screen, window_size):
    pygame.draw.line(screen, pygame.Color('white'),
                     (0, 0), window_size, width=5)
    pygame.draw.line(screen, pygame.Color('white'),
                     (window_size[0], 0), (0, window_size[1]),
                     width=5)


if __name__ == '__main__':
    try:
        size = width, height = int(input()), int(input())
        print(size)
        pygame.init()
        pygame.display.set_caption('Крест')
        screen = pygame.display.set_mode(size)
        draw_lines(screen, size)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
    except ValueError:
        print('Неправильный формат ввода')
