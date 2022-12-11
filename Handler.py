from Client import Client
from Product import Product
import random 

class Handler:
    def __init__(self):
        self.clientsList = []
        self.productsList = []
        self.aux = None

    #adcionar mock clientes
    def add_mock_clients(self):
        self.clientsList.append(Client(random.randint(11,999), "Cliente", 11111111111))
        print("\nMock de Clientes adcionado com sucesso!")

    #adcionar novos clientes
    def add_clients(self, id, name, cpf):
        self.clientsList.append(Client(id, name, cpf))
        print("Cliente cadastrado com sucesso!\n")

    #exibir clientes
    def show_clients(self):
        print("\n ~~ Lista de Clientes ~~")
        for i in self.clientsList:
            print(f"Id:{i.id} Nome:{i.name} CPF:{i.cpf}")

    #remover clientes
    def remove_clients(self, id):
        for i in self.clientsList:
            if id == i.id:
                self.aux = self.clientsList.index(i)
        if self.aux is not None:
            self.clientsList.pop(self.aux)
            print("Cliente removido com sucesso!\n")
            self.aux = None
        else:
            print("Esse Cliente não existe, consulte a nossa lista!\n")
                
    #alterar clientes
    def edit_clients(self, id):
        for i in self.clientsList:
            if id == i.id:
                self.aux = self.clientsList.index(i)
        if self.aux is not None:
            newName = input("Digite o nome atualizado do cliente:\n")
            newCpf = int(input("Digite o CPF atualizado do cliente:\n"))
            self.clientsList[self.aux] = Client(id, newName, newCpf)
            print("Cliente atualizado com sucesso!\n")
            self.aux = None
        else:
            print("Esse Cliente não existe, consulte a nossa lista!\n")
        
   
   
    #adcionar mock produtos
    def add_mock_products(self):
        self.productsList.append(Product(random.randint(11,999), "Produto", 10, 50.0, "Loja"))
        self.productsList.append(Product(random.randint(11,999), "Produto", 10, 50.0, "Fornecedor"))
        print("\nMock de Produtos adcionado com sucesso!")

    #adcionar novos produtos
    def add_products(self, id, name, qtd, price, provider):
        self.productsList.append(Product(id, name, qtd, price, provider))
        print("Produto cadastrado com sucesso!\n")

    #exibir produtos
    def show_products(self):
        print("\n ~~ Lista de Produtos da Loja ~~")
        for i in self.productsList:
            if i.provider == "Loja":
                print(f"Id:{i.id} Nome:{i.name} Quantidade:{i.qtd} Preço:R${i.price}")

    #exibir produtos dos fornecedores
    def show_products_f(self):
        print("\n ~~ Lista de Produtos de Fornecedores ~~")
        for i in self.productsList:
            if i.provider != "Loja":
                print(f"Id:{i.id} Nome:{i.name} Quantidade:{i.qtd} Preço:R${i.price} Fornecedor:{i.provider}")

    #remover produtos
    def remove_products(self, id):
        for i in self.productsList:
            if id == i.id:
                self.aux = self.productsList.index(i)
        if self.aux is not None:
            self.productsList.pop(self.aux)
            print("Produto removido com sucesso!\n")
            self.aux = None
        else:
            print("Esse Produto não existe, consulte a nossa lista!\n")
                
    #alterar produtos
    def edit_products(self, id):
        for i in self.productsList:
            if id == i.id:
                self.aux = self.productsList.index(i)
        if self.aux is not None:
            newName = input("Digite o nome atualizado do produto:\n")
            newQtd = int(input("Digite a quantidade atualizada do produto:\n"))
            newPrice = float(input("Digite o preço atualizado do produto:\n"))
            newProvider = input("Digite o nome atualizado do forncedor (se for a própria loja, digite 'Loja'):\n")
            self.productsList[self.aux] = Product(id, newName, newQtd, newPrice, newProvider)
            print("Produto atualizado com sucesso!\n")
            self.aux = None
        else:
            print("Esse Produto não existe, consulte a nossa lista!\n")
        