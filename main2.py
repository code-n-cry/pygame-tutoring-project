import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(10, 500, 100, 100)
        self.speed_x = random.randint(5,15)
        self.speed_y = random.randint(5,15)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.x + 100 > WIDTH or self.rect.x < 0:
            self.speed_x = -self.speed_x
        if  self.rect.y < 0 or self.rect.y + 100 > HEIGHT:
            self.speed_y = -self.speed_y
        '''pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d] and self.rect.x + 100 < WIDTH:
            self.rect.x += self.speed_x
        if pressed_keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed_x
        if pressed_keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if pressed_keys[pygame.K_s] and self.rect.y + 100 < HEIGHT:
            self.rect.y += self.speed_y'''



player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    player.update()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player.rect)
    clock.tick(60)
    pygame.display.flip()

