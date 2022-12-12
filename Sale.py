from Product import Product

class Sale:
    def __init__(self, id:int, name, qtd:int, price_sell:float, total_sell:float, provider, price_buy:float, total_buy:float, cpf:int):
        self.id = id
        self.name = name
        self.qtd = qtd
        self.price_sell = price_sell
        self.total_sell = total_sell
        self.provider = provider
        self.price_buy = price_buy
        self.total_buy = total_buy
        self.cpf = cpf
        
