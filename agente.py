from manipula_tabuleiro import index_pos, get_sala, atirar
from base               import Base

def next_sala(loc, pos):
  if loc == 'D': return get_sala(pos[0], pos[1] + 1)
  if loc == 'E': return get_sala(pos[0], pos[1] - 1)
  if loc == 'C': return get_sala(pos[0] + 1, pos[1])
  if loc == 'B': return get_sala(pos[0] - 1, pos[1])


class Agente:
  def __init__(self, atual):
    self.caminho      = [atual]
    self.sala_atual   = atual
    self.sala_antiga  = atual
    self.posicao      = 'D'
    self.ouro         = False
    self.base         = Base()
    self.tiro         = True

  def mover(self, todo):
    [_, loc] = todo.split(';')
    pos = index_pos(self.sala_atual.index)
    self.sala_antiga = self.sala_atual
    if loc == 'D': self.sala_atual =  get_sala(pos[0], pos[1] + 1)
    if loc == 'E': self.sala_atual =  get_sala(pos[0], pos[1] - 1)
    if loc == 'C': self.sala_atual =  get_sala(pos[0] + 1, pos[1])
    if loc == 'B': self.sala_atual =  get_sala(pos[0] - 1, pos[1])
    return loc
  
  def analisa_sala(self):
    self.base.tell(self.sala_atual, self.sala_antiga)

  def movimentar(self):
    if self.sala_atual.ouro == True:    return 'OURO'
    if self.sala_atual.poco == True:    return 'MORREU'
    if self.sala_atual.wumpus == True:  return 'MORREU'

    next = self.base.ask(self.sala_atual.index)
    
    if next.startswith('ACTION'):
      [_, action, loc] = next.split(';')
      if action == 'ATIRAR':
        resultado = 'ERROU'
        if(self.tiro == True): 
          resultado = atirar(self.base.tabuleiro, self.sala_atual.index, loc)
          if(resultado == 'ERROU'):
            self.base.afirma('SEGURO', next_sala(loc, index_pos(self.sala_atual.index)).index)
        self.tiro = False
        return 'TIRO;{};{}'.format(loc,resultado)
    if next.startswith('MOVE'):
      loc = self.mover(next)
      if loc == 'X': return 'STOP'
      return 'FOI PARA A POSICAO {}, EM DIRECAO A CASA {}'.format(loc, index_pos(self.sala_atual.index))
