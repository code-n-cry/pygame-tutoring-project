import pygame
import random

from pygame.examples.cursors import image

pygame.init()

WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')
bg_image = pygame.image.load('background.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 60)
        self.speed_x = random.randint(5,10)

    def update(self):
        self.rect.x -= self.speed_x

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 20, 5), self.rect)
        
        
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 60)
        self.speed_x = 7
        self.speed_y = 2
        self.jumping = False
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

    def draw(self, screen):
        pygame.draw.rect(screen, (90, 168, 25), self.rect)


player = Player(50, 448)
enemy_group=pygame.sprite.Group()
for i in range(5):
    enemy = Enemy(x = 650,y = 450)
    enemy_group.add(enemy)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.jumping = True
    for i in enemy_group:
        i.update()
        if pygame.sprite.collide_rect(i,player):
            player.kill()
        if i.rect.x < 0:
            i.kill()
    player.update()
    player.jump()
    screen.blit(bg_image, (0, 0))
    for i in enemy_group:
        i.draw(screen)
    player.draw(screen)
    clock.tick(60)
    pygame.display.flip()
