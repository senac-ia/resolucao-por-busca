def no_caminho(no):
  caminho = [no.estado]
  while no.no_pai is not None:
    no = no.no_pai
    caminho.append(no.estado)
  caminho.reverse()
  return caminho

def vertice_caminho(no):
  caminho = []
  while no.no_pai is not None:
    no = no.no_pai
    if no.vertice is not None: caminho.append(no.vertice)
  caminho.reverse()
  return caminho

class Visitados:
  def __init__(self, no):
    # Conjuntos (Sets) em python e {1, 2, 3}
    # necessita ser uma tupla por ser comparável com ==
    self.visitados = set({tuple(no.estado)})
  
  def adicionar(self, estado):
    self.visitados.add(tuple(estado))
  
  def foi_visitado(self, estado):
    return tuple(estado) in self.visitados

  def tamanho(self):
    return len(self.visitados)