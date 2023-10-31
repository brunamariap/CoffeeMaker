from .recipe_book import RecipeBook
from .inventory import Inventory


class CoffeeMaker:

    def __init__(self):
        self.recipe_book = RecipeBook()
        self.inventory = Inventory()

    def get_recipes(self):
        return self.recipe_book.get_recipes()

    def add_recipe(self, recipe):
        self.recipe_book.add_recipe(recipe)

    def delete_recipe(self, recipe_index):
        self.recipe_book.delete_recipe(recipe_index)

    def edit_recipe(self, recipe_index, new_recipe):
        self.recipe_book.edit_recipe(recipe_index, new_recipe)

    def add_inventory(self, coffee, milk, sugar, chocolate):
        self.inventory.add_coffee(coffee)
        self.inventory.add_milk(milk)
        self.inventory.add_sugar(sugar)
        self.inventory.add_chocolate(chocolate)

    def check_inventory(self):
        return self.inventory

    def make_coffee(self, recipe_index, amount_paid):
        recipe = self.get_recipes()[recipe_index]

        if not recipe:
            return amount_paid

        if recipe.price <= amount_paid:
            if self.inventory.use_ingredients(recipe):
                return amount_paid - recipe.price
            
        return amount_paid
