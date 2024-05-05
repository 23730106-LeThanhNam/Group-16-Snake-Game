
# Khởi tạo vị trí và tốc độ của con rắn
lead_x = width / 2
lead_y = height / 2
lead_x_change = 0
lead_y_change = 0

snake_list = []
snake_length = 1

# Vị trí thức ăn ban đầu
rand_food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
rand_food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

def show_game_over(score):
    game_over_text = font.render('Game Over', True, (255, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

    play_again_text = font.render('Chơi lại', True, (0, 0, 0))
    screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    
    menu_text = font.render('Quay về menu', True, (0, 0, 0))
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

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
                
while not game_exit:
    while game_over == True:
        game_display.fill(white)
        message_to_screen("Game over! Nhấn C hoặc Q để thoát hoặc nhấn R để chơi lại.", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_c:
                    game_exit = True
                    game_over = False
                elif event.key == pygame.K_r:
                    gameLoop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

                

    # Kiểm tra xem con rắn có chạm vào tường không
    if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
        game_over = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    game_display.fill(white)
    pygame.draw.rect(game_display, red, [rand_food_x, rand_food_y, block_size, block_size])

    snake_head = []
    snake_head.append(lead_x)
    snake_head.append(lead_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for each_segment in snake_list[:-1]:
        if each_segment == snake_head:
            game_over = True

    snake(block_size, snake_list)
    pygame.display.update()

    # Kiểm tra xem con rắn có ăn thức ăn không
    if lead_x == rand_food_x and lead_y == rand_food_y:
        rand_food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        rand_food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        snake_length += 1

    clock.tick(fps)

pygame.quit()
quit()
