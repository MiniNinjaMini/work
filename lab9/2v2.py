import pygame
import random
import time

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width,height))

# Variables and their initialization
score = 0
lvl = 1
fruit_eaten = False

#fruits list
fruits = {
    "apple": {"color": (0, 255, 0), "points": 10, "chance": 0.7},
    "banana": {"color": (255, 255, 0), "points": 20, "chance": 0.2},
    "cherry": {"color": (255, 0, 0), "points": 50, "chance": 0.1},
}
fr_x = random.randrange(1, width//10)*10
fr_y = random.randrange(1,height//10)*10
fruit_data = [fr_x, fr_y, "apple"]
# Track fruit appearance time
fruit_appear_time = time.time()

#fruit randomizer
def choose_fruit():
    rand = random.random()
    cumulative_chance = 0
    for fruit, data in fruits.items():
        cumulative_chance += data["chance"]
        if rand < cumulative_chance:
            return fruit
    return "apple"  # На случай, если все шансы не сработали.


head_square = [100, 100]

squares = [
    [30, 100],
    [40, 100],
    [50, 100],
    [60, 100],
    [70, 100],
    [80, 100],
    [90, 100],
    [100, 100]
]

direction = "right"
next_dir = "right"

done = False



def game_over(font, size, color):
    global done
    g_o_font = pygame.font.SysFont(font, size)
    g_o_surface = g_o_font.render(f"Game Over, your score: {score}", True, color)
    g_o_rect = g_o_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
    screen.blit(g_o_surface, g_o_rect)

    g_o_surface = g_o_font.render(f"           your lvl: {lvl}", True, color)
    g_o_rect = g_o_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(g_o_surface, g_o_rect)

    pygame.display.update()
    pygame.time.delay(4000)
    pygame.quit()

# Function to reduce delay as level increases
def get_delay(level, max_delay=200, min_delay=100, max_level=11):
    return max_delay - (level - 1) * (max_delay - min_delay) / (max_level - 1)

# Function to generate fruit
def generate_fruit():
    while True:
        fr_x = random.randrange(1, width // 10) * 10
        fr_y = random.randrange(1, height // 10) * 10
        if [fr_x, fr_y] not in squares:
            fruit_type = choose_fruit()  # Выбираем тип фрукта
            return [fr_x, fr_y, fruit_type]

# Start of gameplay loop
while not done:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_dir = "down"
            if event.key == pygame.K_UP:
                next_dir = "up"
            if event.key == pygame.K_LEFT:
                next_dir = "left"
            if event.key == pygame.K_RIGHT:
                next_dir = "right"

    for square in squares[:-1]:
        if head_square[0] == square[0] and head_square[1] == square[1]:
            game_over("times new roman", 45, (128, 128, 128))

    # Movement logic
    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"

    if direction == "right":
        if head_square[0] + 10 == width:
            game_over("times new roman", 45, (128, 128, 128))
        else:
            head_square[0] += 10
    if direction == "left":
        if head_square[0] - 10 == -10:
            game_over("times new roman", 45, (128, 128, 128))
        else:
            head_square[0] -= 10
    if direction == "up":
        if head_square[1] - 10 == -10:
            game_over("times new roman", 45, (128, 128, 128))
        else:
            head_square[1] -= 10
    if direction == "down":
        if head_square[1] + 10 == height:
            game_over("times new roman", 45, (128, 128, 128))
        else:
            head_square[1] += 10

    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)
    squares.pop(0)

    # Check if fruit is eaten
    if head_square[0] == fruit_data[0] and head_square[1] == fruit_data[1]:
        fruit_eaten = True
        score += fruits[fruit_data[2]]["points"]
        lvl = score // 30 + 1
        fruit_appear_time = time.time()  # Reset fruit timer

    # If fruit has been on screen too long, regenerate it
    if time.time() - fruit_appear_time > 10:  # Fruit disappears after 5 seconds
        fruit_eaten = True
        fruit_appear_time = time.time()  # Reset timer

    # Update fruit if eaten
    if fruit_eaten:
        fruit_data = generate_fruit()
        fruit_eaten = False

    # Drawing section
    screen.fill((0, 0, 0))

    score_font = pygame.font.SysFont("times new roman", 20)
    score_surface = score_font.render("Score: " + str(score), True, (128, 128, 128))
    score_rect = score_surface.get_rect()
    lvl_surface = score_font.render("Level: " + str(lvl), True, (128, 128, 128))
    lvl_rect = lvl_surface.get_rect(center=(32, 50))
    fruit_time_surf = score_font.render("the fruit will disappear in: " + str(abs(10-time.time() + fruit_appear_time)), True, (128, 128, 128))
    fruit_time_rect = fruit_time_surf.get_rect(center=(400, 50))

    screen.blit(score_surface, score_rect)
    screen.blit(lvl_surface, lvl_rect)
    screen.blit(fruit_time_surf, fruit_time_rect)

    # Draw fruit if it hasn't been eaten
    if not fruit_eaten:
        color=fruits[fruit_data[2]]["color"]
        pygame.draw.circle(screen, color, (fruit_data[0] + 5, fruit_data[1] + 5), 5)

    # Draw snake
    for el in squares:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(el[0], el[1], 10, 10))

    zaderzhka = int(get_delay(lvl))
    pygame.display.flip()
    pygame.time.delay(zaderzhka)

pygame.quit()
