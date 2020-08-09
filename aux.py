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
    caminho.append(no.vertice)
  caminho.reverse()
  return caminho

def imprime_atual(estado, imprimir):
  print("Estado atual:")
  print(imprimir(estado))

def imprime_sucessores(estados_sucessores, imprimir):
  print("Estados sucessores:")
  for estado_sucessor in estados_sucessores:
    print(imprimir(estado_sucessor))
    print("\n")
  input()