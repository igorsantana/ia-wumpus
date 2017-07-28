from agente             import Agente
from manipula_tabuleiro import get_sala, print_tt, index_pos, print_array, set_matriz_tabuleiro
import time
import os

# caso_erro =                 [ '','','','',
#                               '','','','',
#                               'P','','','',
#                               '','O','','' ]

# caso_chutecerto =           [ '','','','',
#                               '','','','',
#                               'O','','','',
#                               '','P','','' ]                          

caso_teste_todos_seguros =  [ 'O','','','',
                              '','','','',
                              '','','','',
                              '','','','' ]

caso_teste_todos_seguros2 =  [ '','','','',
                              '','','','',
                              '','','','',
                              '','','','O' ]

caso_teste_probabilidade =  [ '','','P','',
                              '','','','',
                              '','','','O',
                              '','','P','' ]

caso_teste_fronteira =      [ '','P','O','',
                              '','P','','',
                              '','','W','',
                              '','','P','' ]


caso_x2 =                 [ '','','W','O',
                            '','','','P',
                            '','','','',
                            '','','','' ]

set_matriz_tabuleiro(caso_x2)
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
    print('A inteligência não foi suficiente para achar o ouro.')
  if action == 'OURO':
    agente.voltar()
    if agente.tiro == True:
      print('Finalizou o jogo com 1000 pontos')
    else:
      print('Finalizou o jogo com 990 pontos')
    
  if action == 'OURO' or action == 'STOP' or action == 'MORREU':
    break
  time.sleep(0.25)
  
  
