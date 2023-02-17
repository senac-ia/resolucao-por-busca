import itertools
from no import No

class Barqueiro:
  def __init__(self):
    self.estado_objetivo = (frozenset(),frozenset({"🚣‍♂️", "🐑","🥬","🐺"}))
    self.estado_inicial = (frozenset({"🐑","🥬","🐺","🚣‍♂️"}),frozenset())

  def imprimir(self, no):
    return no.estado

  def gerar_no(self, estado):
    return No(estado)

  def iniciar(self):
    self.no_raiz = No(self.estado_inicial)
    return self.no_raiz

  def testar_objetivo(self, no):
    return no.estado == self.estado_objetivo
  
  def gerar_sucessores(self, no):
    estado = no.estado

    # onde testá o barqueiro
    (esquerda, direita) = estado
    sucessores = []
      
    if "🚣‍♂️" in esquerda:
      direita = frozenset(direita.union({"🚣‍♂️"}))
      esquerda = frozenset(esquerda.difference({"🚣‍♂️"}))
      
      # barqueiro vai sozinho
      if self._valida(esquerda):
        sucessores.append(No((esquerda,direita), no, "🚣‍♂️D"))

      sucessores += self._barqueiro_leva_um(no, esquerda, direita, "E")
      sucessores += self._barqueiro_leva_dois(no, esquerda, direita, "E")
    else: 
      direita = frozenset(direita.difference({"🚣‍♂️"}))
      esquerda = frozenset(esquerda.union({"🚣‍♂️"}))
      # barqueiro vai sozinho
      if self._valida(direita):
        sucessores.append(No((esquerda,direita), no, "🚣‍♂️E"))

      sucessores += self._barqueiro_leva_um(no, direita, esquerda, "D")
      sucessores += self._barqueiro_leva_dois(no, direita, esquerda, "D")
    return sucessores

  def _barqueiro_leva_um(self, no, lado, lado_oposto, simbolo):
    sucessores = []
    if (len(lado) >= 1):
      for elemento in list(lado):
        lado_oposto2 = frozenset(lado_oposto.union({elemento}))
        lado2 = frozenset(lado.difference({elemento}))
        if self._valida(lado2):
          if simbolo == "D":
            sucessores.append(No((lado_oposto2,lado2), no, "🚣" + elemento + "E"))
          else:
            sucessores.append(No((lado2,lado_oposto2), no, "🚣" + elemento + "D"))
    return sucessores

  def _barqueiro_leva_dois(self, no, lado, lado_oposto, simbolo):
    sucessores = []
    if (len(lado) >= 2):
      combinacao_elementos = list(itertools.combinations(lado, 2))
      for (e1,e2) in combinacao_elementos:
        lado_oposto2 = frozenset(lado_oposto.union({e1,e2}))
        lado2 = frozenset(lado.difference({e1,e2}))
        if self._valida(lado2):
          if simbolo == "D":
            sucessores.append(No((lado_oposto2,lado2), no, "🚣" + e1 + e2 + "E"))
          else:
            sucessores.append(No((lado2,lado_oposto2), no, "🚣" + e1 + e2 + "D"))
    return sucessores

  def _valida(self, lado):
    if("🐑" in lado and "🥬" in lado):
      return False
    if("🐑" in lado and "🐺" in lado):
      return False
    return True