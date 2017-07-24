from __future__ import print_function
from tabuleiro  import novo_tabuleiro, print_tabuleiro

matriz_tabuleiro = novo_tabuleiro() 

def print_tt():
  print(len(matriz_tabuleiro))
  for i in range(16):
    print(matriz_tabuleiro[i], end='\t')
    if (i+1) % 4 == 0:
      print('\n')

def index_pos(index):
  switcher = {
    0:  [4, 1], 1:  [4, 2], 2:  [4, 3], 3:  [4, 4],
    4:  [3, 1], 5:  [3, 2], 6:  [3, 3], 7:  [3, 4],
    8:  [2, 1], 9:  [2, 2], 10: [2, 3], 11: [2, 4],
    12: [1, 1], 13: [1, 2], 14: [1, 3], 15: [1, 4]
  }
  return switcher.get(index, -1)

def pos_index(i, j):
  pos = [[12, 13, 14, 15], [8, 9, 10, 11], [4, 5, 6, 7], [0, 1, 2, 3]]
  return pos[i - 1][j - 1]

def get_sala(i, j):
  return matriz_tabuleiro[pos_index(i, j)]

def get_wumpus():
  for i in range(len(matriz_tabuleiro)):
    if matriz_tabuleiro[i].wumpus == True:
      return index_pos(matriz_tabuleiro[i].index)
  return [-1, -1]

def remove_wumpus_e_limpa():
  for i in range(len(matriz_tabuleiro)):
    matriz_tabuleiro[i].wumpus = False
    matriz_tabuleiro[i].atualiza_grito(True)
    matriz_tabuleiro[i].atualiza_fedor(False)
    if matriz_tabuleiro[i].status == 'SUSPEITO-WUMPUS':
      matriz_tabuleiro[i].atualiza_status('SEGURO')

def get_tabuleiro():
  return matriz_tabuleiro

def adjacentes(tabuleiro, indice):
  adjacentes = []
  if indice > 3:
    [i, j] = index_pos(indice - 4)
    adjacentes.append(tabuleiro[pos_index(i, j)])
  if indice < 12:
    [i, j] = index_pos(indice + 4)
    adjacentes.append(tabuleiro[pos_index(i, j)])
  if indice % 4 != 0:
    [i, j] = index_pos(indice - 1)
    adjacentes.append(tabuleiro[pos_index(i, j)])
  if (indice + 1) % 4 != 0:
    [i, j] = index_pos(indice + 1)
    adjacentes.append(tabuleiro[pos_index(i, j)])
  return adjacentes

def atirar(index, direcao):
  [i, j] = index_pos(index)
  resultado = 'ERROU'
  if direcao == 'C':
    for x in range(i , 5):
      if([x, j] == get_wumpus()):
        resultado = 'MATOU'
        break
  if direcao == 'B':
    for x in range(1, 4):
      if([i - x, j] == get_wumpus()):
        resultado = 'MATOU'
        break
  if direcao == 'D':
    for x in range(i + 1, 5):
      if([i, x] == get_wumpus()):
        resultado = 'MATOU'
        break
  if direcao == 'E':
    for x in range(1, 4):
      if([i, j - x] == get_wumpus()):
        resultado = 'MATOU'  
        break    
  if resultado == 'MATOU': remove_wumpus_e_limpa()
  return resultado