

def criar_grafo(matriz, info, row, col):

	x_0 = info[1][0]
	y_0 = info[1][1]

	# D(0) -> E(1) -> C(2) -> B(3)
	grafo = {}
	for i in range(0,info[0]): #cria os vertices
		grafo[i] = []

	#guarda a posições do nos a serem inciados
	pos = [[x_0, y_0]]

	_, direcoes = verificar_pos(matriz, row, col, x_0, y_0)

	while True:

		dist = 0

		for pos_atual in pos:
			pos_nos_adj	= criar_grafo_aux(matriz, grafo, pos_atual, row, cow, dir, dist)
		
		###passa o nos adjacentes para serem iniciados
		pos = pos_nos_adj


	return grafo



def criar_grafo_aux(matriz, grafo, pos_atual, row, cow, direcao, dist, no_0, no_adj):

	_, direcoes = verificar_pos(matriz, row, col, pos_atual[0], pos_atual[1])

	##caso encontre um novo nó
	if(type(matriz[pos_atual[0]][pos_atual[1]]) == int and matriz[pos_atual[0]][pos_atual[1]] != no_atual): 

		grafo[no_0].append([matriz[pos_atual[0]][pos_atual[1]], dist, -1])
		grafo[matriz[pos_atual[0]][pos_atual[1]]].append([matriz[no_0], dist, -1])

		no_adj.append(matriz[pos_atual[0]][pos_atual[1]])

		return



	else:

		matriz[atual[0]][atual[1]] = '@'
		dist+=1

		if 0 in direcoes: # direita			
			pos_atual[1]+=1
			dist+=1
			grafo = criar_grafo_aux(matriz, grafo, pos_atual, row, cow, direcao, dist)

		if 1 in direcoes: # esquerda
			pos_atual[1]-=1
			dist+=1
			grafo = criar_grafo_aux(matriz, grafo, pos_atual, row, cow, direcao, dist)

		if 2 in direcoes: # cima
			pos_atual[0]-=1
			dist+=1
			grafo = criar_grafo_aux(matriz, grafo, pos_atual, row, cow, direcao, dist)
		
		if 3 in direcoes: #baixo
			pos_atual[0]+=1
			dist+=1	
			grafo = criar_grafo_aux(matriz, grafo, pos_atual, row, cow, direcao, dist)		

		return grafo


## verifica se aquele ponto pode ser nó e retorna as direçoes 
def verificar_pos(matriz,row,col,i,j):

	direcoes = []

	if(i == 0): # esta na primeira linha

		if(j == 0): # esta na primeira coluna
			
			if(matriz[i+1][j] == "*" or type(matriz[i+1][j]) == int): # Pode ir pra baixo (3)
				direcoes.append(3)
			if(matriz[i][j+1] == "*" or type(matriz[i][j+1]) == int): # Pode ir pra direita (0)
				direcoes.append(0)

		elif(j == col-1): # esta na ultima coluna 
			
			if(matriz[i+1][j] == "*" or type(matriz[i+1][j]) == int): # Pode ir pra baixo (3)
				direcoes.append(3)
			if(matriz[i][j-1] == "*" or type(matriz[i][j-1]) == int): # Pode ir pra esquerda (1)
				direcoes.append(1)

		else: # esta na primeira linha mas ñ esta nas extremidades => n verificar i-1
			
			if(matriz[i+1][j] == "*" or type(matriz[i+1][j]) == int): # Pode ir pra baixo (3)
				direcoes.append(3)
			if(matriz[i][j+1] == "*" or type(matriz[i][j+1]) == int): # Pode ir pra direita (0)
				direcoes.append(0)
			if(matriz[i][j-1] == "*" or type(matriz[i][j-1]) == int): # Pode ir pra esquerda (1)
				direcoes.append(1)


	elif (i == row-1): # esta na ultima linha
		
		if(j == 0):# esta primeira coluna

			if(matriz[i][j+1] == "*" or type(matriz[i][j+1]) == int): # Pode ir pra direita (0)
				direcoes.append(0)
			if(matriz[i-1][j] == "*" or type(matriz[i-1][j]) == int): # Pode ir pra cima (2)
				direcoes.append(2)

		elif(j == col-1): # esta na ultima coluna

			if(matriz[i-1][j] == "*" or type(matriz[i-1][j]) == int): # Pode ir pra cima (2)
				direcoes.append(2)
			if(matriz[i][j-1] == "*" or type(matriz[i][j-1]) == int): # Pode ir pra esquerda (1)
				direcoes.append(1)

		else: # esta na ultima linha mas ñ esta nas extremidades => n verificar i+1
			
			if(matriz[i][j+1] == "*" or type(matriz[i][j+1]) == int): # Pode ir pra direita (0)
				direcoes.append(0)
			if(matriz[i-1][j] == "*" or type(matriz[i-1][j]) == int): # Pode ir pra cima (2)
				direcoes.append(2)
			if(matriz[i][j-1] == "*" or type(matriz[i][j-1]) == int): # Pode ir pra esquerda (1)
				direcoes.append(1)

	else: # nao esta na ultima nem na primeira linha

		if(j == 0): # esta na primeira coluna => n verificar j-1
			
			if(matriz[i+1][j] == "*" or type(matriz[i+1][j]) == int): # Pode ir pra baixo (3)
				direcoes.append(3)
			if(matriz[i][j+1] == "*" or type(matriz[i][j+1]) == int): # Pode ir pra direita (0)
				direcoes.append(0)
			if(matriz[i-1][j] == "*" or type(matriz[i-1][j]) == int): # Pode ir pra cima (2)
				direcoes.append(2)
		
		elif(j == col-1): # esta na ultima coluna => n verificar j+1 

			if(matriz[i+1][j] == "*" or type(matriz[i+1][j]) == int): # Pode ir pra baixo (3)
				direcoes.append(3)
			if(matriz[i-1][j] == "*" or type(matriz[i-1][j]) == int): # Pode ir pra cima (2)
				direcoes.append(2)
			if(matriz[i][j-1] == "*" or type(matriz[i][j-1]) == int): # Pode ir pra esquerda (1)
				direcoes.append(1)
		else: # nao esta em nenhuma das extremidades => pode verificar todas as posiçoes

			if(matriz[i+1][j] == "*" or type(matriz[i+1][j]) == int): # Pode ir pra baixo (3)
				direcoes.append(3)
			if(matriz[i][j+1] == "*" or type(matriz[i][j+1]) == int): # Pode ir pra direita (0)
				direcoes.append(0)
			if(matriz[i-1][j] == "*" or type(matriz[i-1][j]) == int): # Pode ir pra cima (2)
				direcoes.append(2)
			if(matriz[i][j-1] == "*" or type(matriz[i][j-1]) == int): # Pode ir pra esquerda (1)
				direcoes.append(1)

	
	if(len(direcoes)>2):
		return True, direcoes
	else:
		return False, direcoes

## marca na matriz as posições dos nós que serão criados
def encontrar_nos(matriz,row,col):

	no = 0

	##guarda a pos do nó 0 caso ele n for o inicio 
	pos_aux = []

	##posicao dos nós inicial e final e qtd de nos
	info = []

	for i in range(0, row):
		for j in range(0,col):
		
			if (matriz[i][j] == '#'): # Inicio sempre será o 0

				if(no == 0):
					matriz[i][j] = no
				else: # Caso ele n for ser 0, faço a troca
					matriz[i][j] = 0
					matriz[pos_aux[0]][pos_aux[1]] = no
				
				pos_i = (i, j)
				no+=1
			
			elif(matriz[i][j] == '$'): # Fim
				matriz[i][j] = no
				pos_f = (i, j)
				no+=1

			elif(matriz[i][j] == "-"):
				pass
			
			else:
				cond, _ = verificar_pos(matriz,row,col,i,j) # Se a pos pode ser um nó

				if(cond):				
					if(no == 0):
						pos_aux.append(i);
						pos_aux.append(j);

					matriz[i][j] = no				
					no+=1

	info.append(no)
	info.append(pos_i)
	info.append(pos_f)
	return info
	

## printa a matriz
def print_matriz(matriz, row, col):

	for i in range(0,row):
		for j in range(0,col):
			print(matriz[i][j],end ="")
		print("\n")



def main():

 	# abre os arquivos
	arq = open("labirinto.txt",'r')
	
	# define row e col
	row = int(arq.read(2))
	col = int(arq.read(4))

	# cria um arquivo 
	M = arq.readlines()

	# retira os  '\n'
	M = [row.rstrip('\n') for row in M]

	info = []

	
	#transforma de um jeito de fácil manipulacao
	matriz = [[M[x][y] for y in range(col)] for x in range(row)] 

	print_matriz(matriz,row,col)
	
	info = encontrar_nos(matriz,row,col)
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

	print_matriz(matriz,row,col)

	grafo = criar_grafo(matriz,info,row,col)
	
	print (grafo)
	arq.close()

if __name__ == '__main__':
	main()