import pygame 
from settings import * 
from sys import exit 
from snake import Snake
from food import Food

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake-game")

clock = pygame.time.Clock()

snake = pygame.sprite.GroupSingle()
snake.add(Snake((240,240)))

food = pygame.sprite.GroupSingle()
food.add(Food((120,120)))

def main():
    
    while True:

        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill('black')

        snake.draw(screen)
        snake.update(food.sprite.score)

        food.draw(screen)
        food.update(snake,snake.sprite.tail)

        if snake.sprite.game_over:
            
            snake.sprite.kill()
            food.sprite.kill()

            snake.add(Snake((240,240)))
            food.add(Food((120,120)))

        pygame.display.update()

if __name__ == '__main__':
    main()