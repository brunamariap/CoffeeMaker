class Recipe:
    def __init__(self, name: str, price: float, amount_coffee: int, amount_milk: int, amount_sugar: int, amount_chocolate: int):

        self.name: str = name
        self.price: float = price
        self.amount_coffee: int = amount_coffee
        self.amount_milk: int = amount_milk
        self.amount_sugar: int = amount_sugar
        self.amount_chocolate: int = amount_chocolate

        self.verify()

    def verify(self):
        if not isinstance(self.name, str):
            return False
        if not isinstance(self.price, float):
            return False
        if not isinstance(self.amount_coffee, int) or not isinstance(self.amount_milk, int) or not isinstance(self.amount_sugar, int) or not isinstance(self.amount_chocolate, int):
            return False
        
        return True
