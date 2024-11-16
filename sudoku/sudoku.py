import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 540
CELL_SIZE = WINDOW_SIZE // 9
ANIMATION_SPEED = 0.0000001  # Seconds between animation frames

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sudoku Solver Animation")

# Example Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def draw_grid():
    """Draw the Sudoku grid"""
    for i in range(10):
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), line_width)

def draw_numbers():
    """Draw numbers on the board"""
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                number = font.render(str(board[i][j]), True, BLACK)
                x = j * CELL_SIZE + (CELL_SIZE - number.get_width()) // 2
                y = i * CELL_SIZE + (CELL_SIZE - number.get_height()) // 2
                screen.blit(number, (x, y))

def animate_number(row, col, final_num):
    """Animate the number selection process"""
    font = pygame.font.Font(None, 36)
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    
    # Make sure the final number is last
    numbers.remove(final_num)
    numbers.append(final_num)
    
    for num in numbers:
        screen.fill(WHITE)
        draw_grid()
        draw_numbers()
        
        # Draw the animated number in red, except the final number in green
        color = GREEN if num == final_num else RED
        number = font.render(str(num), True, color)
        x = col * CELL_SIZE + (CELL_SIZE - number.get_width()) // 2
        y = row * CELL_SIZE + (CELL_SIZE - number.get_height()) // 2
        screen.blit(number, (x, y))
        
        pygame.display.flip()
        time.sleep(ANIMATION_SPEED)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
    
    board[row][col] = final_num
    return True

def is_valid(num, pos):
    """Check if the number is valid in the given position"""
    # Check row
    for j in range(9):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    
    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def find_empty():
    """Find an empty cell in the board"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve():
    """Solve the Sudoku puzzle using backtracking with animation"""
    empty = find_empty()
    if not empty:
        return True
    
    row, col = empty
    for num in range(1, 10):
        if is_valid(num, (row, col)):
            if not animate_number(row, col, num):
                return False
            
            if solve():
                return True
            
            board[row][col] = 0
            screen.fill(WHITE)
            draw_grid()
            draw_numbers()
            pygame.display.flip()
            time.sleep(ANIMATION_SPEED)
    
    return False

def main():
    """Main function to run the animated Sudoku solver"""
    running = True
    solved = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        if not solved:
            screen.fill(WHITE)
            draw_grid()
            draw_numbers()
            pygame.display.flip()
            
            # Start solving after a brief pause
            time.sleep(1)
            solved = solve()
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()