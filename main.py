from cliente import Cliente
from item import Item

cliente = Cliente("João", "Rua A, 123")
item_1 = Item("Camiseta", 29.99)
item_2 = Item("Calça Jeans", 49.99)
print(f"Item: {item_1.nome}, Preço: {item_1.preco}")
print(f"Item: {item_2.nome}, Preço: {item_2.preco}")
print(f"Nome: {cliente.nome}, Endereço: {cliente.endereco}")