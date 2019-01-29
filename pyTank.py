import pygame

from pygame.locals import *

class Tankbody(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((26, 38))
        self.image.fill((100, 100, 100))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.polygon(self.image, pygame.Color('dodgerblue'), ((0, 8), (26, 8), (13, 0)))
        #pygame.draw.rect(self.image, (0,255,0), (60,10,50,50))

        self.org_image = self.image.copy()
        self.angle = 0
        self.direction = pygame.Vector2(1, 0)
        #self.rect = self.image.get_rect(center=(200, 200))
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(self.rect.center)
        self.timeRunX = 1
        self.timeRunY = 1
        self.tankMouseAgle = 0

    def update(self, pressed_keys,event):

        if pressed_keys[pygame.K_a]:
            print("ok")
        if pressed_keys[pygame.K_d]:
            print("123")

        for event in pygame.event.get():
            if event.type ==  MOUSEBUTTONDOWN:
                print("mm")

        tankMousediff = pygame.mouse.get_pos() - pygame.Vector2(self.rect.center)
        #print(tankMousediff[1])

        self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
        #self.image = pygame.transform.rotate(self.org_image, -tankMousediff[1])
        self.rect = self.image.get_rect(center=self.rect.center)

        #坦克和鼠标的角度
        tankMousediff = pygame.mouse.get_pos() - pygame.Vector2(self.rect.center)

        #print(tankMousediff[1])

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

        aguAcceleration = 100 #加速度调整参数


        xDistance = (pygame.mouse.get_pos()[0] - self.rect.x)/10
        yDistance = (pygame.mouse.get_pos()[1] - self.rect.y)/10
        #print(xDistance)
        pygame.time.delay(50)
        #self.rect.move_ip(xDistance,yDistance)



        # if abs(self.rect.x - pygame.mouse.get_pos()[0]) < 50 and self.timeRunX < 100:
        #     self.timeRunX += 1
        #     # print("X_dis:"+ str(abs(self.rect.x - pygame.mouse.get_pos()[0])))
        #     # print("TimX:" + str(self.timeRunX))
        # else:
        #     self.timeRunX = round(abs(self.rect.x - pygame.mouse.get_pos()[0])/aguAcceleration)
        #
        #
        # if self.rect.x + self.rect.width/2 < pygame.mouse.get_pos()[0]:
        #     pygame.time.delay(self.timeRunX)
        #     self.rect.x += 1
        # elif self.rect.x + self.rect.width/2 > pygame.mouse.get_pos()[0]:
        #     pygame.time.delay(self.timeRunX)
        #     self.rect.x -= 1
        #
        # #纵轴速度调节
        #
        # if abs(self.rect.y - pygame.mouse.get_pos()[1]) < 40 and self.timeRunY < 100:
        #     self.timeRunY += 1
        # else:
        #     self.timeRunY = round(abs(self.rect.y - pygame.mouse.get_pos()[1])/aguAcceleration)
        #
        #
        # if self.rect.y + self.rect.height/2 < pygame.mouse.get_pos()[1]:
        #     pygame.time.delay(self.timeRunY)
        #     self.rect.y += 1
        # elif self.rect.y + self.rect.height/2 > pygame.mouse.get_pos()[1]:
        #     pygame.time.delay(self.timeRunY)
        #     self.rect.y -= 1





class Tanktower(pygame.sprite.Sprite):
    def __init__(self):
        super(Tanktower, self).__init__()
        self.surf = pygame.Surface((15, 20))
        self.surf.fill((255, 50, 100))
        self.rect = self.surf.get_rect()
        self.draw = pygame.draw.circle(self.surf,(0,20,255),[10,100],3,1)

    def update(self):
        self.surf = pygame.transform.rotate(self.surf, 32)
        self.rect = self.get_rect.copy()
        self.rect.center = self.get_rect.center


pygame.init()
screen = pygame.display.set_mode((1000, 600))

tankbody = Tankbody()
tanktower = Tanktower()

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 20))

all_sprites = pygame.sprite.Group()
all_sprites.add(tankbody)
all_sprites.add(tanktower)
#print(all_sprites)

running = True
#pygame.mouse.set_visible(True)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    tankbody.update(pressed_keys)

    #tankbody.image = pygame.transform.rotate(tankbody.image, 90)

    # for entity in all_sprites:
    #     #print(entity.rect)
    #     screen.blit(entity.surf, entity.rect)


    screen.blit(tankbody.image,tankbody.rect)
    screen.blit(tanktower.surf,tanktower.rect)

    tanktower.rect.x=tankbody.rect.x+(tankbody.rect.width-tanktower.rect.width)/2
    tanktower.rect.y=tankbody.rect.y+(tankbody.rect.height-tanktower.rect.height)/2



    pygame.draw.circle(screen,(0,255,255),[100,100],38,1)

    pygame.display.flip()
