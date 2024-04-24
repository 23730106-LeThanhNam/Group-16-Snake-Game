# Hàm vẽ thức ăn
def draw_food(food):
    screen.blit(food_img, (food[0] * CELL_SIZE, food[1] * CELL_SIZE))
 
# Hàm vẽ TNT
def draw_tnt(tnt):
    screen.blit(tnt_img, (tnt[0] * CELL_SIZE, tnt[1] * CELL_SIZE))