import pygame
import PIL.Image


def main():
    pygame.init()  # init
    background = 'board.jpg'  # background image
    window_size = PIL.Image.open(r'{}'.format(background))  # getting size of image
    X, Y = window_size.size     # size to X Y
    black = (0, 0, 0)       # black color

    display_surface = pygame.display.set_mode((X, Y))  # window size of X & Y

    pygame.display.set_caption('Chess')  # title

    image = pygame.image.load(r'{}'.format(background))
    while True:
        display_surface.fill(black)
        display_surface.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()


if __name__ == '__main__':
    main()
