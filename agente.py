from manipula_tabuleiro import index_pos, get_sala, atirar
from base               import Base

class Agente:
  def __init__(self, atual):
    self.caminho    = [atual]
    self.sala_atual = atual
    self.posicao    = 'D'
    self.ouro       = False
    self.base       = Base()

  def achou_ouro(self):
    return self.ouro
  def analisa_sala(self):
    self.base.tell(self.sala_atual)
  def movimentar(self):
    todo = self.base.ask(self.sala_atual.index)
    
    if todo.startswith('ACTION'):
      [_, action, loc] = todo.split(';')
      if action == 'PEGAR':
        self.achou_ouro = True
      if action == 'ATIRAR':
        print(atirar(14, 'E'))

    
    # pos = index_pos(self.sala_atual.index)
    # if self.posicao == 'D':
    #   self.sala_atual =  get_sala(pos[0], pos[1] + 1)
    #   return 0
    # if self.posicao == 'E':
    #   self.sala_atual =  get_sala(pos[0], pos[1] - 1)
    #   return 0
    # if self.posicao == 'C':
    #   self.sala_atual =  get_sala(pos[0] + 1, pos[1])
    #   return 0
    # if self.posicao == 'B':
    #   self.sala_atual =  get_sala(pos[0] - 1, pos[1])
    #   return 0
    # if self.posicao == 'X':
    #   return 101010

   