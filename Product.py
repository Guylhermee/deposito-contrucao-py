class Product:
    def __init__(self, id:int, name, qtd:int, price_buy:float, price_sell:float, provider):
        self.id = id
        self.name = name
        self.qtd = qtd
        self.price_buy = price_buy
        self.price_sell = price_sell
        self.provider = provider
