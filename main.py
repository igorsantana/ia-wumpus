from agente             import Agente
from manipula_tabuleiro import get_sala, print_tt
import time

# print("----------------------------------------------------------------")
print_tt()

agente007 = Agente(get_sala(1, 1))

while True:
  y = agente007.analisa_sala()
  if y == 'OURO': 
    print('Achou ouro em {}'.format(agente007.sala_atual))
  x = agente007.movimentar()
  time.sleep(5)
  if x == 101010: break
