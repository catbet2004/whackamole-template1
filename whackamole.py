import pygame
import random

def draw_grid(screen):
    color=(0,0,0)
    for x in range(0,641,32):
        pygame.draw.line(screen,color,(x,0),(x,512))
    for y in range(0,513,32):
        pygame.draw.line(screen,color,(0,y),(640,y))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        #initial random position for the mole
        x=random.randrange(0,640,32)
        y=random.randrange(0,512,32)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    mole_rect=mole_image.get_rect(topleft=(x,y))
                    if mole_rect.collidepoint(click_x,click_y):
                        #move mole to new random position
                        x = random.randrange(0, 640, 32)
                        y = random.randrange(0, 512, 32)

            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
    main()