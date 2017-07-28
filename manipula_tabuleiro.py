#!-*- coding: utf8 -*-
from tabuleiro  import novo_tabuleiro, Sala
import os
import time

matriz_tabuleiro = novo_tabuleiro() 


def print_tt(tabuleiro, index, seguros, seguros_n_visitados, suspeitos, caminho, t, tem_ouro):
  time.sleep(t)
  os.system('cls' if os.name == 'nt' else 'clear')
  print('=============================================================   Legenda:')
  for i in range(16):
    if(tabuleiro[i].ouro == True and tem_ouro == False):
      print ('['+ '\033[93m' + tabuleiro[i].__str__() + '\033[0m' + ']', end='\t')
    elif (tabuleiro[i].poco == True):
      print ('['+'\033[94m' + tabuleiro[i].__str__() + '\033[0m' + ']', end='\t')
    elif (tabuleiro[i].wumpus == True):
      print ('['+'\033[91m' + tabuleiro[i].__str__() + '\033[0m' + ']', end='\t')
    elif(index == i):
      if tem_ouro == True:
        print ('['+'\033[93m' + tabuleiro[i].__str__() + '\033[0m' + ']', end='\t')
      else:
        print('['+ '\033[32m' + tabuleiro[i].__str__() + '\033[0m' + ']', end='\t')
    else:
      print('['+ tabuleiro[i].__str__()+ ']', end='\t')
    if (i+1) % 4 == 0:
      if i == 3:
        print('\033[94m[ POÇO ]\033[0m', end='')
      elif i == 7:
        print('\033[91m[ WUMPUS ]\033[0m', end='')
      elif i == 11:
        print('\033[93m[ OURO ]\033[0m', end=' ou ')
        print('\033[93m[ AGENTE COM OURO ]\033[0m', end='')
      elif i == 15:
        print('\033[32m[ AGENTE SEM OURO ]\033[0m', end='')
      print('\n')
  print('=============================================================')
  
  
  # print('Seguros: \n')
  # print_array(seguros)
  # print('\n\nSeguros não visitados: \n')
  # print_array(seguros_n_visitados)
  # print('\n\nSuspeitos: \n')
  # print_array(suspeitos)
  # print('\n\nCaminho: \n')
  # print_array(caminho)
  # print('\n')
  
  


def print_array(arr):
  for s in arr:
    print(s, end=' ')  

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

def get_wumpus(tabuleiro):
  for i in range(len(tabuleiro)):
    [x, y] = index_pos(i)
    if get_sala(x,y).wumpus == True:
      return tabuleiro[i].index
  return -1

def remove_wumpus_e_limpa(tabuleiro):
  for i in range(len(tabuleiro)):
    [x, y] = index_pos(i)
    sala = get_sala(x, y)
    sala.wumpus = False
    sala.atualiza_grito(True)
    sala.atualiza_fedor(False)
    if sala.status == 'SUSPEITO-WUMPUS':
      sala.atualiza_status('SEGURO')
      sala.peso_wumpus = 0

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
  if (indice + 1) % 4 != 0:
    [i, j] = index_pos(indice + 1)
    adjacentes.append(tabuleiro[pos_index(i, j)])
  if indice % 4 != 0:
    [i, j] = index_pos(indice - 1)
    adjacentes.append(tabuleiro[pos_index(i, j)])
  return adjacentes

def atirar(tabuleiro, index, direcao):
  [i, j] = index_pos(index)
  resultado = 'ERROU'
  if direcao == 'C':
    for x in range(i , 5):
      if(pos_index(x, j) == get_wumpus(tabuleiro)):
        resultado = 'MATOU'
        break
  if direcao == 'B':
    for x in range(1, 4):
      if(pos_index(i - x, j) == get_wumpus(tabuleiro)):
        resultado = 'MATOU'
        break
  if direcao == 'D':
    for x in range(i + 1, 5):
      if(pos_index(i, x) == get_wumpus(tabuleiro)):
        resultado = 'MATOU'
        break
  if direcao == 'E':
    for x in range(1, 4):
      if(pos_index(i, j - x) == get_wumpus(tabuleiro)):
        resultado = 'MATOU'  
        break    
  if resultado == 'MATOU': 
    remove_wumpus_e_limpa(tabuleiro)
  return resultado

def set_matriz_tabuleiro(arr_):
  novo_tabuleiro = list(range(16))
  for i in range(len(arr_)):
    novo_tabuleiro[i] = Sala()
    novo_tabuleiro[i].set_index(i)
    if arr_[i] == 'O':
      # print('OURO ' + str(i))
      novo_tabuleiro[i].ouro = True
      novo_tabuleiro[i].atualiza_brilho(True)
    if arr_[i] == 'P':
      # print('POCO ' + str(i))
      novo_tabuleiro[i].poco = True
    if arr_[i] == 'W':
      # print('WUMPUS ' + str(i))
      novo_tabuleiro[i].wumpus = True
  del matriz_tabuleiro[:]
  new_Trab = atualiza_sensores(novo_tabuleiro)
  for i in new_Trab:
    matriz_tabuleiro.append(i)
  


def atualiza_sensores(tabuleiro):
  for i in list(range(16)):
    wumpus = poco = False
    sala   = tabuleiro[i]
    for a in adjacentes(tabuleiro, i):
      if a.wumpus: wumpus = True
      if a.poco: poco = True
    if wumpus: sala.atualiza_fedor(True)
    if poco: sala.atualiza_brisa(True)
    
  return tabuleiro
