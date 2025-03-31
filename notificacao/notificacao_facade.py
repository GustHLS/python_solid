from notificacao.notificacao_email import NotificacaoEmail
from notificacao.notificacao_sms import NotificacaoSMS

class NotificacaoFacade:
    def __init__(self):
        self.notificacoes = [NotificacaoEmail(), NotificacaoSMS()]

    def enviar_notificacao(self, cliente, mensagem):
        for notificacao in self.notificacoes:
            notificacao.enviar(cliente, mensagem)