from tabuleiro          import novo_tabuleiro
from manipula_tabuleiro import index_pos, pos_index, get_sala, print_tt, get_tabuleiro, adjacentes

matriz_tabuleiro = novo_tabuleiro()

def every(strc, adj):
  every = True
  for i in range(len(adj)):
    if adj[i].status != strc: every = False
  return every  

def menor_pass(adj):
  menor_adj = adj[0]
  for i in range(1,len(adj)):
    if adj[i].passagens < menor_adj.passagens: menor_adj = adj[i]
  return menor_adj

def prox_direcao(atual, prox):
  if (atual - 4) == prox: return 'C'
  if (atual + 4) == prox: return 'B'
  if (atual + 1) == prox: return 'D'
  if (atual - 1) == prox: return 'E'

class Base:
  def __init__(self):
    self.tabuleiro         = novo_tabuleiro()
    self.seguros           = []
    self.segurosnvisitados = []
    
  def ask(self, index_atual):
    adj = adjacentes(self.tabuleiro, index_atual)
    if every('SEGURO', adj) == True:          return 'MOVE;{}'.format(prox_direcao(index_atual, menor_pass(adj).index))
    if every('SUSPEITO-POCO', adj) == True:   return 'MOVE;{}'.format(prox_direcao(index_atual, menor_pass(adj).index))
    if every('SUSPEITO-WUMPUS', adj) == True: return 'ACTION;{};{}'.format('ATIRAR', prox_direcao(index_atual, menor_pass(adj).index))
    return 'MOVE;X'

  def tell(self, sala, sala_antiga):
    adj = adjacentes(matriz_tabuleiro, sala.index)
    self.tabuleiro[sala.index].atualiza_passagens(self.tabuleiro[sala.index].passagens + 1)
    self.tabuleiro[sala.index].atualiza_status("SEGURO")
    self.seguros.append([sala])

    for k in range(len(adj)):
      [x, y]   = index_pos(adj[k].index)
      if adj[k].index != sala_antiga.index:
        if (sala.sensores[0] == True):                                  self.tabuleiro[pos_index(x, y)].atualiza_status("SUSPEITO-WUMPUS")
        if (sala.sensores[1] == True):                                  self.tabuleiro[pos_index(x, y)].atualiza_status("SUSPEITO-POCO")
        if (sala.sensores[0] == False) and (sala.sensores[1] == False): self.tabuleiro[pos_index(x, y)].atualiza_status("SEGURO")
    return 0
  