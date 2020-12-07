import pygame
import basicClass


pygame.init()
W = H = 1024  # width and height
board_size = 8  # size is 8x8
single_square_size = H // board_size
imgs = {}  #saving images in dictionary


def pieces_images():  # loading all images into dictionary
    pieces = ['1', '2', '3', '4', '5', '6', '-1', '-2', '-3', '-4', '-5', '-6']
    for p in pieces:
        imgs[p] = pygame.transform.scale(pygame.image.load("images_pieces/" + p + ".png"), (single_square_size, single_square_size))


def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))  # creating a window
    screen.fill(pygame.Color("white"))  # filling it white for a sec
    board = basicClass.basicBoard()
    pieces_images()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        drawGame(screen, board)
        pygame.display.flip()


def drawGame(screen, board):
    Board(screen)
    Pieces(screen, board.background)


def Board(screen):
    colors = [pygame.Color("white"), pygame.Color("wheat")]
    for r in range(board_size):
        for c in range(board_size):
            color = colors[((r+c)%2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*single_square_size, r*single_square_size, single_square_size, single_square_size))


def Pieces(screen, background):
    for r in range(board_size):
        for c in range(board_size):
            setted = background[r][c]
            if setted != "0":
                screen.blit(imgs[setted], pygame.Rect(c*single_square_size, r*single_square_size, single_square_size, single_square_size))


if __name__ == '__main__':
    main()
