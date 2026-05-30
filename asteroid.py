from math import dist

import pygame, random, math, os

pygame.init()
width, height = 800,600
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Mini asteroids Expandido")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,32)

x_player, y_player = width // 2, height // 2
player_speed = 5
player_lives = 3

bullets = []
bullet_speed = 8
last_shot = 0
shot_cooldown = 300

STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU

spawn_timer = 0
spawn_interval = 2000

asteroids = []
asteroid_types = [
    {"size": 20, "speed": 3, "points": 15,"color":(200,200,255)},
    {"size": 35, "speed": 2, "points": 10,"color":(200,200,255)},
    {"size": 50, "speed": 1.5, "points": 5,"color":(200,200,255)}
]
def spawn_asteroid():
    t = random.choice(asteroid_types)
    x = random.randint(width,height)
    y = random.choice([-50,height+50])

    angle = math.atan2(height//2 - y, width//2 - x)
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
    x = random.randint(50, width-50)
    y = random.randint(50, height-50)
    powerups.append([x, y, "shield"])
def reset_game():
    pass
    global player_pos, player_lives, score, asteroids, bullets, powerups
    player_pos = [width//2,height//2]
    player_lives = 3
    score = 0
    asteroids = []
    bullets = []
    powerups = []





while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.KEYDOWN:
                if game_state == STATE_MENU and event.key ==pygame.K_RETURN:
                        game_state = STATE_GAME
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:

                game_state = STATE_GAME

    if game_state == STATE_GAME:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x_player += player_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x_player += player_speed
        if keys[pygame.k_w] or keys[pygame.K_UP]:
            x_player -= player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            x_player += player_speed

        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - last_shot > shot_cooldown:
            lastshot = pygame.time.get_ticks()

            mouse_x,mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - x_player
            dy = mouse_y - y_player
            dist = math.hypot(dx,dy)

            vx = dx / dist#-------Vetores-------
            vy = dy / dist

            bullets.append([x_player,y_player,vx * bullet_speed,vy * bullet_speed])

        for b in bullets:
            b[0] += [2] #x_player + vetor
            b[1] += b[3]

        bullets = [b for b in bullets if 0 < b[0] < width and 0 < b[1] < height]

        for a in asteroids:
            a[0] += math.cos(a[4]) * a[2]
            a[1] += math.sin(a[4])  * a[2]
        spawn_timer += dt
        if spawn_timer > spawn_interval > 1000:
            spawn_interval -=50

        new_asteroids = []
        for a in asteroids:
            ax, ay, sp ,sz, ang, pts, color = a
            hit = False
        for b in bullets:
            if math.hypot(ax -b[0], ay -b[1]) < sz:
                bullets.remove(b)
                hit = True
                break
            if hit:
                score += pts
                spawn_asteroid()
            else:
                 new_asteroids.append(a)
        asteroids = new_asteroids



    win.fill((0, 0, 20))
    if game_state == STATE_MENU:
        pygame.draw.circle(win, (0, 255, 0), (x_player,y_player),20)
        title = font.render("MINI ASTEROIDS",True, (255, 255,255))
        prompt = font.render("Preciona ENTER para começar", True, (200,200,200))
        #high_score = font.render(f"Highscore: ")

        win.blit(title, (width // 2 - 100, height // 2 - 40))
        win.blit(prompt,(width // 2 - 180, height // 2))

    elif game_state == STATE_GAME:
        pygame.draw.circle(win, (0, 255,0),(x_player,y_player), 20)
        for bullet in bullets:
            pygame.draw.circle(win, (255,255,0),(int(bullet[0],int(bullets[1])),5))

        hud = font.render(f"score:{score} Vidas: {player_lives}", True, (255, 255, 255))
        win.blit(hud, (10, 10))

    pygame.display.flip()

pygame.quit()

