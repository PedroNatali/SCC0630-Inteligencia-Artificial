#@authors Pedro Natali, Rafael Pinho & Patrick Feitosa

import pygame
import sys
import time


#Colors
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200,0,0)
YELLOW = (255,200,0) 
BLUE = (0,0,200)
GREY = (150,150,150)
BLUE = (0,0,255)

#Size of the block
blockSize = 20 #Set the size of the grid block


#Node class
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.h = 0

    def __eq__(self, other):
        return self.position == other.position


def bestfit(maze, start, end):


    time_begin = time.time()
    # Create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)
    end_node.h = 0
    start_node.h = ((start_node.position[0] - end_node.position[0]) ** 2) + ((start_node.position[1] - start_node.position[1]) ** 2)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.h < current_node.h:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                maze[current.position[0]][current.position[1]] = 'v'
                path.append(current.position)
                current = current.parent
            time_end = time.time()
            print("tempo de execução: ",time_end-time_begin)
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable node
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            aux = 0

            #child cannot be a verified node
            for item in closed_list:
                if item.position == new_node.position:
                    aux=aux+1
            # Append
            if aux == 0:
                children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

           
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node:
                    continue

            # Add the child to the open list
            open_list.append(child)



def ler_arquivo(arquivo):           
    arq = open(arquivo,'r')

    #define row e col
    row = int(arq.read(2))
    col = int(arq.read(4))
    start = (0,0)
    end = (0,0)
    #cria um arquivo 
    M = arq.readlines()
    M = [row.rstrip('\n') for row in M]

    matriz = [[0 for x in range(col)] for y in range(row)] 
    for i in range(0,row):
        for j in range(0,col):
            matriz[i][j] = M[i][j]

    for i in range(0,row):
        for j in range(0,col):
            if M[i][j] == '-':
                matriz[i][j] = 1
            if M[i][j] == '*':
                matriz[i][j] = 0
            if M[i][j] == '#':
                matriz[i][j] = 0
                start = (i,j) 
            if M[i][j] == '$':
                matriz[i][j] = 0
                end = (i,j)

    return matriz, start, end , row, col

    #Desenha de fato
def drawGrid(col, row,comeco,fim,matriz):


    for x in range(col):
        for y in range(row):
            if(matriz[y][x] == "f"):
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(SCREEN, RED, rect)
            elif(matriz[y][x] == "v"):
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(SCREEN, YELLOW, rect)
            elif(matriz[y][x] == "i"):
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(SCREEN, GREEN, rect)
            elif(matriz[y][x] == 0):
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect)
            elif(matriz[y][x] == 1):
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(SCREEN, BLACK, rect)
            else:
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(SCREEN, BLUE, rect)
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, GREY, rect,1)


def main():


    arquivo_entrada = "entrada.txt"
    maze, start, end, row, col = ler_arquivo(arquivo_entrada)

    WINDOW_HEIGHT = (col)*blockSize
    WINDOW_WIDTH = (row)*blockSize

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    pygame.display.set_caption('Best-Fit')
    SCREEN.fill(BLACK)
    pygame.display.flip()
 

    path = bestfit(maze, start, end)
    print(path)

    while True:
        drawGrid(col, row, start, end,maze)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()