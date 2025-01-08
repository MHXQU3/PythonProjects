import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dims
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (0, 255, 255) #Called white for dichotomy reasons but colour code is Cyan
BLACK = (0, 0, 0)

# Paddle dims
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 5

# Ball properties
BALL_SIZE = 15
initial_ball_speed = 4

# Player paddles
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = initial_ball_speed, initial_ball_speed

# Scores and series
score1, score2 = 0, 0
games_won_1, games_won_2 = 0, 0
MAX_GAMES = 1 # ----> Change this if you want to change no of games series
# Experimenting with inputs (decided not worth it, maybe add in future)
# MAX_GAMES = input("How many games would you like to be played: ")
# MAX_GAMES = int(MAX_GAMES)

# Font
font = pygame.font.Font(None, 36)

# Game mode and difficulty
game_mode = None  # "AI" or "2P"
ai_difficulty = None  # "Easy", "Medium", "Hard"

# Sounds
paddle_hit_sound = pygame.mixer.Sound(r"paddle_hit.mp3")
score_sound = pygame.mixer.Sound(r"score.mp3")

# Functions
def draw():
    """Draw all elements on the screen."""
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    game_series_text = font.render(f"Games: {games_won_1} - {games_won_2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))
    screen.blit(game_series_text, (WIDTH // 2 - game_series_text.get_width() // 2, 50))
    pygame.display.flip()

def move_paddles():
    # Player 1 paddle movement using W and S keys 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += paddle_speed

    if game_mode == "2P":
        # Player 2 paddle movement using Up and Down arrow keys
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += paddle_speed

def ai_move_paddle():
    """AI-controlled paddle with difficulty settings."""
    if ai_difficulty == "Easy":
        speed = 3  # Slow paddle
        reaction_chance = 0.85  # 85% chance to react
        buffer = 20  # Good chance for mistakes
    elif ai_difficulty == "Medium":
        speed = 5  # Medium paddle
        reaction_chance = 0.95  # 95% chance to react
        buffer = 10  # Small amount of mistakes
    elif ai_difficulty == "Hard":
        speed = 7  # Faster paddle
        reaction_chance = 1.0  # Always reacts
        buffer = 5  # Almost no mistakes
    if random.random() < reaction_chance:
        if paddle2.centery < ball.centery - buffer:
            paddle2.y += min(speed, ball.centery - paddle2.centery)
        elif paddle2.centery > ball.centery + buffer:
            paddle2.y -= min(speed, paddle2.centery - ball.centery)
    paddle2.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

def reset_ball():
    """Reset the ball to the center of the screen."""
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = initial_ball_speed if random.choice([True, False]) else -initial_ball_speed
    ball_speed_y = random.choice([-initial_ball_speed, initial_ball_speed])

def move_ball():
    """Move the ball and handle collisions."""
    global ball_speed_x, ball_speed_y, score1, score2
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        paddle_hit_sound.play()
        ball_speed_x *= -1.1  # Increase speed slightly with each hit
        offset = (ball.centery - (paddle1.centery if ball.colliderect(paddle1) else paddle2.centery)) / (PADDLE_HEIGHT // 2)
        ball_speed_y += offset

    # Score points
    if ball.left <= 0:
        score_sound.play()
        score2 += 1
        reset_ball()
    if ball.right >= WIDTH:
        score_sound.play()
        score1 += 1
        reset_ball()

def check_game_over():
    """Check if a player has won the series."""
    global games_won_1, games_won_2, score1, score2

    if score1 >= 7:
        games_won_1 += 1
        reset_ball()
    elif score2 >= 7:
        games_won_2 += 1
        reset_ball()

    # Check if someone has won the series
    if games_won_1 >= MAX_GAMES or games_won_2 >= MAX_GAMES:
        return True  # Series over
    return False  # Game continues

def display_winner():
    """Display the winner of the series."""
    global games_won_1, games_won_2, score1, score2, game_mode, ai_difficulty

    # Capture the current final scores before resetting them
    final_score_player_1 = score1
    final_score_player_2 = score2
    
    # Determine the winner message based on game mode
    if game_mode == "AI":
        if games_won_2 >= MAX_GAMES:  # CPU wins
            if ai_difficulty == "Easy":
                winner = "CPU (Easy) wins the series!"
            elif ai_difficulty == "Medium":
                winner = "CPU (Medium) wins the series!"
            elif ai_difficulty == "Hard":
                winner = "CPU (Hard) wins the series!"
        elif games_won_1 >= MAX_GAMES:  # Player 1 wins
            winner = "Player 1 wins the series!"
    else:  # Two-Player mode
        if games_won_1 >= MAX_GAMES:
            winner = "Player 1 wins the series!"
        elif games_won_2 >= MAX_GAMES:
            winner = "Player 2 wins the series!"
    
    # Display winner text on screen
    screen.fill(BLACK)
    winner_text = font.render(winner, True, WHITE)
    screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - 50))
    
    # Display the final score before resetting
    final_score_text = font.render(f"Final Score: {final_score_player_1} - {final_score_player_2}", True, WHITE)
    screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 10))
    
    # Ask if the player wants to play again
    play_again_text = font.render("Press 'Y' to play again or 'N' to quit", True, WHITE)
    screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()
    
    # Wait for player input to decide whether to play again
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # 'Y' for Yes
                    games_won_1, games_won_2 = 0, 0  # Reset series scores
                    score1, score2 = 0, 0  # Reset final scores
                    reset_ball()  # Reset ball position for new game
                    waiting_for_input = False  # Exit the loop and restart the game
                elif event.key == pygame.K_n:  # 'N' for No
                    pygame.quit()
                    sys.exit()  # Exit the game

def select_mode():
    """Let the player select game mode and AI difficulty."""
    global game_mode, ai_difficulty
    screen.fill(BLACK)

    # Display the mode and difficulty options
    mode_text = font.render("Press 'E' for Easy, 'M' for Medium, 'H' for Hard", True, WHITE)
    two_player_text = font.render("Press '2' for 2-Player", True, WHITE)
    controls_text = font.render("Player 1: 'W' (Up), 'S' (Down) | Player 2: Up/Down Arrows", True, WHITE)

    # Blit the text to the screen
    screen.blit(mode_text, (WIDTH // 2 - mode_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(two_player_text, (WIDTH // 2 - two_player_text.get_width() // 2, HEIGHT // 2 + 50))
    screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 2 + 100))
    pygame.display.flip()

    game_mode = None  # Default is no mode
    ai_difficulty = None  # Default is No AI (Assumming 2P)

    while game_mode is None:  # Wait for the mode selection (either difficulty or 2P)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Easy diff
                    game_mode = "AI"
                    ai_difficulty = "Easy"
                    print("AI difficulty set to Easy.")
                elif event.key == pygame.K_m:  # Medium diff
                    game_mode = "AI"
                    ai_difficulty = "Medium"
                    print("AI difficulty set to Medium.")
                elif event.key == pygame.K_h:  # Hard diff
                    game_mode = "AI"
                    ai_difficulty = "Hard"
                    print("AI difficulty set to Hard.")
                elif event.key == pygame.K_2:  # 2P mode
                    game_mode = "2P"
                    print("Two-Player mode selected.")

# Main game loop
select_mode()
clock = pygame.time.Clock()
reset_ball()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_paddles()
    if game_mode == "AI":
        ai_move_paddle()
    move_ball()

    if check_game_over():
        display_winner()  # Show the winner screen
        pygame.time.wait(10000)  # Wait 10 seconds before resetting
        games_won_1, games_won_2 = 0, 0  # Reset series
        reset_ball()  # Reset ball for the new series


    draw()
    clock.tick(60)
