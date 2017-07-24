from manipula_tabuleiro import index_pos, get_sala, atirar
from base               import Base

class Agente:
  def __init__(self, atual):
    self.caminho      = [atual]
    self.sala_atual   = atual
    self.sala_antiga  = atual
    self.posicao      = 'D'
    self.ouro         = False
    self.base         = Base()
    self.tiro         = True

  def achou_ouro(self):
    return self.ouro
  def analisa_sala(self):
    print(index_pos(self.sala_atual.index), self.sala_atual.sensores)
    self.base.tell(self.sala_atual, self.sala_antiga)
  def movimentar(self):
    todo = self.base.ask(self.sala_atual.index)
    print(todo)
    if todo.startswith('ACTION'):
      [_, action, loc] = todo.split(';')
      if action == 'PEGAR':
        self.achou_ouro = True
      if action == 'ATIRAR':
        if(self.tiro == True):
          atirar(self.sala_atual.index, loc)
        self.tiro = False
    if todo.startswith('MOVE'):
      [_, loc] = todo.split(';')
      pos = index_pos(self.sala_atual.index)
      self.sala_antiga = self.sala_atual
      if loc == 'D':
        self.sala_atual =  get_sala(pos[0], pos[1] + 1)
        return 0
      if loc == 'E':
        self.sala_atual =  get_sala(pos[0], pos[1] - 1)
        return 0
      if loc == 'C':
        self.sala_atual =  get_sala(pos[0] + 1, pos[1])
        return 0
      if loc == 'B':
        self.sala_atual =  get_sala(pos[0] - 1, pos[1])
        return 0
      if loc == 'X':
        return 101010
