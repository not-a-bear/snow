import random, sys, math

import pygame

pygame.init()

# basic screen settings
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snowfall')

class Snow(pygame.sprite.Sprite):

    def __init__(self, top_left_coord):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = top_left_coord
        self.trig = random.randint(1, 2)
        self.velocity = 2
        self.unique = random.uniform(1, 2*math.pi)


    def update(self):
        time = pygame.time.get_ticks()
        self.y = self.velocity + (self.unique/3)
        self.x = math.sin((time/500)+self.unique)*3
        self.rect.move_ip(self.x, self.y)

        if self.rect.top > HEIGHT:
            self.kill()


# initialize snows as pygame Group        
snows = pygame.sprite.Group()

def main():
    # define run, set clock and spawn timer for snows
    run = True
    clock = pygame.time.Clock()
    snow_spawn = 100
    snow_timer = 0
    
    while run:
        # start snow timer with FPS of 60
        snow_timer += clock.tick(60)

        screen.fill('black')  
        
        # event handler only for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        # spawn a new snow every 100 ticks
        if snow_timer > snow_spawn:
            snow = Snow((random.randint(0, WIDTH), 0))
            snows.add(snow)
            snow_timer = 0

        # update positions and draw to screen
        snows.update()
        snows.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()


