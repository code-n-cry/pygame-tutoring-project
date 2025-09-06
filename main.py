import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')

rectange = pygame.Rect(100, 100, 400, 400)
#pygame.draw.rect(screen, (107, 142, 35), rectange)
#pygame.draw.circle(screen, (107, 142, 35), (400, 300), 50)
#surface = pygame.display.get_surface()
start_position = [0,0]
end_position = [0,0]
count = 0

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            count += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            count += 1
            if count % 2 == 1:
                start_position = event.pos
            if count % 2 == 0:
                end_position = event.pos
                rectange = pygame.Rect( start_position[0],start_position[1],end_position[0],end_position[1] )
                pygame.draw.rect(screen, (107, 142, 35), rectange)
    pygame.display.update()



