from notificacao.notificacao import Notificacao

class NotificacaoEmail(Notificacao):
    def enviar(self, cliente, mensagem):
        print(f"Enviando email para {cliente.nome}: {mensagem}")