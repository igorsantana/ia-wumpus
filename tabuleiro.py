from random import randint

def pr(value):
  return 'F' if value == False else 'T'

class Sala:
  def __init__(self):
    # Fedor, Brisa, Brilho, Grito
    self.sensores = [False,False,False,False]
    # self.adjacentes = []
    self.wumpus       = False
    self.ouro         = False
    self.poco         = False
    self.passagens    = 0
    # DESCONHECIDO, SUSPEITO-POCO, SUSPEITO-WUMPUS, SEGURO, PERIGO
    self.status       = 'DESCONHECIDO'
    self.index        = 0
    self.peso_wumpus  = 0
    self.peso_poco    = 0

  def atualiza_fedor(self, fedor):
    self.sensores[0] = fedor
  def atualiza_brisa(self, brisa):
    self.sensores[1] = brisa
  def atualiza_brilho(self, brilho):
    self.sensores[2] = brilho
  def atualiza_grito(self, grito):
    self.sensores[3] = grito
  def atualiza_status(self, status):
    self.status = status
  def atualiza_passagens(self, i):
    self.passagens = i
  def aumenta_peso_wumpus(self, i):
    self.peso_wumpus += i
  def aumenta_peso_poco(self, i):
    self.peso_poco += i

  def __str__(self):
    s = ''
    [i, j] = index_pos(self.index)
    if self.wumpus == True:       s += 'W'
    if self.ouro == True:         s += 'O'
    if self.poco == True:         s += 'P'
    if self.sensores[0] == True:  s += 'F'
    if self.sensores[1] == True:  s += 'B'
    return '[{}, {} ({})]'.format(i, j, s)
    
def cria_tabuleiro():
  wumpus_tabuleiro = [list(range(4)), list(range(4)), list(range(4)), list(range(4))]
  for i in list(range(4)):
    for j in list(range(4)):
      wumpus_tabuleiro[i][j] = Sala()
      wumpus_tabuleiro[i][j].index = ((i * 4) + j)
  return wumpus_tabuleiro

def atualiza_salas(tabuleiro):
  wumpus  = randint(1, 15)
  ouro    = randint(1, 15)
  max_poco = 4
  while wumpus == 12: wumpus = randint(1, 15)
  while ouro == wumpus: ouro = randint(2, 15)

  for i in list(range(4)):
    for j in list(range(4)):
      sala = tabuleiro[i][j]
      x = ((i * 4) + j)
      if x == wumpus:
        sala.wumpus = True
      elif x == ouro:
        sala.ouro = True
        sala.atualiza_brilho(True)
      else:
        if randint(0, 9) <= 1 and x != 12 and max_poco > 0:
          sala.poco = True
          max_poco -= 1
      
  return tabuleiro

def adjacentes(tabuleiro, i, j):
  adjacentes = []
  x = ((i * 4) + j)
  if x > 3:
    adjacentes.append(tabuleiro[i - 1][j])
  if x < 12:
    adjacentes.append(tabuleiro[i + 1][j])
  if x % 4 != 0:
    adjacentes.append(tabuleiro[i][j - 1])
  if (x + 1) % 4 != 0:
    adjacentes.append(tabuleiro[i][j + 1])
  return adjacentes


def atualiza_sensores(tabuleiro):
  for i in list(range(4)):
    for j in list(range(4)):
      wumpus = poco = False
      sala = tabuleiro[i][j]
      for a in adjacentes(tabuleiro, i, j):
        if a.wumpus: wumpus = True
        if a.poco: poco = True
      if wumpus: sala.atualiza_fedor(True)
      if poco: sala.atualiza_brisa(True)
    
      
  return tabuleiro


def novo_tabuleiro():
  array_tabuleiro = []
  tabuleiro = atualiza_sensores(atualiza_salas(cria_tabuleiro()))
  for i in list(range(4)):
    for j in list(range(4)):
      # (tabuleiro[i][j]).adjacentes = adjacentes(tabuleiro, i, j)
      array_tabuleiro.append(tabuleiro[i][j])
  return array_tabuleiro

def novo_tabuleiro_vazio():
  array_tabuleiro = []
  tabuleiro = cria_tabuleiro()
  for i in list(range(4)):
    for j in list(range(4)):
      # (tabuleiro[i][j]).adjacentes = adjacentes(tabuleiro, i, j)
      array_tabuleiro.append(tabuleiro[i][j])
  return array_tabuleiro

def index_pos(index):
  switcher = {
    0:  [4, 1], 1:  [4, 2], 2:  [4, 3], 3:  [4, 4],
    4:  [3, 1], 5:  [3, 2], 6:  [3, 3], 7:  [3, 4],
    8:  [2, 1], 9:  [2, 2], 10: [2, 3], 11: [2, 4],
    12: [1, 1], 13: [1, 2], 14: [1, 3], 15: [1, 4]
    
  }
  return switcher.get(index, -1)