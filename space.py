import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.polygon(self.image, pygame.Color('dodgerblue'), ((0, 0), (32, 16), (0, 32)))
        self.org_image = self.image.copy()
        self.angle = 0
        self.direction = pygame.Vector2(1, 0)
        self.rect = self.image.get_rect(center=(200, 200))
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, events, dt):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.groups()[0].add(Projectile(self.rect.center, self.direction.normalize()))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.angle += 3
        if pressed[pygame.K_d]:
            self.angle -= 3

        print(self.angle)
        self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
        self.image = pygame.transform.rotate(self.org_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Projectile(pygame.sprite.Sprite):
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    sprites = pygame.sprite.Group(Player())
    clock = pygame.time.Clock()
    dt = 0

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
        sprites.update(events, dt)
        screen.fill((30, 30, 30))
        sprites.draw(screen)
        pygame.display.update()
        dt = clock.tick(60)

if __name__ == '__main__':
    main()
