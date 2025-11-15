import pygame
import random
import sys

# pygame 초기화
pygame.init()

# 화면 크기
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1000

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 한글을 지원하는 글꼴 경로 설정
FONT_PATH = "C:\\Windows\\Fonts\\malgun.ttf"
FONT = pygame.font.Font(FONT_PATH, 74)
SMALL_FONT = pygame.font.Font(FONT_PATH, 36)

# 화면 초기화
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("라면먹기 게임")

# 시계
clock = pygame.time.Clock()

# 게임 변수
ramen_clicks_needed = 20  # 라면을 먹기 위해 필요한 클릭 수를 20으로 고정
ramen_clicks = 0
start_time = None
elapsed_time = 0

def reset_game():
    global ramen_clicks, start_time, elapsed_time
    ramen_clicks = 0
    start_time = pygame.time.get_ticks()
    elapsed_time = 0

game_state = "main"  # 가능한 상태: main, playing, finished



start_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 100)
retry_button = pygame.Rect(SCREEN_WIDTH - 200, SCREEN_HEIGHT - 100, 150, 50)

# 라면 이미지 로드
ramen_images = [
    pygame.image.load("ramen_full.png"),  # 가득 찬 라면
    pygame.image.load("ramen_half.png"),  # 반쯤 먹은 라면
    pygame.image.load("ramen_empty.png"), # 빈 그릇
]

# 젓가락 이미지 로드 및 크기 조정
chopstick_image = pygame.image.load("chopstick.png")
chopstick_image = pygame.transform.scale(chopstick_image, (500, 350))  # 크기를 조금 더 키움
chopstick_x = SCREEN_WIDTH // 2
chopstick_y = SCREEN_HEIGHT // 2 - 200

# 메인 메뉴 그리기
def draw_main_menu():
    screen.fill(WHITE)
    title_text = FONT.render("라면먹기 게임", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

    pygame.draw.rect(screen, RED, start_button)
    start_text = SMALL_FONT.render("START", True, WHITE)
    screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                             start_button.y + start_button.height // 2 - start_text.get_height() // 2))

# 게임 화면 그리기
def draw_game():
    screen.fill(WHITE)

    # 젓가락 이미지 그리기 (맨 뒤로 이동)
    screen.blit(chopstick_image, (chopstick_x, chopstick_y))

    # 라면 이미지 그리기
    ramen_image = get_ramen_image()
    screen.blit(ramen_image, (SCREEN_WIDTH // 2 - ramen_image.get_width() // 2, SCREEN_HEIGHT // 2))

    # 타이머 그리기
    if start_time:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        timer_text = SMALL_FONT.render(f"{elapsed_time:.2f}초", True, BLACK)
        screen.blit(timer_text, (20, 20))

    # 라면 진행 상황 그리기
    progress_text = SMALL_FONT.render(f"라면 먹기: {ramen_clicks}/{ramen_clicks_needed}", True, BLACK)
    screen.blit(progress_text, (SCREEN_WIDTH // 2 - progress_text.get_width() // 2, SCREEN_HEIGHT // 2 - 150))

# 게임 종료 화면 그리기
def draw_finished():
    screen.fill(WHITE)

    # 축하 메시지 그리기
    congrats_text = FONT.render("축하합니다!", True, BLACK)
    screen.blit(congrats_text, (SCREEN_WIDTH // 2 - congrats_text.get_width() // 2, 100))

    # 걸린 시간 그리기
    time_text = SMALL_FONT.render(f"걸린 시간: {elapsed_time:.2f}초", True, BLACK)
    screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, 200))

    # 빈 그릇 이미지 그리기
    ramen_image = ramen_images[2]  # 빈 그릇 이미지
    screen.blit(ramen_image, (SCREEN_WIDTH // 2 - ramen_image.get_width() // 2, SCREEN_HEIGHT // 2))

    # 다시하기 버튼 그리기
    pygame.draw.rect(screen, RED, retry_button)
    retry_text = SMALL_FONT.render("다시하기", True, WHITE)
    screen.blit(retry_text, (retry_button.x + retry_button.width // 2 - retry_text.get_width() // 2,
                             retry_button.y + retry_button.height // 2 - retry_text.get_height() // 2))

# 라면 상태를 업데이트하는 함수
def get_ramen_image():
    progress = ramen_clicks / ramen_clicks_needed
    if progress < 0.5:
        return pygame.transform.scale(ramen_images[0], (300, 300))  # 가득 찬 라면 크기 축소
    elif progress < 1.0:
        return pygame.transform.scale(ramen_images[1], (300, 300))  # 반쯤 먹은 라면 크기 축소
    else:
        return pygame.transform.scale(ramen_images[2], (300, 300))  # 빈 그릇 크기 축소

# 이미지 로드 확인
for i, img in enumerate(ramen_images):
    if img is None:
        print(f"Error: ramen_images[{i}] failed to load.")

# 젓가락 움직임 업데이트 함수 수정
def update_chopstick():
    global chopstick_x, chopstick_y
    chopstick_x += random.choice([-10, 10])  # 좌우로 랜덤 이동
    chopstick_y += random.choice([-5, 5])    # 상하로 랜덤 이동

    # 젓가락이 라면을 가리지 않도록 위치 제한
    ramen_top = SCREEN_HEIGHT // 2 - 100
    ramen_bottom = SCREEN_HEIGHT // 2 + 100
    chopstick_y = max(chopstick_y, ramen_top - 50)  # 라면 위로 제한
    chopstick_y = min(chopstick_y, ramen_top - 10)  # 라면 바로 위까지만 이동 가능

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 마우스 왼쪽 버튼
            if game_state == "main":
                game_state = "playing"
                reset_game()

            elif game_state == "finished" and retry_button.collidepoint(event.pos):
                game_state = "main"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 스페이스 키
            if game_state == "playing":
                ramen_clicks += 1
                update_chopstick()  # 젓가락 움직임 업데이트
                if ramen_clicks >= ramen_clicks_needed:
                    game_state = "finished"
                    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    # 적절한 화면 그리기
    if game_state == "main":
        draw_main_menu()
    elif game_state == "playing":
        draw_game()
    elif game_state == "finished":
        draw_finished()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()