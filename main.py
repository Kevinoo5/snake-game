import pygame
import sys
import random

from pygame import Rect

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 480
GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE
BLACK = (0,0,0)
LBORDER = pygame.Rect(0.3, 1, 1, SCREEN_HEIGHT)
#RBORDER =
UBORDER = pygame.Rect(1, 1, 480, 1)
#DBORDER =
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)
class Snake(object):

    def __init__(self):
        self.length = 1
        self.pos = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.facing = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0,151,255)
    def head_pos(self):
        return self.pos[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.facing:
            return
        else:
            self.facing = point
    def reset(self):

        self.length = 1
        self.pos = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.facing = random.choice([UP, DOWN, LEFT, RIGHT])


    def move(self):
        cur = self.head_pos()
        x, y = self.facing
        new = (((cur[0] + (x * GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.pos) > 2 and new in self.pos[2:]:
            self.reset()
        else:
            self.pos.insert(0, new)
            if len(self.pos) > self.length:
                self.pos.pop()



    def draw(self, surface):
        for p in self.pos:
            first = pygame.Rect((p[0], p[1]), (GRIDSIZE,GRIDSIZE))
            pygame.draw.rect(surface, self.color, first)
            pygame.draw.rect(surface, (93,216, 228), first, 1)
        if first.colliderect(LBORDER) or first.colliderect(UBORDER):
            pygame.quit()


    def keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

class Food(object):
    def __init__(self):
        self.position = (random.randint(0,GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)
        self.color = (255,0,0)


    def random_pos(self):
        self.position = (random.randint(0, GRID_WIDTH-1)*GRIDSIZE, random.randint(0, GRID_HEIGHT-1)*GRIDSIZE)

    def draw(self, surface):
        second = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, second)
        pygame.draw.rect(surface, (93, 216, 228), second, 1)


def main():
    run = True
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)


    snake = Snake()
    food = Food()

    score = 0
    while run:
        clock.tick(10)
        snake.keys()
        drawGrid(surface)
        snake.move()
#         pygame.draw.rect(surface, BLACK, LBORDER, 10)
#         pygame.draw.rect(surface, BLACK, UBORDER, 10)

        if snake.head_pos() == food.position:
            snake.length += 1
            score += 1
            food.random_pos()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



    pygame.quit()


main()
