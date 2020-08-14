from no import No
from aux import imprime_atual, imprime_atual, imprime_sucessores

# Depth-First Search - Busca em Profundidade
# no_raiz => Instância de No
# testar_objetivo => função que verifica se o estado atual é aceito
# gerar_sucessores => Gera os nós sucessores de acordo com a regra do problema
def dfs(estado_inicial, testar_objetivo, gerar_sucessores, imprimir=str, stepEstado=False, stepSucessores=False):
  pilha = Pilha()
  pilha.push(No(estado_inicial))
  visitados = {estado_inicial} # Conjuntos (Sets) em python e {1, 2, 3}

  while not pilha.esta_vazio():
    no_atual = pilha.pop()
    estado_atual = no_atual.estado
    if stepEstado: imprime_atual(estado_atual, imprimir)

    # faz o teste objetivo conforme a função `teste_objetivo`
    # para a execução se achou o objetivo
    if(testar_objetivo(estado_atual)):
      return no_atual
    
    # verifico os nos filhos e os adiciono na pilha
    # função sucessores define os estados seguintes e adiciona os nós seguintes
    estados_vertices_sucessores = gerar_sucessores(estado_atual)
    if stepSucessores: imprime_sucessores(estados_vertices_sucessores, imprimir)

    print(len(visitados))
    for estados_vertices_sucessor in estados_vertices_sucessores:
      estado_filho = estados_vertices_sucessor[0]
      vertice = estados_vertices_sucessor[1]
      if estado_filho in visitados: # pula estado_filho se já foi expandido
        continue
      visitados.add(estado_filho)
      pilha.push(No(estado_filho, no_atual, vertice))
      
      #print("Tamanho: " + str(pilha.tamanho()))

  return None

class Pilha:
  def __init__(self):
    self.pilha = []
  
  def push(self, item):
    self.pilha.append(item)
  
  def pop(self):
    if(self.esta_vazio()):
        return None
    else:
        return self.pilha.pop()

  def esta_vazio(self):
    return len(self.pilha) == 0

  def tamanho(self):
    return len(self.pilha)