from abc import ABC, abstractmethod
from observer import Subject

class Avaliacao(ABC):
    @abstractmethod
    def avaliar(self, resposta1: str, resposta2: str) -> str:
        pass

class AvaliacaoTamanho(Avaliacao, Subject):
    def __init__(self):
        Avaliacao.__init__(self)
        Subject.__init__(self)

    def avaliar(self, resposta1: str, resposta2: str) -> str:
        if len(resposta1) > len(resposta2):
            resultado = resposta1
        else:
            resultado = resposta2
        self.notify_observers(resultado)
        return resultado
        
class AvaliacaoClareza(Avaliacao):
    def __init__(self, palavras_chave: set):
        self.palavras_chave = palavras_chave

    def contar_palavras_chave(self, resposta: str) -> int:
        contagem = sum(resposta.lower().count(palavra) for palavra in self.palavras_chave)
        return contagem

    def avaliar(self, resposta1: str, resposta2: str) -> str:
        contagem1 = self.contar_palavras_chave(resposta1)
        contagem2 = self.contar_palavras_chave(resposta2)

        if contagem1 > contagem2:
            return resposta1
        else:
            return resposta2
    
class Avaliador:
    def __init__(self, estrategia: Avaliacao):
        self.estrategia = estrategia

    def avaliar(self, resposta1: str, resposta2: str) -> str:
        return self.estrategia.avaliar(resposta1, resposta2)
