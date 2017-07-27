from manipula_tabuleiro import index_pos, get_sala, atirar, print_tt, print_array, adjacentes
from base               import Base, prox_direcao, menor_pass

def next_sala(loc, pos):
  if loc == 'D': return get_sala(pos[0], pos[1] + 1)
  if loc == 'E': return get_sala(pos[0], pos[1] - 1)
  if loc == 'C': return get_sala(pos[0] + 1, pos[1])
  if loc == 'B': return get_sala(pos[0] - 1, pos[1])

def list_op(l_ist):
  to_return = []
  for i in range(len(l_ist)):
    if len(list(filter(lambda x: x.index == l_ist[i].index, to_return))) == 0: 
      to_return.append(l_ist[i])
    else: to_return.pop()
  return to_return


class Agente:
  def __init__(self, atual):
    self.caminho      = [atual]
    self.sala_atual   = atual
    self.sala_antiga  = atual
    self.posicao      = 'D'
    self.ouro         = False
    self.base         = Base()
    self.tiro         = True
    self.to_back      = []
    self.goin_back    = False


  def voltar(self):
    self.goin_back = True
    while self.sala_atual.index != 12:
      next_to_go  = self.to_back.pop() 
      dire        = prox_direcao(self.sala_atual.index, next_to_go.index) 
      self.mover('_;{}'.format(dire)) 
      print_tt(self.base.tabuleiro_real, self.sala_atual.index, self.base.seguros, self.base.seguros_n_visitados, self.base.todos_suspeitos_print(), self.caminho, 1)
      
  def mover(self, todo):
    [_, loc] = todo.split(';')
    pos = index_pos(self.sala_atual.index)
    self.sala_antiga = self.sala_atual
    if loc == 'D': self.sala_atual =  get_sala(pos[0], pos[1] + 1)
    if loc == 'E': self.sala_atual =  get_sala(pos[0], pos[1] - 1)
    if loc == 'C': self.sala_atual =  get_sala(pos[0] + 1, pos[1])
    if loc == 'B': self.sala_atual =  get_sala(pos[0] - 1, pos[1])
    if self.goin_back == False:
      self.to_back = list_op(self.caminho)
    self.caminho.append(self.sala_atual)
    return loc
  
  def analisa_sala(self):
    self.base.tell(self.sala_atual, self.sala_antiga)
    print_tt(self.base.tabuleiro, self.sala_atual.index, self.base.seguros, self.base.seguros_n_visitados, self.base.todos_suspeitos_print(), self.caminho, 0)
    
  def movimentar(self):
    if self.sala_atual.ouro == True:    return 'OURO'
    if self.sala_atual.poco == True:    return 'MORREU'
    if self.sala_atual.wumpus == True:  return 'MORREU'

    next = self.base.ask(self.sala_atual.index)
    if next.startswith('ACTION'):
      [_, action,todo, loc] = next.split(';')
      if action == 'ROLLBACK':
        adj_indices = list(map(lambda x: x.index, adjacentes(self.base.tabuleiro, int(loc))))
        if(self.sala_atual.index not in adj_indices):
          while True:
            self.caminho.pop()
            antiga      = self.sala_atual 
            next_to_go  = self.caminho.pop() 
            dire        = prox_direcao(self.sala_atual.index, next_to_go.index) 
            self.mover('_;{}'.format(dire)) 
            print_tt(self.base.tabuleiro_real, self.sala_atual.index, self.base.seguros, self.base.seguros_n_visitados, self.base.todos_suspeitos_print(), self.caminho, 1)
            if (self.sala_atual.index in adj_indices): break
        if todo == 'ATIRAR':
          action = 'ATIRAR'
          loc = prox_direcao(self.sala_atual.index, int(loc))
        if todo == 'POCO':
          next = 'MOVE;{}'.format(prox_direcao(self.sala_atual.index, int(loc)))

      if action == 'ATIRAR':
        if(self.tiro == True): 
          self.base.afirma('NUM_FLECHAS', 0)
          resultado = atirar(self.base.tabuleiro, self.sala_atual.index, loc)
          self.base.afirma('SEGURO', next_sala(loc, index_pos(self.sala_atual.index)).index)
          return 'AGENTE ESTA EM {} E ATIROU PARA A POSICAO {}, E TEVE RESULTADO: {}'.format(index_pos(self.sala_atual.index), loc,resultado)

        return 'STOP'

    if next.startswith('MOVE'):
      
      antiga  = self.sala_atual
      loc     = self.mover(next)
      if loc == 'X': return 'STOP'
      return 'ESTA EM {} E VAI PARA A CASA {}'.format(index_pos(antiga.index), index_pos(self.sala_atual.index))
