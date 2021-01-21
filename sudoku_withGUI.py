import pygame, sys

BOARD_ROWS = 9
WIDTH = 500
HEIGHT = 700
SQUARE_WIDTH = 500 / 9
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 5
#green = (0, 255, 0)
#blue = (0, 0, 128)
COLOUR_BLACK = (0,0,0)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_BLUE = (0, 153, 153)
COLOUR_RED = (255,0,0)

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]




class SolveSudoku:
    def find_empty(self, board):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_ROWS):
                if board[row][col] == 0:
                    return (row, col)
        return BOARD_ROWS, BOARD_ROWS

    def checkrow(self, board, row, num):
        for col in range(BOARD_ROWS):
            if board[row][col] ==num:
                return False
        return True

    def checkcol(self, board, col, num):
        for row in range(BOARD_ROWS):
            if board[row][col] ==num:
                return False
        return True

    def checkbox(self, board, row, col, num):
        for i in range(3):
            for j in range(3):
                if board[row + i][col + j] == num:
                    return False

        return True

    def check(self, board, row, col, num):
        if self.checkrow(board, row, num) and self.checkcol(board, col, num) and self.checkbox(board, row - (row%3), col - (col%3), num):
            return True
        else:
            return False

    def solvesudoku(self, board):
        row, col = self.find_empty(board)
        if row != BOARD_ROWS and col != BOARD_ROWS:
            for num in range(1,10):
                    if self.check(board, row, col, num):
                        board[row][col] = num

                        if self.solvesudoku(board):
                            return True
                        
                        board[row][col] = 0
                    
        else:
            return True


class MakeGui:
    def __init__(self, screen, grid, board, checkanswer):
        self.screen = screen
        self.grid = grid
        self.board = board
        self.correctcounter = 0
        self.wrongcounter = 0
        self.checkanswer = checkanswer
        self.draw()

    
    def draw(self):
        
        font = pygame.font.Font('freesansbold.ttf', 32)

        for i in range (BOARD_ROWS): 
            for j in range (BOARD_ROWS):  
                    # Fill blue color in already numbered grid 
                    pygame.draw.rect(self.screen, COLOUR_BLUE, (j * SQUARE_WIDTH, i * SQUARE_WIDTH, SQUARE_WIDTH + 1, SQUARE_WIDTH + 1))
                    if self.grid[i][j]!= 0:
                    # Fill gird with default numbers specified 
                        text = font.render(str(self.grid[i][j]), 1, COLOUR_BLACK) 
                        self.screen.blit(text, (j * SQUARE_WIDTH + 15, i * SQUARE_WIDTH + 15)) 
        
        self.drawboldlines()
        self.makebuttons()
        self.counterUI()

    def drawboldlines(self):
                    
        # Draw lines horizontally and verticallyto form grid            
        for i in range(BOARD_ROWS+1): 
            if i % 3 == 0 : 
                boldwidth = 5
            else: 
                boldwidth = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * SQUARE_WIDTH), (500, i * SQUARE_WIDTH), boldwidth) 
            pygame.draw.line(self.screen, (0, 0, 0), (i * SQUARE_WIDTH, 0), (i * SQUARE_WIDTH, 500), boldwidth) 
        
    

    def makebuttons(self):
        
        #Get Solution Button
        #check = pygame.font.SysFont('Arial', 18)
        check = pygame.font.Font('freesansbold.ttf', 18)
        pygame.draw.rect(self.screen, LINE_COLOR, (0, 530, 120, 30))
        pygame.draw.rect(self.screen, LINE_COLOR, (0, 570, 200, 60)) #for displaying correct/wrong ans
        checktext = check.render("Get Solution", 1 , COLOUR_BLACK)
        self.screen.blit(checktext, (5, 535))

        #Retry button
        pygame.draw.rect(self.screen, LINE_COLOR, (0, 645, 80, 30))
        checktext = check.render("Restart", 1 , COLOUR_BLACK)
        self.screen.blit(checktext, (5, 650))


    
    def counterUI(self):
        counter = pygame.font.Font('freesansbold.ttf', 15)
        pygame.draw.rect(self.screen, LINE_COLOR, (250, 530, 180, 25)) # for text
        pygame.draw.rect(self.screen, LINE_COLOR, (450, 530, 40, 25)) # for counter
        countertext = counter.render("Number of correct tries:", 1 , COLOUR_BLACK)
        self.screen.blit(countertext, (255, 535))
        text = counter.render(str(0), 1, COLOUR_BLACK) 
        self.screen.blit(text, (455, 535))

        pygame.draw.rect(self.screen, LINE_COLOR, (250, 560, 180, 25)) #for text
        pygame.draw.rect(self.screen, LINE_COLOR, (450, 560, 40, 25)) # for counter
        countertext = counter.render("Number of wrong tries:", 1 , COLOUR_BLACK)
        self.screen.blit(countertext, (255, 565))
        text = counter.render(str(0), 1, COLOUR_BLACK) 
        self.screen.blit(text, (455, 565))
    
    
    def updatecorrectcounterUI(self, correctcounter):
        counter = pygame.font.Font('freesansbold.ttf', 15)

        pygame.draw.rect(self.screen, LINE_COLOR, (450, 530, 40, 25)) # for counter
        text = counter.render(str(correctcounter), 1, COLOUR_BLACK) 
        self.screen.blit(text, (455, 535))


    def updatewrongcounterUI(self, wrongcounter):
        counter = pygame.font.Font('freesansbold.ttf', 15)

        pygame.draw.rect(self.screen, LINE_COLOR, (450, 560, 40, 25)) # for counter
        text = counter.render(str(wrongcounter), 1, COLOUR_BLACK) 
        self.screen.blit(text, (455, 565))

    #user select box to key in 
    def selectbox(self, xpos, ypos):
        x = int(xpos // (SQUARE_WIDTH))
        y = int(ypos // (SQUARE_WIDTH))

        if self.grid[y][x] == 0:
            pygame.draw.rect(self.screen, COLOUR_YELLOW, (x * SQUARE_WIDTH, y * SQUARE_WIDTH, SQUARE_WIDTH + 1, SQUARE_WIDTH +1))
            return x, y
        return False
    
    def typeintobox(self, xpos, ypos, key):
        typefont = pygame.font.Font('freesansbold.ttf', 32)
        if not self.selectbox(xpos, ypos):
            x, y = None, None
        else:
            x,y = self.selectbox(xpos, ypos)
            typetext = typefont.render(str(key), 1, COLOUR_BLACK) 
            self.screen.blit(typetext, (x * SQUARE_WIDTH + 15, y * SQUARE_WIDTH + 15))
            self.drawboldlines()
            self.checkwithsolution(x, y, typefont, key)
    
    def checkwithsolution(self, x, y, typefont, key):
        displayfont = pygame.font.Font('freesansbold.ttf', 23)
        pygame.draw.rect(self.screen, LINE_COLOR, (0, 570, 200, 60))
        self.checkanswer[y][x] = key #store response
        if self.board[y][x] == key:
            displaytext = displayfont.render("Correct Answer!", 1, COLOUR_BLACK) 
            self.counter(True)
        else:
            displaytext = displayfont.render("Wrong Answer!", 1, COLOUR_BLACK) 
            pygame.draw.rect(self.screen, COLOUR_RED, (x * SQUARE_WIDTH, y * SQUARE_WIDTH, SQUARE_WIDTH + 1, SQUARE_WIDTH +1))
            typetext = typefont.render(str(key), 1, COLOUR_BLACK) 
            self.screen.blit(typetext, (x * SQUARE_WIDTH + 15, y * SQUARE_WIDTH + 15))
            self.counter(False)
        
        self.screen.blit(displaytext, (5, 575))
    
    def counter(self, correct):

        if correct:
            self.correctcounter += 1
            self.updatecorrectcounterUI(self.correctcounter)
        else:
            self.wrongcounter += 1
            self.updatewrongcounterUI(self.wrongcounter)

    def getsolution(self):
        typefont = pygame.font.Font('freesansbold.ttf', 32)
        
        pygame.draw.rect(self.screen, LINE_COLOR, (0, 570, 200, 60))
        for i in range(BOARD_ROWS):
            for j in range(BOARD_ROWS):
                pygame.draw.rect(self.screen, COLOUR_BLUE, (j * SQUARE_WIDTH, i * SQUARE_WIDTH, SQUARE_WIDTH + 1, SQUARE_WIDTH + 1))
                text = typefont.render(str(self.board[i][j]), 1, COLOUR_BLACK) 
                self.screen.blit(text, (j * SQUARE_WIDTH + 15, i * SQUARE_WIDTH + 15)) 
                #pygame.time.wait(100)
        
        self.drawboldlines()
        self.printsudokusolved()

    def printsudokusolved(self):
        displayfont = pygame.font.Font('freesansbold.ttf', 23)
        displaytext = displayfont.render("Sudoku Solved!", 1, COLOUR_BLACK) 
        self.screen.blit(displaytext, (5, 575))
    
    def restart(self):
        self.draw()

    
    def checkcomplete(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_ROWS):
                if not self.checkanswer[row][col] == self.board[row][col]:  
                    return 
        
        self.printsudokusolved()
                    



def main():
    #copy board to grid
    grid = [x[:] for x in board]

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')

    #solve sudoku
    s = SolveSudoku()

    if not s.solvesudoku(board):
        sys.exit() #no solution exists for sudoku
    
    checkanswer = [x[:] for x in grid]
    m = MakeGui(screen, grid, board, checkanswer)

    while True:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 0 <= x <= 120 and 530 <= y <= 560: #check if Get Solution button is pressed
                    m.getsolution()
                if 0 <= x <= 80 and 645 <= y <= 675: #check if Restart button is pressed
                    m.restart()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                elif event.key == pygame.K_2:
                    key = 2
                elif event.key == pygame.K_3:
                    key = 3
                elif event.key == pygame.K_4:
                    key = 4
                elif event.key == pygame.K_5:
                    key = 5
                elif event.key == pygame.K_6:
                    key = 6
                elif event.key == pygame.K_7:
                    key = 7
                elif event.key == pygame.K_8:
                    key = 8
                elif event.key == pygame.K_9:
                    key = 9
                else:
                    key = None

                if key != None:
                    m.typeintobox(x, y, key)
                

            m.checkcomplete()

        pygame.display.update()

if __name__ == "__main__":
    main()
            
