import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up fonts
font = pygame.font.SysFont("comicsans", 80)

# Initialize board
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Function to draw the grid lines
def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X and O
def draw_markers():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20), 
                                 ((col + 1) * SQUARE_SIZE - 20, (row + 1) * SQUARE_SIZE - 20), 5)
                pygame.draw.line(screen, BLACK, ((col + 1) * SQUARE_SIZE - 20, row * SQUARE_SIZE + 20), 
                                 (col * SQUARE_SIZE + 20, (row + 1) * SQUARE_SIZE - 20), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), 
                                                    int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), 30, 5)
# Function to check for a win
def check_win(player):
    # Check rows and columns
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)):
            return True
        if all(board[j][i] == player for j in range(BOARD_ROWS)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_ROWS)):
        return True
    if all(board[i][BOARD_COLS - i - 1] == player for i in range(BOARD_ROWS)):
        return True
    return False

# Function to check for a tie
def check_tie():
    return all(board[i][j] != ' ' for i in range(BOARD_ROWS) for j in range(BOARD_COLS))

# Function to draw the result
def draw_result(result):
    if result == 'X':
        text = font.render("X wins!", True, BLACK)
    elif result == 'O':
        text = font.render("O wins!", True, BLACK)
    elif result == 'Tie':
        text = font.render("It's a tie!", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)

# Main game loop
def main():
    turn_count = 0
    player = 'X'
    result = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and result is None:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE

                if board[mouseY][mouseX] == ' ':
                    board[mouseY][mouseX] = player
                    turn_count += 1

                    if check_win(player):
                        result = player
                    elif check_tie():
                        result = 'Tie'
                    else:
                        player = 'O' if player == 'X' else 'X'

        screen.fill(WHITE)
        draw_grid()
        draw_markers()

        if result:
            draw_result(result)
            main()

        pygame.display.update()

if __name__ == "__main__":
    main()
