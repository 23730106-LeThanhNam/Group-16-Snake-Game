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
