import pygame
import random
import sys
import turtle
pygame.init()
WIDTH = 800
HEIGHT = 600
Purple = (225, 0, 250)
Orange = (255,100,0)
Yellow = (255, 255, 0)
Background_color = (0,0,0)
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]
enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]
Speed = 10
Score = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 35)
def set_level(Score, Speed):
	#if Score < 20:
	#	Speed = 5
	#elif Score < 40:
	#	Speed = 8
	#elif Score < 80:
	#	Speed = 12
	#elif Score < 120: 
	#	Speed = 15
	#else:
	#	Speed = 18
	#return Speed
	Speed = Score/5 + 5
	return Speed
def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0, WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])
def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, Orange, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
def update_enemy_positions(enemy_list, Score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += Speed
		else: 
			enemy_list.pop(idx)
			Score += 1
	return Score
def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False
def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]
	e_x = enemy_pos[0]
	e_y = enemy_pos[1]
	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >=e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False		
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x = player_pos[0]
			y = player_pos[1]
			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size
			elif event.key == pygame.K_UP:
				y -= player_size
			elif event.key == pygame.K_DOWN:
				y += player_size
			player_pos = [x,y]
	if player_pos[0] > 750 or player_pos[0] < 0 or player_pos[1] > 550 or player_pos[1] < 0:
		game_over = True
	screen.fill((Background_color))
	drop_enemies(enemy_list)
	Score = update_enemy_positions(enemy_list, Score)
	Speed = set_level(Score, Speed)
	text = "Score:" + str(Score)
	label = myFont.render(text,1, Yellow)
	screen.blit(label, (WIDTH-200, HEIGHT-40))
	if collision_check(enemy_list, player_pos):
		game_over = True
		break
	draw_enemies(enemy_list)
	pygame.draw.rect(screen, Purple, (player_pos[0], player_pos[1], player_size, player_size))
	clock.tick(30)
	pygame.display.update()