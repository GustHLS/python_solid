from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery

class PedidoFacade:
    
    @staticmethod
    def criar_pedido_retirada(tipo_pedido, cliente, itens, taxa_entrega):
        if tipo_pedido == "retirada":
            return PedidoRetirada(cliente, itens)
        elif tipo_pedido == "delivery":
            return PedidoDelivery(cliente, itens, taxa_entrega)
        else:
            raise ValueError(f"Tipo de pedido '{tipo_pedido}' inválido.")