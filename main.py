import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shot = pygame.sprite.Group()

  AsteroidField.containers = (updatable,) 
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  Shot.containers = (shot, updatable, drawable)
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidField = AsteroidField()

  clock = pygame.time.Clock()
  dt = 0
  while True:
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
         return
       
     keys = pygame.key.get_pressed()
     if keys[pygame.K_SPACE]:
         new_shot = player.shoot()
         shot.add(new_shot)  
     
     for obj in updatable:
       obj.update(dt)
     
     for obj in asteroids:
       if obj.collision(player):
         sys.exit("Game over!")
     
     screen.fill((0, 0, 0))

     for obj in drawable:
       obj.draw(screen)

     pygame.display.flip()
     dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()