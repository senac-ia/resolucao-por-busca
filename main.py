from dfs import dfs
from bfs import bfs
from a_estrela import a_estrela
from aux import vertice_caminho, no_caminho
from quebra_cabeca_de_8 import QuebraCabecaDe8
from quebra_cabeca_de_4 import QuebraCabecaDe4
import numpy as np
from barqueiro import Barqueiro

if __name__ == "__main__":
    #problema = Barqueiro()
    problema = QuebraCabecaDe8()
    # problema não solucionável
    # https://pt.stackoverflow.com/questions/333702/como-verificar-se-o-sliding-puzzle-%C3%A9-solucion%C3%A1vel
    #estado = np.array(["4", "2", "3", "_", "7", "8", "1", "5", "6"])
    
    #problema = QuebraCabecaDe4()
    # problema não solucionável
    #estado = np.array(["_", "3", "1", "2"])
    # problema.define_estado_inicial(estado)
    # print(problema.tem_solucao(estado))

    no_solucao = dfs(problema)
    # no_solucao = bfs(problema)

    #no_solucao = a_estrela(problema)

    if(no_solucao is None):
        print("Não houve solução ao problema")
    else:
        print("Solução:")
        #caminho = no_caminho(no_solucao)
        caminho = vertice_caminho(no_solucao)
        print(caminho)

    print("Estado Inicial:")
    print(problema.imprimir(problema.no_raiz))