from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade

cliente = Cliente("Gustavo", "Rua Alegre, 123")
item_1 = Item("Camiseta", 29.99)
item_2 = Item("Calça Jeans", 49.99)

itens = [item_1, item_2]
pedido_retirada = PedidoRetirada(cliente, itens)
print(f"Total do pedido: {pedido_retirada.calcular_total():.2f}")

pedido_delivery = PedidoDelivery(cliente, itens, 5.0)

valor_pedido = pedido_delivery.calcular_total()
tipo_pagamento = "pix"
pagamento = PagamentoFactory().criar_pagamento(tipo_pagamento)
pagamento.processar(valor_pedido)

MENSAGEM = "Seu pedido saiu para entrega!"
notificacao = NotificacaoFacade()
notificacao.enviar_notificacao(cliente, MENSAGEM)