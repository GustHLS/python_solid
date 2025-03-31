from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery

cliente = Cliente("João", "Rua A, 123")
item_1 = Item("Camiseta", 29.99)
item_2 = Item("Calça Jeans", 49.99)
print(f"Item: {item_1.nome}, Preço: {item_1.preco}")
print(f"Item: {item_2.nome}, Preço: {item_2.preco}")
print(f"Nome: {cliente.nome}, Endereço: {cliente.endereco}")

itens = [item_1, item_2]
pedido_retirada = PedidoRetirada(cliente, itens)
print(f"Total do pedido: {pedido_retirada.calcular_total():.2f}")

pedido_delivery = PedidoDelivery(cliente, itens, 5.0)
print(f"Total do pedido: {pedido_delivery.calcular_total():.2f}")