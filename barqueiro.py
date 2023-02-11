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
            if self._valida(esquerda):
                sucessores.append(No((esquerda,direita), no, "🚣‍♂️D"))

            if (len(esquerda) >= 1):
                for elemento in list(esquerda):
                    direita2 = frozenset(direita.union({elemento}))
                    esquerda2 = frozenset(esquerda.difference({elemento}))
                    if self._valida(esquerda2):
                        sucessores.append(No((esquerda2,direita2), no, "🚣" + elemento + "D"))

            if (len(esquerda) >= 2):
                combinacao_elementos = list(itertools.combinations(esquerda, 2))
                for (e1,e2) in combinacao_elementos:
                    direita2 = frozenset(direita.union({e1,e2}))
                    esquerda2 = frozenset(esquerda.difference({e1,e2}))
                    if self._valida(esquerda2):
                        sucessores.append(No((esquerda2,direita2), no, "🚣" + e1 + e2 + "D"))
        else: 
            direita = frozenset(direita.difference({"🚣‍♂️"}))
            esquerda = frozenset(esquerda.union({"🚣‍♂️"}))
            if self._valida(direita):
                sucessores.append(No((esquerda,direita), no, "🚣‍♂️E"))

            if (len(direita) >= 1):
                for elemento in list(direita):
                    esquerda2 = frozenset(esquerda.union({elemento}))
                    direita2 = frozenset(direita.difference({elemento}))
                    if self._valida(direita2):
                        sucessores.append(No((esquerda2,direita2), no, "🚣" + elemento + "E"))

            if (len(direita) >= 2):
                combinacao_elementos = list(itertools.combinations(direita, 2))
                for (e1,e2) in combinacao_elementos:
                    esquerda2 = frozenset(esquerda.union({e1,e2}))
                    direita2 = frozenset(direita.difference({e1,e2}))
                    if self._valida(direita2):
                        sucessores.append(No((esquerda2,direita2), no, "🚣" + e1 + e2 + "E"))

        return sucessores

    def _valida(self, lado):
        if("🐑" in lado and "🥬" in lado):
            return False
        if("🐑" in lado and "🐺" in lado):
            return False
        return True
