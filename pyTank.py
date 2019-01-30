import pygame

from pygame.locals import *

class Tankbody(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((26, 38))
        self.image.fill((100, 100, 100))
        self.image.set_colorkey((0, 0, 0))
        self.org_image = self.image.copy()
        self.angle = 0
        self.direction = pygame.Vector2(1, 0)
        self.rect = self.image.get_rect(center=(500, 300))
        self.pos = pygame.Vector2(self.rect.center)
        self.groups()[0].add(Tankshell(self.rect.center, self.direction.normalize()))


    def update(self, events, dt):
        #这是坦克和鼠标的极坐标差
        tankMousediff = pygame.mouse.get_pos() - pygame.Vector2(self.rect.center)
        tmDistance, tmTangle = pygame.math.Vector2.as_polar(tankMousediff)

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    print("111")#这里打算发射子弹
            if e.type ==  pygame.MOUSEBUTTONDOWN:
                self.groups()[0].add(Tankshell(self.rect.center, self.direction.normalize()))
                #self.groups()[0].add(Tankshell(self.rect.center, self.direction.normalize()-10))
                print(self.direction.normalize())

        self.image = pygame.transform.rotate(self.org_image, -tmTangle + 90)
        self.direction = pygame.Vector2(1, 0).rotate(tmTangle)
        self.rect = self.image.get_rect(center=self.rect.center)


        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


        xDistance = (pygame.mouse.get_pos()[0] - self.rect.x)/10
        yDistance = (pygame.mouse.get_pos()[1] - self.rect.y)/10

        #pygame.time.delay(50)
        if tmDistance > 20:
            self.rect.move_ip(xDistance,yDistance)


class Tankshell(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color('orange'), (4, 4), 4)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, events, dt):
        self.pos += self.direction * dt
        self.rect.center = self.pos
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()

class Tanktower(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color('red'), (8, 8), 8)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, events, dt):
        self.rect.center = self.pos
        print(dt)


pygame.init()
screen = pygame.display.set_mode((1000, 600))

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 20))

sprites = pygame.sprite.Group(Tankbody())

clock = pygame.time.Clock()
dt = 0

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    dt = clock.tick(60)
    screen.blit(background, (0, 0))

    sprites.update(events, dt)

    sprites.draw(screen)

    #pygame.display.update()

    pygame.display.flip()
