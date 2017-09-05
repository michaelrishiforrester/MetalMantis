import pygame
import time

black = (0,0,0)
white = (255,255,255)
ocean_blue = (0, 119, 190)

pygame.init()

surfaceWidth = 1024
surfaceHeight = 800

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Dad\'s Nightmare of the Sea Game')
clock = pygame.time.Clock()

img = pygame.image.load('mantis_shrimp.png')

def blocks(x_block, y_block, block_width, block_height, gap)
    pygame.draw.rect(surface, white, [x_block, y_block,block_width,block_height])
    pygame.draw.rect(surface, white, [x_block, y_block+block_height+gap, block_width, block_height])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    return None


def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def msgSurface(text) :
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue kissing each other on the mouth', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(3)

    while replay_or_quit() == None:
        clock.tick()

    main()

def gameOver ():
    msgSurface('OneTWoThree, Death!')
    pygame.quit()
    quit ()

def helicopter(x, y, image):
    surface.blit(img, (x,y))

def main():

    x = 150
    y = 200
    y_move = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 20

        y += y_move

        surface.fill(ocean_blue)
        helicopter(x, y, img)
    #40 is the size of the Mantis shrimp image and 0 is the start of the range of pixels for height
        if y > surfaceHeight-40 or y < 0:
            gameOver()
        pygame.display.update()

        clock.tick(60)

main()
pygame.quit()
quit()

