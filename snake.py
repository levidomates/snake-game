import pygame 
from settings import * 

class Snake(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size-2,size-2))
        self.image.fill(snake_color)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.direction.x = 1 
        self.speed = 4 
        self.tail = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()
        self.game_over = False 

    def input(self):

        key = pygame.key.get_pressed()
        
        if key[pygame.K_w] and self.direction.y != 1:
            self.direction.y = -1
            self.direction.x = 0
        elif key[pygame.K_s] and self.direction.y != -1:
            self.direction.y = 1
            self.direction.x = 0
        elif key[pygame.K_a] and self.direction.x != 1:
            self.direction.x = -1
            self.direction.y = 0
        elif key[pygame.K_d] and self.direction.x != -1:
            self.direction.x = 1
            self.direction.y = 0

    def apply_speed(self):
        self.rect.x += self.direction.x * self.speed 
        self.rect.y += self.direction.y * self.speed 

    def control_square(self):
        flag = False 
        if self.rect.x % size == 0 and self.rect.y % size == 0:
            flag = True
        return flag 
    
    def tp(self):

        if self.rect.x > width-size:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = width-size
        
        if self.rect.y > height-size:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = height-size
    
    def tail_create(self):
        self.tail.add(Tail((self.rect.x,self.rect.y)))

    def tail_delete(self,score):
        if len(self.tail.sprites()) > score:
            self.tail.sprites()[0].kill()

    def tail_bite(self):
        count = 0
        for sprite in self.tail.sprites():
            if sprite.rect.colliderect(self.rect):
                count += 1

        if count > 1:
            self.game_over = True 

    def update(self,score):
        
        if self.control_square():
            self.input()
            self.tail_create()

        self.apply_speed()
        self.tp()
        self.tail_delete(score)
        self.tail_bite()

        self.tail.draw(self.display_surface)

class Tail(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size-2,size-2))
        self.image.fill(snake_color)
        self.rect = self.image.get_rect(topleft=pos)

    