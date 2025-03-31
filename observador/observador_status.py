class ObservadorStatus:
    def __init__(self, notificacoes):
        self.notificacoes = notificacoes

    def atualizar(self, pedido):
        mensagem = f"Status do pedido foi atualizado para: {pedido.status}"
        self.notificacoes.enviar_notificacao(pedido.cliente, mensagem)