import sys, pygame
pygame.init()

size = width, height = 1000, 700
speed = [0, 0]
direction = 1
black = 0, 0, 0

screen = pygame.display.set_mode(size)

snake = pygame.image.load("tankbody.png")
snakerect = snake.get_rect()
snakerect.right = width/2
snakerect.top = height/2

score = 0

rightcount = 0
leftcount = 0
topcount = 0
bottomcount = 0
while 1:
    if snakerect.right > width:
        speed[0] = 0
        snakerect.right = width
    if snakerect.left < 0:
        speed[0] = 0
        snakerect.left = 0
    if snakerect.bottom > height:
        speed[1] = 0
        snakerect.bottom = height
    if snakerect.top < 0:
        speed[1] = 0
        snakerect.top = 0
    snakerect = snakerect.move(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = -1
                speed[1] = 0
                if direction == 2:
                    snake = pygame.transform.rotate(snake, 180)
                if direction == 1:
                    snake = pygame.transform.rotate(snake, 270)
                if direction == 0:
                    snake = pygame.transform.rotate(snake, 90)
                direction = 3
            if event.key == pygame.K_RIGHT:
                speed[0] = 1
                speed[1] = 0
                if direction == 3:
                    snake = pygame.transform.rotate(snake, 180)
                if direction == 0:
                    snake = pygame.transform.rotate(snake, 270)
                if direction == 1:
                    snake = pygame.transform.rotate(snake, 90)
                direction = 2
            if event.key == pygame.K_DOWN:
                speed[1] = 1
                speed[0] = 0
                if direction == 0:
                    snake = pygame.transform.rotate(snake, 180)
                if direction == 3:
                    snake = pygame.transform.rotate(snake, 90)
                if direction == 2:
                    snake = pygame.transform.rotate(snake, 270)
                direction = 1
            if event.key == pygame.K_UP:
                speed[1] = -1
                speed[0] = 0
                if direction == 1:
                    snake = pygame.transform.rotate(snake, 180)
                if direction == 2:
                    snake = pygame.transform.rotate(snake, 90)
                if direction == 3:
                    snake = pygame.transform.rotate(snake, 270)
                direction = 0

    screen.fill(black)
    screen.blit(snake, snakerect)
    pygame.display.flip()
