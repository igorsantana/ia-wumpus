from agente             import Agente
from manipula_tabuleiro import get_sala, print_tt, index_pos
import time

# print("----------------------------------------------------------------")
print_tt()

agente007 = Agente(get_sala(1, 1))

while True:
  agente007.analisa_sala()
  action = agente007.movimentar()
  if action == 'TIRO':
    [_, loc, resultado] = action.split(';')
    print('Atirou em {} e {}'.format(loc, resultado))
  if action == 'STOP':
    print('Parou o movimento por causa de implementacao')
  if action == 'OURO':
    print('Achou ouro na casa {}'.format(index_pos(agente007.sala_atual.index)))
  if action == 'OURO' or action == 'STOP':
    break
  print(action)
  time.sleep(5)
  
