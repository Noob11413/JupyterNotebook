import pygame
import time
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
black = (0, 0, 0)

grid_size = 5
cell_width = screen_width // grid_size
cell_height = screen_height // grid_size

# Sudoku grid representation (1-5, 0 means empty cell)
sudoku_grid = [
    [1, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 0, 0, 4, 0],
    [0, 0, 0, 0, 5]
]

def is_valid_move(grid, row, col, num):
    # Check if 'num' is a valid move in the Sudoku grid at the given position (row, col)
    # Check the row
    if num in grid[row]:
        return False
    
    # Check the column
    if num in [grid[i][col] for i in range(grid_size)]:
        return False
    
    return True


def solve_sudoku(grid):
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == 0:
                for num in range(1, grid_size + 1):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        yield grid  #current state of the grid
                        yield from solve_sudoku(grid)  # Recursively yield the next steps
                        grid[row][col] = 0  # If placing 'num' doesn't lead to a solution, backtrack

def draw_sudoku_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            num = sudoku_grid[i][j]
            if num != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(num), True, black)
                x = j * cell_width + (cell_width // 2) - (text.get_width() // 1)
                y = i * cell_height + (cell_height // 2) - (text.get_height() // 1)
                screen.blit(text, (x, y))

run = True
solver = solve_sudoku(sudoku_grid)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    try:
        sudoku_grid = next(solver)  # Get the next step in solving
    except StopIteration:
        print("Sudoku solved!")
        

    screen.fill(white)
    draw_sudoku_grid()

    # Draw the grid
    for x in range(0, screen_width, cell_width):
        pygame.draw.line(screen, black, (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_height):
        pygame.draw.line(screen, black, (0, y), (screen_width, y))

    pygame.display.update()
    time.sleep(0.10)  # Control the speed of solving

pygame.quit()
