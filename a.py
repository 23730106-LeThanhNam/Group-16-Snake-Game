import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 580

# Kích thước ô
CELL_SIZE = 25

# Khởi tạo màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Hình ảnh

background_img_level3 = pygame.transform.scale(pygame.image.load('Graphics/hard_level.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_img_level2 = pygame.transform.scale(pygame.image.load('Graphics/medium_level.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_img_level1 = pygame.transform.scale(pygame.image.load('Graphics/easy_level.png').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
food_img = pygame.transform.scale(pygame.image.load('Graphics/food.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
tnt_img = pygame.transform.scale(pygame.image.load('Graphics/tnt.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
food_img.set_colorkey((0, 0, 0))  # Đặt màu đen là màu trong suốt cho food_img

# Font
try:
    font = pygame.font.Font('Font/arial.ttf', 36)
except FileNotFoundError:
    font = pygame.font.SysFont(None, 36)

# Hàm vẽ con rắn
BODY_COLOR = (43, 196, 0)
EYE_COLOR = (0, 0, 0)
HEAD_COLOR = (36, 232, 83)

def draw_snake(snake, direction):
    for i, segment in enumerate(snake):
        segment_rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if i == 0:  # Đầu con rắn
            pygame.draw.rect(screen, HEAD_COLOR, segment_rect)
            eye_left = pygame.Rect(segment[0] * CELL_SIZE + CELL_SIZE * 0.25, segment[1] * CELL_SIZE + CELL_SIZE * 0.3, CELL_SIZE * 0.2, CELL_SIZE * 0.2)
            pygame.draw.circle(screen, EYE_COLOR, eye_left.center, int(CELL_SIZE * 0.1))
            eye_right = pygame.Rect(segment[0] * CELL_SIZE + CELL_SIZE * 0.55, segment[1] * CELL_SIZE + CELL_SIZE * 0.3, CELL_SIZE * 0.2, CELL_SIZE * 0.2)
            pygame.draw.circle(screen, EYE_COLOR, eye_right.center, int(CELL_SIZE * 0.1))
        else:  # Các phần còn lại
            pygame.draw.rect(screen, BODY_COLOR, segment_rect)

# Hàm vẽ thức ăn
def draw_food(food):
    screen.blit(food_img, (food[0] * CELL_SIZE, food[1] * CELL_SIZE))

# Hàm vẽ TNT
def draw_tnt(tnt):
    screen.blit(tnt_img, (tnt[0] * CELL_SIZE, tnt[1] * CELL_SIZE))

# Hàm hiển thị Game Over
def show_game_over(score):
    game_over_text = font.render('Game Over', True, (255, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

    play_again_text = font.render('Chơi lại', True, (0, 0, 0))
    screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    
    menu_text = font.render('Quay về menu', True, (0, 0, 0))
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
    pygame.mixer.Sound('Sound/game_over.wav').play()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if SCREEN_WIDTH // 2 - play_again_text.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + play_again_text.get_width() // 2 and \
                   SCREEN_HEIGHT // 2 + 50 <= y <= SCREEN_HEIGHT // 2 + 50 + play_again_text.get_height():
                    return 'play_again'
                elif SCREEN_WIDTH // 2 - menu_text.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + menu_text.get_width() // 2 and \
                     SCREEN_HEIGHT // 2 + 100 <= y <= SCREEN_HEIGHT // 2 + 100 + menu_text.get_height():
                    return 'menu'

# Hàm chính
def main():
    score = 0  # Khởi tạo biến score
    snake = [[5, 5], [4, 5], [3, 5]]
    direction = 'RIGHT'
    food = [random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE), 
            random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE)]
    tnt = [random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE), 
           random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE)]
    running = True
    while running:
        if score >= 0 and score <= 3:
            screen.blit(background_img_level1, (0, 0))
            clock.tick(10)
        elif score > 3 and score <= 5:
            screen.blit(background_img_level2, (0, 0))
            clock.tick(15)
        else:
            screen.blit(background_img_level3, (0, 0))
            clock.tick(20)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
        
        # Di chuyển con rắn
        head = list(snake[0])
        if direction == 'UP':
            head[1] -= 1
        elif direction == 'DOWN':
            head[1] += 1
        elif direction == 'LEFT':
            head[0] -= 1
        elif direction == 'RIGHT':
            head[0] += 1
        
        # Kiểm tra va chạm với tường
        if head[0] < 0 or head[0] >= SCREEN_WIDTH//CELL_SIZE or head[1] < 0 or head[1] >= SCREEN_HEIGHT//CELL_SIZE:
            running = False
        
        # Kiểm tra va chạm với bản thân
        if head in snake:
            running = False

        # Kiểm tra ăn thức ăn
        if head == food:
            score += 1
            food = [random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE), 
                    random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE)]
            snake.append(snake[-1])  # Thêm một đốt thêm vào đuôi
            pygame.mixer.Sound('Sound/crunch.wav').play()
        
        # Kiểm tra va chạm với TNT
        if head == tnt:
            running = False
        
        # Cập nhật vị trí TNT
        if random.randint(0, 99) < 5:  # Cập nhật vị trí TNT với xác suất 5%
            tnt = [random.randint(0, (SCREEN_WIDTH-CELL_SIZE - 20)//CELL_SIZE), 
                   random.randint(0, (SCREEN_HEIGHT-CELL_SIZE - 20)//CELL_SIZE)]
        
        snake.insert(0, head)
        if head != food:
            snake.pop()
        
        draw_snake(snake, direction)
        draw_food(food)
        draw_tnt(tnt)
        
        # Hiển thị điểm số
        score_surface = font.render(f'Score: {score}', True, (56,74,12))
        screen.blit(score_surface,(10, 10))
        pygame.display.flip()
        
        

    return show_game_over(score)

# Hàm menu
def menu():
    while True:
        screen.blit(background_img_level1, (0, 0))

        start_text = font.render('Bắt đầu chơi', True, (0, 0, 0))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if SCREEN_WIDTH // 2 - start_text.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + start_text.get_width() // 2 and \
                   SCREEN_HEIGHT // 2 - 50 <= y <= SCREEN_HEIGHT // 2 - 50 + start_text.get_height():
                    return 'play'

# Hàm chính của chương trình
if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == 'play':
            result = main()
            while result == 'play_again':
                result = main()
