import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
clock = pygame.time.Clock()
pygame.init()
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 3000)
TIME_EVENT =pygame.USEREVENT + 2
pygame.time.set_timer(TIME_EVENT, 1500)
clock = pygame.time.Clock()

enemy_bullet_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

class Wall:
    def __init__(self,x,y,w,h):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 60)
        self.speed_x = 7
        self.speed_y = 2
        self.jumping = False
        self.alive = True
        self.jump_timer = 12

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d] and self.rect.x + 30 < WIDTH:
            self.rect.x += self.speed_x
        if pressed_keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed_x


def jump(self):
    if self.jumping:
        if self.jump_timer >= -12:
            neg = 1
            if self.jump_timer < 0:
                neg = -1
            self.rect.y -= (self.jump_timer ** 2) // 10 * neg
            self.jump_timer -= 1
        else:
            self.jumping = False
            self.jump_timer = 12


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 60,30)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 20, 5), self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 7, 7)
        self.speed_x = 12

    def update(self):
        self.rect.x += self.speed_x

    def draw(self, screen):
        pygame.draw.rect(screen, (30, 40, 56), self.rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
        if event.type == TIME_EVENT:
            for i in enemy_group:
                enemy_bullet = Bullet(enemy.rect.x, enemy.rect.y + 30)
                enemy_bullet_group.add(enemy_bullet)
        if event.type == SPAWN_EVENT:
                enemy = Enemy(x=random.randint(1,940), y=random.randint(1,770))
                enemy_group.add(enemy)
