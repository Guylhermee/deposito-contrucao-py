from Client import Client
from Product import Product
from Sale import Sale
from collections import defaultdict
import random 

class Handler:
    clientsList = []
    productsList = []
    saleList = []
    bestSellerList = []
    bestProviderList = []
    money_spent = 0.0
    money_earned = 0.0
    cashier = 0.0
    aux = None

    #adcionar mock clientes
    def add_mock_clients(self):
        self.clientsList.append(Client(random.randint(11,999), "Guilherme B.", 123))
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
                
    #editar clientes
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
        self.productsList.append(Product(1, "C", 10, 20.0, 50.0, "Loja"))
        self.productsList.append(Product(2, "Python", 10, 20.0, 50.0, "Fornecedor"))
        print("\nMock de Produtos adcionado com sucesso!")

    #adcionar novos produtos
    def add_products(self, id, name, qtd, price_buy, price_sell, provider):
        self.productsList.append(Product(id, name, qtd, price_buy, price_sell, provider))
        print("Produto cadastrado com sucesso!\n")

    #exibir produtos
    def show_products(self):
        print("\n ~~ Lista de Produtos da Loja ~~")
        for i in self.productsList:
            if i.provider == "Loja":
                print(f"Id:{i.id} Nome:{i.name} Quantidade:{i.qtd} Preço de Compra:R${i.price_buy} Preço de Venda:R${i.price_sell} ")

    #exibir produtos dos fornecedores
    def show_products_f(self):
        print("\n ~~ Lista de Produtos de Fornecedores ~~")
        for i in self.productsList:
            if i.provider != "Loja":
                print(f"Id:{i.id} Nome:{i.name} Quantidade:{i.qtd} Preço de Compra:R${i.price_buy} Preço de Venda:R${i.price_sell} Fornecedor:{i.provider}")

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
                
    #editar produtos
    def edit_products(self, id):
        for i in self.productsList:
            if id == i.id:
                self.aux = self.productsList.index(i)
        if self.aux is not None:
            newName = input("Digite o nome atualizado do produto:\n")
            newQtd = int(input("Digite a quantidade atualizada do produto:\n"))
            newPriceBuy = float(input("Digite o preço de compra atualizado do produto:\n"))
            newPriceSell = float(input("Digite o preço de venda atualizado do produto:\n"))
            newProvider = input("Digite o nome atualizado do forncedor (se for a própria loja, digite 'Loja'):\n")
            self.productsList[self.aux] = Product(id, newName, newQtd, newPriceBuy, newPriceSell, newProvider)
            print("Produto atualizado com sucesso!\n")
            self.aux = None
        else:
            print("Esse Produto não existe, consulte a nossa lista!\n")
        
    #vender produtos
    def sale(self, cpf, id, qtd):
        for j in self.clientsList:
            if cpf == j.cpf:
                client = self.clientsList[self.clientsList.index(j)]
                for i in self.productsList:
                    if id == i.id and qtd <= i.qtd:
                        self.aux = self.productsList.index(i)
                if self.aux is not None:
                    product = self.productsList[self.aux]
                    total_sell = product.price_sell * qtd
                    total_buy = product.price_buy * qtd
                    option = input(f"{qtd} unidade/s do produto {product.name} custam {total_sell}. Deseja finalizar a compra d@ {client.name}(S/N)?")
                    if option in "sS":
                        product.qtd = product.qtd - qtd
                        self.saleList.append(Sale(product.id, product.name, qtd, product.price_sell, total_sell, product.provider, product.price_buy, total_buy, client.cpf))
                        for item in range(qtd):
                            self.bestSellerList.append(product.id)
                            self.bestProviderList.append(product.provider)
                        print("Compra realizada!\n") 
                    else:
                        print("Compra cancelada!\n") 
                    self.aux = None
                else:
                    print("Ou esse Produto não existe ou não temos essa quantidade no estoque, consulte a nossa lista de produtos!\n")
            else:
                print("Esse cliente não está cadastrado em nosso sistema, confira a nossa lista!\n")

    #exibir vendas
    def show_sale(self):
        print("\n ~~ Relatórios de Vendas ~~")
        for i in self.saleList:
            print(f"Id:{i.id} Nome:{i.name} Quantidade:{i.qtd} Preço de Venda:R${i.price_sell} Total da Venda:R${i.total_sell} Cliente:{i.cpf} Fornecedor:{i.provider}")

    #exibir caixa
    def show_cashier(self):
        print("\n ~~ Caixa da Empresa ~~")
        for i in self.saleList:
            product = self.saleList[self.saleList.index(i)]
            self.money_spent = self.money_spent + product.total_buy
            self.money_earned = self.money_earned + product.total_sell
            self.cashier = self.money_earned - self.money_spent
        print(f"Total adquirido: R${self.money_earned} Total gasto: R${self.money_spent} Caixa atual: R${self.cashier} ")
        option = input("\nDeseja criar um arquivo externo com as informações do Caixa? ")
        if option in "sS":
            arquivo = open("Caixa.txt", "wt")
            if arquivo:
                print("\nArquivo externo foi criado com sucesso!")
                arquivo.write(f"Total adquirido: R${self.money_earned} Total gasto: R${self.money_spent} Caixa atual: R${self.cashier} ")
            else:
                print("Não foi possível criar o arquivo, tente novamente em breve!\n")
            arquivo.close()
        
    #produto mais vendido
    def best_product(self):
        print("\n ~~ Produto mais vendido ~~")
        max = 0
        keys = defaultdict(list)
        for key, value in enumerate(self.bestSellerList):
            keys[value].append(key)
        for value in keys:
            if len(keys[value]) > max:
                max = len(keys[value]) 
                for i in self.saleList:
                    if value == i.id:
                        name = i.name
        print(f"O produto mais vendido foi: {name}, com um total de {max} vendas!")

    #fornecedor mais escolhido
    def best_provider(self):
        print("\n ~~ Fornecedor mais escolhido ~~")
        max = 0
        keys = defaultdict(list)
        for key, value in enumerate(self.bestProviderList):
            keys[value].append(key)
        for value in keys:
            if len(keys[value]) > max:
                max = len(keys[value]) 
                for i in self.saleList:
                    if value == i.provider:
                        name = i.provider
        print(f"O fornecedor mais escolhido foi: {name}, com um total de {max} vendas feitas através dele!")