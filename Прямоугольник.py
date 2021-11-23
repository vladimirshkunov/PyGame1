import pygame


def draw_rect(screen, width, height):
    pygame.draw.rect(screen, pygame.Color('red'),
                     (1, 1, width - 2, height - 2))


if __name__ == '__main__':
    try:
        size = width, height = int(input()), int(input())
        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Прямоугольник')
        draw_rect(screen, width, height)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        pygame.quit()
    except ValueError:
        print('Неправильный формат ввода')
