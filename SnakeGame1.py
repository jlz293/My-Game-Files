import pygame
import random

pygame.init()


white = (255,255,255)
black = (0, 0, 0)
red = (255, 100, 100)
green = (0,155,0)

displayX = 700
displayY = 700
BlockSize = 10
FPS = 30
appleThickness = 40

clock = pygame.time.Clock()


gameDisplay = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Slither")

font = pygame.font.SysFont(None, 25)


def apple(randAppleX, randAppleY, appleThickness):
    pygame.draw.rect(gameDisplay, green, [randAppleX, randAppleY, appleThickness, appleThickness])


def snake(snakeList, BlockSize):
    for XY in snakeList:
        pygame.draw.rect(gameDisplay, red, [XY[0], XY[1], BlockSize, BlockSize])


def message_screen(msg, color):
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [displayX /6, displayY / 2])


def gameLoop():
    lead_x = displayX/2
    lead_y = displayY/2
    x_change = 0
    y_change = 0
    gameExit = False
    gameOver = False

    randAppleX = round(random.randrange(0, displayX-appleThickness)/10)*10
    randAppleY = round(random.randrange(0, displayY-appleThickness)/10)*10

    snakeList = []
    snakeLength = 1

    while not gameExit:



        while gameOver:
            gameDisplay.fill(black)
            message_screen("Game Over press C to play again or Q to quit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BlockSize
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change  = BlockSize
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BlockSize
                    x_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BlockSize
                    x_change = 0
                    #If you want the snake to stop when you stop pressing the key:
            '''if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0'''




        if lead_x >= displayX or lead_x <= 0 or lead_y >= displayY or lead_y <= 0:
                gameOver = True



        lead_x += x_change
        lead_y += y_change
        gameDisplay.fill(white)
        apple(randAppleX, randAppleY, appleThickness)

        snakeHead = []

        snakeHead.append(lead_x)
        snakeHead.append(lead_y)

        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachBox in snakeList[:-1]:
            if eachBox == snakeHead:
                gameOver = True

        snake(snakeList, BlockSize)
        pygame.display.update()

        if lead_x >= randAppleX and (lead_x <= randAppleX+appleThickness) and lead_y >= randAppleY and (lead_y <= randAppleY + appleThickness):
            snakeLength += 1
            randAppleX = round(random.randrange(0, displayX - appleThickness) / 10) * 10
            randAppleY = round(random.randrange(0, displayY - appleThickness) / 10) * 10




        clock.tick(FPS)



    pygame.quit()

    quit()

gameLoop()
