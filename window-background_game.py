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