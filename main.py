
#!-*- coding: utf8 -*-
from agente             import Agente
from manipula_tabuleiro import get_sala, print_tt, index_pos, print_array, set_matriz_tabuleiro
import time
import os
import sys

def argumento_matriz(arg):
  t1 =  ['O','','','','','','','','','','','','','','','']
  t2 =  ['','','','','','','','','','','','','','','','O']
  t3 =  ['','','','','','','','','P','','','','','O','','']
  t4 =  ['','','','','','','','','O','','','','','P','','']
  t5 =  ['','','P','','','','','','','','','O','','','P','']
  t6 =  ['','P','O','','','P','','','','','W','','','','P','']
  switcher = { 't1': t1, 't2': t2, 't3': t3, 't4': t4, 't5': t5, 't6': t6 }
  
  return switcher.get(arg, arg)


matriz = argumento_matriz(sys.argv[1] if len(sys.argv) > 1 else 'x')
if matriz != 'x':
  set_matriz_tabuleiro(matriz)
agente = Agente(get_sala(1, 1))

while True:
  
  agente.analisa_sala()
  action = agente.movimentar()
  if action.startswith('ESTA'):
    print(action)
  if action.startswith('AGENTE'):
    print(action)
  if action == 'STOP':
    print('Parou o movimento por causa de implementacao')
  if action == 'OURO':
    print('Achou ouro na casa {}'.format(index_pos(agente.sala_atual.index)))
  if action == 'MORREU':
    print('A inteligencia não foi suficiente para achar o ouro.')
  if action == 'OURO':
    agente.voltar()
    if agente.tiro == True:
      print('Finalizou o jogo com 1000 pontos')
    else:
      print('Finalizou o jogo com 990 pontos')
    
  if action == 'OURO' or action == 'STOP' or action == 'MORREU':
    break
  time.sleep(1)
  
  
