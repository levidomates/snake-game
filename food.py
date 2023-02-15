import pygame 
from settings import *
from random import choice 

class Food(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size-2,size-2))
        self.image.fill(food_color)
        self.rect = self.image.get_rect(topleft=pos)
        self.score = 1 

    def eat(self,snake,tail):

        if self.rect.colliderect(snake.sprite.rect):
            pos = choice(self.cordinate_create(tail))

            self.rect.x = pos[0]
            self.rect.y = pos[1]

            self.score += 1 

    def cordinate_create(self,tail):

        cordinate = []

        for x in range(0,width,size):
            for y in range(0,height,size):
                flag = True 
                for sprite in tail.sprites():
                    if sprite.rect.x == x and sprite.rect.y == y:
                        flag = False 
                if flag:    
                    cordinate.append((x,y))

        return cordinate

    def update(self,snake,tail):
        self.eat(snake,tail)