from aux import Visitados

# Depth-First Search - Busca em Profundidade
def dfs(problema):
  no = problema.iniciar()

  pilha = Pilha()
  pilha.push(no)

  visitados = Visitados()

  while not pilha.esta_vazio():
    no = pilha.pop()
    visitados.adicionar(no)
    print("Nó Atual")
    print(problema.imprimir(no))
    print("\n")

    # faz o teste objetivo. Se chegou no resultado final
    # retorna o No correspondente
    if(problema.testar_objetivo(no)):
      print(f"Estados visitados: {visitados.tamanho()}")
      return no
    
    # função sucessores define os Nós sucessores
    nos_sucessores = problema.gerar_sucessores(no)

    # para cada sucessor, se armazena se ainda não visitado
    print(f"Nós Sucessores: {len(nos_sucessores)}")
    for no_sucessor in nos_sucessores:
      # pula estado_filho se já foi expandido
      if not visitados.foi_visitado(no_sucessor):
        #print(problema.imprimir(no_sucessor), end=" a\033[A")
        print(problema.imprimir(no_sucessor))
        print("---------")
        pilha.push(no_sucessor)
        
    print("\n")

  print(f"Estados visitados: {visitados.tamanho()}")
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