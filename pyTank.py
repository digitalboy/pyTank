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
        print(len(self.groups()))
        self.booTanktower = True
        self.boomSound = pygame.mixer.Sound('cannon.wav')
        self.boomSound.set_volume(0.5)
        #self.groups()[0].add(Tanktower(self.rect.center, self.direction.normalize()))


    def update(self, events, dt):
        #加入炮塔
        while self.booTanktower:
            self.groups()[0].add(Tanktower(self.rect.center, self.direction.normalize()))
            self.booTanktower = False

        #这是坦克和鼠标的极坐标差
        tankMousediff = pygame.mouse.get_pos() - pygame.Vector2(self.rect.center)
        tmDistance, tmTangle = pygame.math.Vector2.as_polar(tankMousediff)

        for e in events:
            #print("GGG:"+str(len(self.groups()[0])))
            if e.type ==  pygame.MOUSEBUTTONDOWN:
                self.groups()[0].add(Tankshell(self.rect.center, self.direction.normalize()))
                self.boomSound.play()

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


        xDistance = (pygame.mouse.get_pos()[0] - self.rect.x)/20
        yDistance = (pygame.mouse.get_pos()[1] - self.rect.y)/20

        pygame.time.Clock().tick(60)
        if tmDistance > 50:
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
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color('red'), (8, 8), 8)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, events, dt):
        self.pos = tankSprites.sprites()[0].rect.center
        self.rect.center = self.pos

class Target(pygame.sprite.Sprite):
    fenshu = 100
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color('yellow'), (10, 10), 10)
        self.rect = self.image.get_rect(center=(100,100))
        self.pos = pygame.Vector2(self.rect.center)
        self.t = pygame.sprite.Sprite()
        self.xMov = 1
        self.yMov = 1
        self.life = Target.fenshu
        self.painSound = pygame.mixer.Sound('monster-pain3.wav')
        self.painSound.set_volume(0.5)

    def update(self, tankGroup):
        if self.rect.left < 0:
            self.xMov = 1
        elif self.rect.right > 1000:
            self.xMov = -1
        if self.rect.top <= 0:
            self.yMov = 1
        elif self.rect.bottom >= 600:
            self.yMov = -1
        self.pos+=(self.xMov,self.yMov)
        targhit = pygame.sprite.spritecollideany(self,tankGroup)
        if targhit:
            self.painSound.play()
            self.life -= 1
            Target.fenshu = self.life
        self.rect.center = self.pos
    def retrnLife(self):
        return(str(Target.fenshu))

class Score():
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 42)
        self.image = self.font.render("Ready", True, (255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, valueDisplay):
        self.image = self.font.render(str(valueDisplay), True, (255, 255, 255))

pygame.init()
screen = pygame.display.set_mode((1000, 600))

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 20))

tankSprites = pygame.sprite.Group(Tankbody())

targetSpr = pygame.sprite.Group((Target()))

score = Score()
target = Target()

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

    dt = clock.tick(90)
    screen.blit(background, (0, 0))

    tankSprites.update(events, dt)
    tankSprites.draw(screen)

    targetSpr.update(tankSprites)
    targetSpr.draw(screen)

    score.update(target.retrnLife())
    screen.blit(score.image, (200, 0))

    pygame.display.flip()
