from Handler import Handler

class Deposito:
    #construtor
    def __init__(self):
        self.listaux = []

    #menu principal
    def main(self):
        while True:
            print(" ~ DEPÓSITO DE CONSTRUÇÃO ~")
            print("1 - Atendimento ao Cliente \n2 - Produtos \n3 - Setor de Vendas \n0 - Sair")
            self.option = int(input("Selecione uma opção:"))

            if self.option == 0:
                print("Volte sempre! :)")
                break
            elif self.option == 1:
                self.viewClientOptions()
            elif self.option == 2:
                self.viewProductsOptions() 
            elif self.option == 3:
                self.viewSaleOptions()
    
    #menu dos clientes        
    def viewClientOptions(self):
        handler = Handler()
        while True:
            print("\n ~ Atendimento ao Cliente ~")
            print("1 - Criar Cliente \n2 - Exibir Clientes \n3 - Remover Cliente \n4 - Editar Cliente \n5 - Adicionar Clientes Testes \n0 - Sair")
            self.option = int(input("Selecione uma opção:"))

            if self.option == 0:
                print("")
                self.main()

            elif self.option == 1:
                handler.add_clients(int(input("\nDigite o ID do novo cliente:")), input("\nDigite o nome do cliente:"), int(input("\nDigite os números do CPF:")))
            
            elif self.option == 2:
                handler.show_clients()

            elif self.option == 3:
                handler.remove_clients(int(input("Digite o ID do cliente que será removido:\n")))
            
            elif self.option == 4:
                handler.edit_clients(int(input("Digite o ID do cliente que terá os dados alterados:\n")))
            
            elif self.option == 5:
                handler.add_mock_clients()   

    #menu dos produtos        
    def viewProductsOptions(self):
        handler = Handler()
        while True:
            print("\n ~ Produtos ~")
            print("1 - Adicionar Produto \n2 - Exibir Estoque de Produtos \n3 - Exibir Estoque de Fornecedores \n4 - Remover Produtos \n5 - Editar Produtos \n6 - Adicionar Produtos Testes \n0 - Sair")
            self.option = int(input("Selecione uma opção:"))

            if self.option == 0:
                break

            elif self.option == 1:
                handler.add_products(int(input("\nDigite o ID do novo produto:")), input("\nDigite o nome do produto:"), int(input("\nDigite a quantidade de produtos:")), float(input("\nDigite o preço de compra do produto:")), float(input("\nDigite o preço de venda do produto:")), input("\nDigite o nome do fornecedor (se for a própria loja, digite 'Loja'):"))
            
            elif self.option == 2:
                handler.show_products()

            elif self.option == 3:
                handler.show_products_f()
        
            elif self.option == 4:
                handler.remove_products(int(input("Digite o ID do produto que será removido:\n")))
            
            elif self.option == 5:
                handler.edit_products(int(input("Digite o ID do produto que terá os dados alterados:\n")))
  
            elif self.option == 6:
                handler.add_mock_products()   

    #menu de vendas
    def viewSaleOptions(self):
        handler = Handler()
        while True:
            print("\n ~ Setor de Vendas ~")
            print("1 - Vender Produto \n2 - Exibir relatório de todos os itens vendidos \n3 - Caixa \n0 - Sair")
            self.option = int(input("Selecione uma opção:"))

            if self.option == 0:
                break

            elif self.option == 1:
                handler.sale(int(input("\nDigite o cpf do cliente que irá realizar a compra:")), int(input("\nDigite o ID do produto que deseja vender:")), int(input("\nDigite a quantidade de produtos:")))

            elif self.option == 2:
                handler.show_sale()
            
            elif self.option == 3:
                handler.show_cashier() 

            elif self.option == 4:
                handler.show_products()
  
m = Deposito()
m.main()