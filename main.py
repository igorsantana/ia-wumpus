from agente             import Agente
from manipula_tabuleiro import get_sala, print_tt

# print("----------------------------------------------------------------")
# print_tt()

agente007 = Agente(get_sala(1, 1))

# while agente007.achou_ouro() == False:
agente007.analisa_sala()
x = agente007.movimentar()
  # if x == 101010: break
