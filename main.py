import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosin import Explosion


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    img = pygame.image.load("images/asteroids-backgroundimage.jpg")
    pygame.font.init()
    game_font = pygame.font.SysFont('Arial',24)
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    Player.containers = (updatable,drawable) 
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    asteriod_field = AsteroidField()
    Shot.containers = (shots,updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                print("Score:",player.score)
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()

                    player.score = player.score + 100

                    explosion = Explosion(asteroid.position.x,asteroid.position.y)
                    explosions.add(explosion)
                    shot.kill()
            

        #screen.fill("black")
        screen.blit(img,(0,0))

        text_score = "Score: "+ str(player.score)
        text_surface = game_font.render(text_score,False,"white")
        screen.blit(text_surface,(SCREEN_WIDTH/2,16))
        explosions.draw(screen)
        explosions.update()
        #pygame.display.update()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        time=clock.tick(60)
        dt=time/1000
        


if __name__ == "__main__":
    main()
