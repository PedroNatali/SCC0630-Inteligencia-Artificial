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


def ler_arquivo(arquivo):           
	arq = open(arquivo,'r')

	#define row e col
	row = int(arq.read(2))
	col = int(arq.read(4))

	#cria um arquivo 
	M = arq.readlines()
	M = [row.rstrip('\n') for row in M]

	matriz = [[0 for x in range(col)] for y in range(row)] 

	#transforma de um jeito de fácil manipulacao
	for i in range(0,row):
		for j in range(0,col):
			matriz[i][j] = M[i][j]


	arq.close()
	return matriz, row, col

def BFS(matriz, inicio, final, row, col):

	time_begin = time.time()
	visitados = []
	visitar = []
	lista = []
	chegou = False
	i = inicio[0]
	j = inicio[1]
	dist = 0

	visitados.append(inicio)
	atual = inicio
	while not chegou:
		visitados.append(atual)
		i = atual[0]
		j = atual[1]
		if atual == final:
			chegou = True
			print("\n\nCHEGOU!!!\n\n")
			while atual != inicio:
				i = atual[0]
				j = atual[1]
				if matriz[i][j] == "cima":
					matriz[i][j] = 'v'
					i = i-1
					atual = [i,j]
					lista.append(atual)
				elif matriz[i][j] == "baixo":
					matriz[i][j] = 'v'
					i = i+1
					atual = [i,j]
					lista.append(atual)
				elif matriz[i][j] == "direita":
					matriz[i][j] = 'v'
					j = j+1
					atual = [i,j]
					lista.append(atual)
				elif matriz[i][j] == "esquerda":
					matriz[i][j] = 'v'
					j = j-1
					atual = [i,j]
					lista.append(atual)
		else:
			if ( (i < row ) & (j < col) ):
				if i == 0:
					if j == 0:
						if ( (matriz[i+1][j] == '*' ) or (matriz[i+1][j] == '$') ):
							matriz[i+1][j] = "cima"
							visitar.append([i+1,j])
						elif ( (matriz[i][j+1] == '*' ) or (matriz[i][j+1] == '$') ):
							matriz[i][j+1] = "esquerda"
							visitar.append([i,j+1])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
					elif j == col-1:
						if ( (matriz[i+1][j] == '*' ) or (matriz[i+1][j] == '$') ):
							matriz[i+1][j] = "cima"
							visitar.append([i+1,j])
						elif ( (matriz[i][j-1] == '*' ) or (matriz[i][j-1] == '$')):
							matriz[i][j-1] = "direita"
							visitar.append([i,j-1])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
					elif j > 0:
						if ( (matriz[i+1][j] == '*' ) or (matriz[i+1][j] == '$') ):
							matriz[i+1][j] = "cima"
							visitar.append([i+1,j])
						elif ( (matriz[i][j+1] == '*' ) or (matriz[i][j+1] == '$') ):
							matriz[i][j+1] = "esquerda"
							visitar.append([i,j+1])
						elif ( (matriz[i][j-1] == '*' ) or (matriz[i][j-1] == '$')):
							matriz[i][j-1] = "direita"
							visitar.append([i,j-1])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
				elif i == row-1:
					if j == 0:
						if ( (matriz[i][j+1] == '*' ) or (matriz[i][j+1] == '$')):
							matriz[i][j+1] = "esquerda"
							visitar.append([i,j+1])
						elif ( (matriz[i-1][j] == '*' ) or (matriz[i-1][j] == '$')):
							matriz[i-1][j] = "baixo"
							visitar.append([i-1,j])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
					elif j == col-1:
						if ( (matriz[i][j-1] == '*' ) or (matriz[i][j-1] == '$')):
							matriz[i][j-1] = "direita"
							visitar.append([i,j-1])
						elif ( (matriz[i-1][j] == '*' ) or (matriz[i-1][j] == '$') ):
							matriz[i-1][j] = "baixo"
							visitar.append([i-1,j])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
					elif j > 0:
						if ( (matriz[i][j+1] == '*' ) or (matriz[i][j+1] == '$') ):
							matriz[i][j+1] = "esquerda"
							visitar.append([i,j+1])
						elif ( (matriz[i][j-1] == '*' ) or (matriz[i][j-1] == '$') ):
							matriz[i][j-1] = "direita"
							visitar.append([i,j-1])
						elif ( (matriz[i-1][j] == '*' ) or (matriz[i-1][j] == '$') ):
							matriz[i-1][j] = "baixo"
							visitar.append([i-1,j])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
				elif i > 0:
					if j == 0:
						if ( (matriz[i+1][j] == '*' ) or (matriz[i+1][j] == '$')  ):
							matriz[i+1][j] = "cima"
							visitar.append([i+1,j])
						elif ( (matriz[i][j+1] == '*' ) or (matriz[i][j+1] == '$') ):
							matriz[i][j+1] = "esquerda"
							visitar.append([i,j+1])
						elif ( (matriz[i-1][j] == '*' ) or (matriz[i-1][j] == '$') ):
							matriz[i-1][j] = "baixo"
							visitar.append([i-1,j])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
					elif j == col-1:
						if ( (matriz[i+1][j] == '*' ) or (matriz[i+1][j] == '$') ):
							matriz[i+1][j] = "cima"
							visitar.append([i+1,j])
							
						elif ( (matriz[i][j-1] == '*' ) or (matriz[i][j-1] == '$') ):
							matriz[i][j-1] = "direita"
							visitar.append([i,j-1])
						elif ( (matriz[i-1][j] == '*' ) or (matriz[i-1][j] == '$') ):
							matriz[i-1][j] = "baixo"
							visitar.append([i-1,j])
						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
							#dist = matriz[atual[0]][atual[1]] +1
					elif j > 0:
						if ( (matriz[i+1][j] == '*' ) or (matriz[i+1][j] == '$') ):
							matriz[i+1][j] = "cima"
							visitar.append([i+1,j])
						elif ( (matriz[i][j+1] == '*' ) or (matriz[i][j+1] == '$') ):
							matriz[i][j+1] = "esquerda"
							visitar.append([i,j+1])

						elif ( (matriz[i][j-1] == '*' ) or (matriz[i][j-1] == '$') ):
							matriz[i][j-1] = "direita"
							visitar.append([i,j-1])

						elif ( (matriz[i-1][j] == '*' ) or (matriz[i-1][j] == '$') ):
							matriz[i-1][j] = "baixo"
							visitar.append([i-1,j])

						else:
							print(atual)
							atual = visitar[0]
							del(visitar[0])
				

			else:
				print("\n\nERRO!!!\n\n")
	time_end = time.time()
	print("tempo de execução: ",time_end-time_begin)
	print(lista)






#Desenha de fato
def drawGrid(col, row,comeco,fim,matriz):

	# 4 no primeiro == 4 pra direita (colunas da matriz - deve ter 25 nesse caso)
	# 2 no segundo == 2 pra baixo (pra baixo, linhas da matriz - deve ter 28 nesse caso)

	#rect = pygame.Rect(4*blockSize, 2*blockSize, blockSize, blockSize)
	#pygame.draw.rect(SCREEN, RED, rect)

	# Matriz tem 28x25

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
			elif(matriz[y][x] == '*'):
				rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
				pygame.draw.rect(SCREEN, WHITE, rect)
			elif(matriz[y][x] == '-'):
				rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
				pygame.draw.rect(SCREEN, BLACK, rect)
			else:
				rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
				pygame.draw.rect(SCREEN, WHITE, rect)
			rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
			pygame.draw.rect(SCREEN, GREY, rect,1)



if __name__ == '__main__':


	arquivo_entrada = "entrada2.txt"

	matriz, row, col = ler_arquivo(arquivo_entrada)

	#Window  - (altura = 25 largura = 28 ) x 20
	WINDOW_HEIGHT = (col)*blockSize;
	WINDOW_WIDTH = (row)*blockSize;
	
	global SCREEN, CLOCK
	pygame.init()
	SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
	pygame.display.set_caption('Busca em Largura')
	#CLOCK = pygame.time.Clock()
	SCREEN.fill(BLACK)
	pygame.display.flip()



	for i in range(0,row):
		for j in range(0,col):
			#print(matrix[i][j], end = "")
			if(matriz[i][j] == '#'):
				inicio = [i,j]  # [0,2]

			if(matriz[i][j] == '$'):
				final = [i,j]
				print("final = ")
				print(inicio)
		#print()
	

	BFS(matriz,inicio,final,row,col)
	#lista.append( DFS(inicio, matriz, row, col, final, lista) )
	matriz[inicio[0]][inicio[1]] = 'i'
	matriz[final[0]][final[1]] = 'f'
	#lista.remove(None)

	# for i in range(0, row):
	# 	for j in range(0, col):

	# 		#if([i,j] in lista):
	# 		#	matriz[i][j] = lista.index([i,j])

	# 		print(matriz[i][j], end = " ")

	# 	print()

	# print()
		

	while True:
		drawGrid(col, row, inicio, final,matriz)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()