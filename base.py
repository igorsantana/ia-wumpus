from tabuleiro          import novo_tabuleiro
from manipula_tabuleiro import index_pos, pos_index, get_sala, print_tt, get_tabuleiro, adjacentes

matriz_tabuleiro = novo_tabuleiro()

def todos_x(strc, adj):
  todos_x = True
  for i in range(len(adj)):
    if adj[i].status != strc:
      todos_x = False
  return todos_x  

def menor_passagem(adj):
  menor_adj = adj[0]
  for i in range(1,len(adj)):
    if adj[i].passagens < menor_adj.passagens:
      menor_adj = adj[i]
  return menor_adj

def prox_direcao(atual, prox):
  if (atual - 4) == prox:
    return 'C'
  if (atual + 4) == prox:
    return 'B'
  if (atual + 1) == prox:
    return 'D'
  if (atual - 1) == prox:
    return 'E'

class Base:
  def __init__(self):
    self.tabuleiro  = novo_tabuleiro()
       
  def ask(self, index_atual):
    adj  = adjacentes(self.tabuleiro, index_atual)

    if todos_x('SEGURO', adj) == True:
      return 'MOVE;{}'.format(prox_direcao(index_atual, menor_passagem(adj).index))
    if todos_x('SUSPEITO-POCO', adj) == True:
      return 'MOVE;{}'.format(prox_direcao(index_atual, menor_passagem(adj).index))
    if todos_x('SUSPEITO-WUMPUS', adj) == True:
      return 'ACTION;{};{}'.format('ATIRAR', prox_direcao(index_atual, menor_passagem(adj).index))
    
    return 'MOVE;X'

  def tell(self, sala_atual, sala_antiga):
    adj    = adjacentes(matriz_tabuleiro, sala_atual.index)
    [i, j] = index_pos(sala_atual.index)
    sala   = get_sala(i, j)

    self.tabuleiro[sala_atual.index].atualiza_passagens(self.tabuleiro[sala_atual.index].passagens + 1)
    self.tabuleiro[sala_atual.index].atualiza_status("SEGURO")
    
    for k in range(len(adj)):
      [x, y]   = index_pos(adj[k].index)
      if adj[k].index != sala_antiga.index:
        if (sala.sensores[0] == True):
          print('{} foi marcado como suspeito de wumpus'.format([x, y]))
          self.tabuleiro[pos_index(x, y)].atualiza_status("SUSPEITO-WUMPUS")
        if (sala.sensores[1] == True):
          print('{} foi marcado como suspeito de poco'.format([x, y]))
          self.tabuleiro[pos_index(x, y)].atualiza_status("SUSPEITO-POCO")
        if(sala.sensores[0] == False) and (sala.sensores[1] == False):
            self.tabuleiro[pos_index(x, y)].atualiza_status("SEGURO")
      
    return 0
  