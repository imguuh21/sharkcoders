import pygame, random, math, os

pygame.init()
W, H = 800,600
win = pygame.display.set_mode((W, H))

pygame.display.set_caption("Mini asteroids Expandido")
clock = pygame.time.Clock()
font = pygame.SysFont(None,32)

player_pos = [W//2,W//2]
player_speed = 5
player_lives = 3

bullets = []

lastshot = 0
shotcooldown = 0

STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU

asteroids = []
asteroid_types = [
    {"size": 20, "speed": 3, "points": 15,}

]
def spawn_asteroid():
    t = random.choice(asteroid_types)
    x = random.randint(W,H)
    y = random.choice([-50,H+50])

    angle = math.atan2(H//2 - y, W//2 - x)
    asteroids.append([x, y, t["speed"],t["size"],angle, t["points"],t["color"]])
HIGHSCORE_FILE = "highscore.txt"
if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE,"r") as f:
        highscore = int(f.read())
else:
    highscore = 0

running = True
spawn_timer = 0
spawn_interval = 3000
last_powerup = 0
powerup_interval = 10000
powerup_active = 1



def spawn_powerups():
    x = random.randint(50, W-50)
    y = random.randint(50, H-50)
    powerups.append([x, y, "shield"])
def reset_game():
    pass
    global player_pos, player_lives, score, asteroids, bullets, powerups
    player_pos = [W//2,H//2]
    player_lives = 3
    score = 0
    asteroids = []
    bullets = []
    powerups = []



for _ in range(6):
    spawn_asteroid()



while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.KEYDOWN:
                reset_game()
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME


    if game_state == STATE_GAME:
        pygame.draw.circle(win, (0, 255, 0), player_pos,20)
        if powerup_active:
            pygame.draw.circle(win, (0, 150, 255), player_pos,30, 2)

        for b in bullets:
            pygame.draw.circle(win, (255, 255, 0),(int(b[0]),int(b[1])),5)

        for a in asteroids:
            pygame.draw.circle(win, a[6],(int(a[0]), int(a[1])),a[3])

        for p in powerups:
            pygame.draw.rect(win, [0, 200, 255], (p[0] - 10, p[1] - 10, 20, 20))


        hud = font.render(f"score:{score} Vidas: {player_lives}", True, (255, 255, 255))
        win.blit(hud, (10, 10))

