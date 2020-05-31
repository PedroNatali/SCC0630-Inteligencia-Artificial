#@authors Pedro Natali, Rafael Pinho & Patrick Feitosa

import pygame

#Colors
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200,0,0)
YELLOW = (255,200,0) 
BLUE = (0,0,200)
GREY = (150,150,150)

#Size of the block
blockSize = 20 #Set the size of the grid block


def descobre_melhor(teste1,teste2,teste3,teste4,fim):

	pontuacao1 = abs(teste1[0] - fim[0]) + abs(teste1[1] - fim[1])
	pontuacao2 = abs(teste2[0] - fim[0]) + abs(teste2[1] - fim[1])
	pontuacao3 = abs(teste3[0] - fim[0]) + abs(teste3[1] - fim[1])
	pontuacao4 = abs(teste4[0] - fim[0]) + abs(teste4[1] - fim[1])

	if(pontuacao1 <= pontuacao2):
		if(pontuacao1 <= pontuacao3):
			if(pontuacao1 <= pontuacao4):
				return pontuacao1, teste1
			else:
				return pontuacao4, teste4
		else:
			if(pontuacao3<=pontuacao4):
				return pontuacao3, teste3
			else:
				return pontuacao4, teste4
	else:
		if(pontuacao2 <= pontuacao3):
			if(pontuacao2 <= pontuacao4):
				return pontuacao2, teste2
			else:
				return pontuacao4, teste4
		else:
			if(pontuacao3 <= pontuacao4):
				return pontuaca3, teste3
			else:
				return pontuacao4, teste4


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

def HC(atual, matriz, row, col, fim, lista):

	i = atual[0]
	j = atual[1]


	pontuacao_atual = abs(atual[0] - fim[0]) + abs(atual[1] - fim[1])
	teste1 = atual
	teste2 = atual
	teste3 = atual
	teste4 = atual

	matriz[i][j]= 'v'

	if(pontuacao_atual == 0):
		lista.append([i,j])
		return lista

	#i max = 28 // j max = 25 
	else:

		if ( (i < row ) & (j < col) ):

			if (i == 0):

				if (j == 0):

					#Calcula pontuacao de 1 
					if ( (matriz[i+1][j] == '*' ) or (matriz[i+1][j] == '$') ):
						teste1 = [i+1, j]
						
					#Calcula pontuacao de 2 
					if (matriz[i][j+1] == '*' or matriz[i][j+1] == '$'):
						teste2 = [i, j+1]
						
					pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

					if(pontuacao_res < pontuacao_atual):

						lista.append([i,j])
						atual = teste_res
						HC(atual, matriz, row, col,fim,lista)  

				elif(j == (col-1)):

					if (matriz[i+1][j] == '*'or matriz[i+1][j] == '$' ):
						teste1 = [i+1, j]

					if (matriz[i][j-1] == '*' or matriz[i][j-1] == '$' ):
						teste3 = [i, j-1]

					pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

					if(pontuacao_res < pontuacao_atual):

						lista.append([i,j])
						atual = teste_res
						HC(atual, matriz, row, col,fim,lista)  

				else:

					if (matriz[i+1][j] == ('*'or'$') ):
						teste1 = [i+1, j]

					if (matriz[i][j+1] == '*' or matriz[i][j+1] == '$'):
						teste2 = [i, j+1]

					if (matriz[i][j-1] == '*'or  matriz[i][j-1] == '$' ):
						teste3 = [i, j-1]

					pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

					if(pontuacao_res < pontuacao_atual):

						lista.append([i,j])
						atual = teste_res
						HC(atual, matriz, row, col,fim,lista)  

			elif (i > 0):

				if(i == (row-1)):

					if(j == 0):

						if (matriz[i][j+1] == '*' or matriz[i][j+1] == '$' ):
							teste2 = [i, j+1]


						if (matriz[i-1][j] == '*'or matriz[i-1][j] == '$'):
							teste4 = [i-1, j]

						pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

						if(pontuacao_res < pontuacao_atual):

							lista.append([i,j])
							atual = teste_res
							HC(atual, matriz, row, col,fim,lista)  


					elif(j == (col-1)):

						if (matriz[i][j-1] == '*'or matriz[i][j-1] == '$' ):
							teste3 = [i, j-1]


						if (matriz[i-1][j] == '*'or matriz[i-1][j] == '$'):
							teste4 = [i-1, j]

						pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

						if(pontuacao_res < pontuacao_atual):

							lista.append([i,j])
							atual = teste_res
							HC(atual, matriz, row, col,fim,lista)  


					else:

						if (matriz[i][j+1] == '*'or matriz[i][j+1] == '$'):
							teste2 = [i, j+1]


						if (matriz[i][j-1] == '*'or matriz[i][j-1] == '$' ):
							teste3 = [i, j-1]


						if (matriz[i-1][j] == '*'or matriz[i-1][j] == '$'):
							teste4 = [i-1, j]

						pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

						if(pontuacao_res < pontuacao_atual):

							lista.append([i,j])
							atual = teste_res
							HC(atual, matriz, row, col,fim,lista)  



				else:

					if (j == 0):

						if (matriz[i+1][j] == '*'or matriz[i+1][j] == '$' ):
							teste1 = [i+1, j]

						if (matriz[i][j+1] == '*'or matriz[i][j+1] == '$'):
							teste2 = [i, j+1]

						if (matriz[i-1][j] == '*'or matriz[i-1][j] == '$'):
							teste4 = [i-1, j]

						pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

						if(pontuacao_res < pontuacao_atual):

							lista.append([i,j])
							atual = teste_res
							HC(atual, matriz, row, col,fim,lista)  



					elif( j == (col-1) ):

						if (matriz[i+1][j] == '*'or matriz[i+1][j] == '$' ):
							teste1 = [i+1, j]


						if (matriz[i][j-1] == '*'or matriz[i][j-1] == '$' ):
							teste3 = [i, j-1]


						if (matriz[i-1][j] == '*'or matriz[i-1][j] == '$'):
							teste4 = [i-1, j]

						pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

						if(pontuacao_res < pontuacao_atual):

							lista.append([i,j])
							atual = teste_res
							HC(atual, matriz, row, col,fim,lista)  


					else:

						if (matriz[i+1][j] == '*'or matriz[i+1][j] == '$' ):
							teste1 = [i+1, j]


						if (matriz[i][j+1] == '*'or matriz[i][j+1] == '$'):
							teste2 = [i, j+1]


						if (matriz[i][j-1] == '*'or matriz[i][j-1] == '$' ):
							teste3 = [i, j-1]


						if (matriz[i-1][j] == '*' or matriz[i-1][j] == '$'):
							teste4 = [i-1, j]

						pontuacao_res, teste_res = descobre_melhor(teste1,teste2,teste3,teste4,fim)

						if(pontuacao_res < pontuacao_atual):

							lista.append([i,j])
							atual = teste_res
							HC(atual, matriz, row, col,fim,lista)  



#Desenha de fato
def drawGrid(col, row,lista,comeco,fim,matriz):

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
			else:
				rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
				pygame.draw.rect(SCREEN, BLACK, rect)
			rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
			pygame.draw.rect(SCREEN, GREY, rect,1)



if __name__ == '__main__':


	arquivo_entrada = "entrada3.txt"

	matriz, row, col = ler_arquivo(arquivo_entrada)

	#Window  - (altura = 25 largura = 28 ) x 20
	WINDOW_HEIGHT = (col)*blockSize;
	WINDOW_WIDTH = (row)*blockSize;
	
	global SCREEN, CLOCK
	pygame.init()
	SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
	pygame.display.set_caption('Algoritmo de Hill Climbing')
	#CLOCK = pygame.time.Clock()
	SCREEN.fill(BLACK)
	pygame.display.flip()



	for i in range(0,row):
		for j in range(0,col):
			#print(matrix[i][j], end = "")
			if(matriz[i][j] == '#'):
				inicio = [i,j]

			if(matriz[i][j] == '$'):
				final = [i,j]
		#print()
	

	lista = []
	lista.append( HC(inicio, matriz, row, col, final, lista) )
	matriz[inicio[0]][inicio[1]] = 'i'
	matriz[final[0]][final[1]] = 'f'
	lista.remove(None)
	print(lista)

	# for i in range(0, row):
	# 	for j in range(0, col):

	# 		#if([i,j] in lista):
	# 		#	matriz[i][j] = lista.index([i,j])

	# 		print(matriz[i][j], end = " ")

	# 	print()

	# print()
		

	while True:
		drawGrid(col, row, lista, inicio, final,matriz)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()

