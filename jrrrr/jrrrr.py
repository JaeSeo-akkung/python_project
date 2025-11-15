import pygame
import sys
import random

# -----------------------------
# Game config
# -----------------------------
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

FPS_BASE = 10           # 기본 프레임(속도)
SPEED_STEP = 0.8        # 일정 점수마다 속도 증가 비율
SPEED_UP_EVERY = 5      # 점수 5점마다 속도 증가

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
GREEN = (0, 200, 0)
RED = (200, 40, 40)
YELLOW = (240, 200, 0)
BLUE = (50, 150, 255)

# -----------------------------
# Utility
# -----------------------------
def draw_grid(surface):
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(surface, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(surface, GRAY, (0, y), (WIDTH, y))

def random_cell(exclude=None):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if not exclude or pos not in exclude:
            return pos

# -----------------------------
# Snake class
# -----------------------------
class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        center = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.body = [center, (center[0] - 1, center[1]), (center[0] - 2, center[1])]
        self.direction = (1, 0)   # moving right
        self.pending_dir = self.direction
        self.grow = 0

    def set_direction(self, new_dir):
        # Prevent reversing directly
        if (new_dir[0] == -self.direction[0] and new_dir[1] == -self.direction[1]):
            return
        self.pending_dir = new_dir

    def move(self):
        self.direction = self.pending_dir
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        if self.grow > 0:
            self.grow -= 1
        else:
            self.body.pop()

    def collide_self(self):
        return self.body[0] in self.body[1:]

    def collide_wall(self):
        x, y = self.body[0]
        return x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT

    def draw(self, surface):
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = GREEN if i == 0 else (0, 140, 0)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

# -----------------------------
# Food class
# -----------------------------
class Food:
    def __init__(self, snake):
        self.position = random_cell(exclude=set(snake.body))
        self.color = RED

    def respawn(self, snake):
        self.position = random_cell(exclude=set(snake.body))

    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)

# -----------------------------
# Game loop
# -----------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game (Arrow keys to move, R to restart)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 22)
    big_font = pygame.font.SysFont("consolas", 36)

    snake = Snake()
    food = Food(snake)
    score = 0
    fps = FPS_BASE
    game_over = False

    def draw_hud():
        text = f"Score: {score}   Speed: {fps:.1f} FPS"
        surface = font.render(text, True, WHITE)
        screen.blit(surface, (10, 10))

    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    snake.set_direction((0, -1))
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    snake.set_direction((0, 1))
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    snake.set_direction((-1, 0))
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake.set_direction((1, 0))
                elif event.key == pygame.K_r and game_over:
                    # Restart game
                    snake.reset()
                    food = Food(snake)
                    score = 0
                    fps = FPS_BASE
                    game_over = False

        if not game_over:
            snake.move()

            # Collisions
            if snake.collide_wall() or snake.collide_self():
                game_over = True

            # Eat food
            if snake.body[0] == food.position:
                score += 1
                snake.grow += 1
                food.respawn(snake)

                # Speed up every SPEED_UP_EVERY points
                if score % SPEED_UP_EVERY == 0:
                    fps = min(30, fps + SPEED_STEP)

        # Draw
        screen.fill((25, 25, 25))
        draw_grid(screen)
        food.draw(screen)
        snake.draw(screen)
        draw_hud()

        if game_over:
            msg1 = big_font.render("Game Over", True, YELLOW)
            msg2 = font.render("Press R to restart", True, BLUE)
            msg3 = font.render("Arrow keys or WASD to move", True, WHITE)
            screen.blit(msg1, (WIDTH // 2 - msg1.get_width() // 2, HEIGHT // 2 - 40))
            screen.blit(msg2, (WIDTH // 2 - msg2.get_width() // 2, HEIGHT // 2 + 5))
            screen.blit(msg3, (WIDTH // 2 - msg3.get_width() // 2, HEIGHT // 2 + 30))

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()


