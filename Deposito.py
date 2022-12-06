from Client import Client
#from Options.MovieOptions import MovieOptions
#from Options.CashOptions import CashOptions


class Deposito:
    def __init__(self):
        self.clientsList = []

    def main(self):
        while True:
            print(" ~ DEPÓSITO DE CONSTRUÇÃO ~")
            print("1 - Atendimento ao Cliente \n0 - Sair")
            self.option = int(input("Selecione uma opção:"))

            if self.option == 0:
                break
            elif self.option == 1:
                self.viewClientOptions()
            
    def viewClientOptions(self):
        print(" ~ Atendimento ao Cliente ~")
        print("1 - Criar Cliente \n2 - Exibir Clientes")
        self.option = int(input("Selecione uma opção:"))

        if self.option == 1:
            self.add_clients(input("Digite o nome do cliente:\n"), int(input("Digite os números do CPF:\n")))
        
        elif self.option == 2:
            self.show_clients()

    def add_clients(self, name, cpf):
        self.clientsList.append(Client(cpf, name))
        print("Cliente cadastrado com sucesso.\n")

    def show_clients(self):
        for i in self.clientsList:
            print(f"{i.cpf} - {i.name}")


m = Deposito()
m.main()