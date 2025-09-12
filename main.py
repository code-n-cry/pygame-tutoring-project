import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')

start_position = None
end_position = None
drawing = False
rectangle = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not drawing:
            start_position = event.pos
            drawing = True
        if event.type == pygame.MOUSEBUTTONDOWN and drawing:
            end_position = event.pos
            left = min(start_position[0], end_position[0])
            top = min(start_position[1], end_position[1])
            width = abs(end_position[0] - start_position[0])
            height = abs(end_position[1] - start_position[1])

            rectangle = pygame.Rect(left, top, width, height)
            pygame.draw.rect(screen, (107, 142, 35), rectangle)
            pygame.display.update()
            
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            end_position = event.pos
            drawing = False
            left = min(start_position[0], end_position[0])
            top = min(start_position[1], end_position[1])
            width = abs(end_position[0] - start_position[0])
            height = abs(end_position[1] - start_position[1])
            rectangle = pygame.Rect(left, top, width, height)
        screen.fill((0, 0, 0))
        if drawing:
            end_position = pygame.mouse.get_pos()
            left = min(start_position[0], end_position[0])
            top = min(start_position[1], end_position[1])
            width = abs(end_position[0] - start_position[0])
            height = abs(end_position[1] - start_position[1])
            rectangle = pygame.Rect(left, top, width, height)
        if rectangle:
            pygame.draw.rect(screen, (107, 142, 35), rectangle)
        clock.tick(60)
        pygame.display.flip()
pygame.quit()
