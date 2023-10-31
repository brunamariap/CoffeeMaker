from .recipe import Recipe


class Inventory:

    def __init__(self, coffee = 0, milk = 0, sugar = 0, chocolate = 0):
        self.coffee= coffee
        self.milk = milk
        self.sugar = sugar
        self.chocolate = chocolate

    def add_coffee(self, quantity=1):
        self.coffee += quantity
    
    def add_milk(self, quantity=1):
        self.milk += quantity

    def add_sugar(self, quantity=1):
        self.sugar += quantity

    def add_chocolate(self, quantity=1):
        self.chocolate += quantity

    def enough_ingredients(self, recipe: Recipe):
        if self.coffee < recipe.amount_coffee:
            return False
        
        if self.milk < recipe.amount_milk:
            return False

        if self.sugar < recipe.amount_sugar:
            return False
        
        if self.chocolate < recipe.amount_chocolate:
            return False
        
        return True
    
    def use_ingredients(self, recipe: Recipe):
        if self.enough_ingredients(recipe):
            self.coffee -= recipe.amount_coffee
            self.milk -= recipe.amount_milk
            self.sugar -= recipe.amount_sugar
            self.chocolate -= recipe.amount_chocolate

            return True
        print("Ingredientes insuficientes")
        return False

    def __str__(self) -> str:
        return f"""===================
                \nCoffee: {self.coffee} 
                \nMilk: {self.milk} 
                \nSugar: {self.sugar} 
                \nChocolate: {self.chocolate} 
                \n==================="""

