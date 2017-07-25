from random import randint

def pr(value):
  return 'F' if value == False else 'T'





class Sala:
  def __init__(self):
    # Fedor, Brisa, Brilho, Grito
    self.sensores = [False,False,False,False]
    self.adjacentes = []
    self.wumpus     = False
    self.ouro       = False
    self.poco       = False
    self.passagens  = 0
    # DESCONHECIDO, SUSPEITO-POCO, SUSPEITO-WUMPUS, SEGURO, PERIGO
    self.status     = 'DESCONHECIDO'
    self.index      = 0

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
  
  def __str__(self):
    return "[{} Wumpus:{} | Ouro:{} | Poco:{} | Fedor: {} | Brisa: {}]".format(self.index, pr(self.wumpus), pr(self.ouro), pr(self.poco), pr(self.sensores[0]),pr(self.sensores[1]))
    

def cria_tabuleiro():
  wumpus_tabuleiro = [range(4), range(4), range(4), range(4)]
  for i in range(4):
    for j in range(4):
      wumpus_tabuleiro[i][j] = Sala()
      wumpus_tabuleiro[i][j].index = ((i * 4) + j)

  return wumpus_tabuleiro

def atualiza_salas(tabuleiro):
  wumpus  = randint(2, 15)
  ouro    = randint(2, 15)

  while ouro == wumpus: ouro = randint(2, 15)

  for i in range(4):
    for j in range(4):
      sala = tabuleiro[i][j]
      x = ((i * 4) + j)
      if x == wumpus:
        sala.wumpus = True
      elif x == ouro:
        sala.ouro = True
        sala.atualiza_brilho(True)
      else:
        if randint(0, 9) <= 1 and x != 12:
          sala.poco = True
      
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

def print_tabuleiro(tabuleiro):
  for i in range(4):
    for j in range(4):
      print tabuleiro[i][j],
    print


def atualiza_sensores(tabuleiro):
  for i in range(4):
    for j in range(4):
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
  for i in range(4):
    for j in range(4):
      (tabuleiro[i][j]).adjacentes = adjacentes(tabuleiro, i, j)
      array_tabuleiro.append(tabuleiro[i][j])

  return array_tabuleiro


