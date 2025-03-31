from abc import ABC, abstractmethod

class Notificacao(ABC):

    @abstractmethod
    def enviar(self, cliente, mensagem):
        pass
