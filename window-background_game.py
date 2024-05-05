import pygame
import random
 
# Khởi tạo pygame
pygame.init()
 
# Kích thước cửa sổ
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
 
# Kích thước ô
CELL_SIZE = 20
 
# Khởi tạo màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
# Hình ảnh
background_img = pygame.transform.scale(pygame.image.load('background.png').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
food_img = pygame.transform.scale(pygame.image.load('food.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
tnt_img = pygame.transform.scale(pygame.image.load('tnt.png').convert_alpha(), (CELL_SIZE, CELL_SIZE))
food_img.set_colorkey((0, 0, 0))  # Đặt màu đen là màu trong suốt cho food_img
 
# Font
try:
    font = pygame.font.Font('arial.ttf', 36)
except FileNotFoundError:
    font = pygame.font.SysFont(None, 36)

# Snake colors
BODY_COLOR = (43, 196, 0)
EYE_COLOR = (0, 0, 0)
HEAD_COLOR = (36, 232, 83)

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
        screen.blit(background_img, (0, 0))
 
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
            food = [
                random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE), 
                random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE)
            ]
            snake.append(snake[-1])  # Thêm một đốt thêm vào đuôi
 
        # Kiểm tra va chạm với TNT
        if head == tnt:
            running = False
 
        # Cập nhật vị trí TNT
        if random.randint(0, 99) < 5:  # Cập nhật vị trí TNT với xác suất 5%
            tnt = [
                random.randint(0, (SCREEN_WIDTH-CELL_SIZE)//CELL_SIZE), 
                random.randint(0, (SCREEN_HEIGHT-CELL_SIZE)//CELL_SIZE)
            ]
 
        snake.insert(0, head)
        if head != food:
            snake.pop()
 
        draw_snake(snake, direction)
        draw_food(food)
        draw_tnt(tnt)
 
        # Hiển thị điểm số
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
 
        pygame.display.flip()
 
        clock.tick(10)
 
    return show_game_over(score)
