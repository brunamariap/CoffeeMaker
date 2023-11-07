""" 
Testes baseados no documento de casos de teste: https://docs.google.com/spreadsheets/d/16OIwhYM6lyx9oiZnHXHeXsJN3qBCzDr8/edit#gid=1792693487
"""

from src.coffee_maker import CoffeeMaker
from src.recipe import Recipe
import pytest


class TestCoffeeMaker:

    @pytest.fixture
    def setUp(self):
        coffee_maker = CoffeeMaker()

        return coffee_maker

    def test_add_valid_recipe(self, setUp):
        recipe = Recipe('Café', 2.0, 3, 4, 5, 2)

        assert setUp.add_recipe(recipe) == True

    def test_invalid_recipe(self, setUp):
        recipe = Recipe('Café test', '10', 9, 3, '2', 2)

        assert setUp.add_recipe(recipe) == False

    def test_edit_recipe(self, setUp):
        recipe = Recipe('Café', 2.0, 3, 4, 5, 2)
        setUp.add_recipe(recipe)
        edited_recipe = Recipe("Café editado", 3.0, 9, 8, 7, 1)

        assert setUp.edit_recipe(0, edited_recipe) == True

    def test_edit_non_exists_recipe(self, setUp):
        edited_recipe = Recipe("Café editado", 3.0, 9, 8, 7, 1)

        assert setUp.edit_recipe(4, edited_recipe) == False

    def test_delete_recipe(self, setUp):
        recipe = Recipe('Café', 2.0, 3, 4, 5, 2)
        setUp.add_recipe(recipe)

        assert setUp.delete_recipe(0) == True
    
    def test_delete_non_exists_recipe(self, setUp):
        assert setUp.delete_recipe(4) == False

    def test_add_inventory(self, setUp):
        assert setUp.add_inventory(10, 10, 10, 10) == True

    def test_make_coffe_not_enough_ingredients(self, setUp):
        recipe = Recipe('Café', 2.0, 3, 4, 5, 2)
        setUp.add_recipe(recipe)
        setUp.add_inventory(10, 10, 10, 1)

        amount_paid = 10.0
        assert setUp.make_coffee(0, amount_paid) == 10.0 # Deve retornar o valor que foi pago, pois o pedido não pode ser realizado

    def test_no_enoungh_money(self, setUp):
        recipe = Recipe('Café', 2.0, 3, 4, 5, 2)
        setUp.add_recipe(recipe)
        setUp.add_inventory(10, 10, 10, 10)

        amount_paid = 1.0
        assert setUp.make_coffee(0, amount_paid) == 1.0 # Valor devolvido, pois não foi feito o pedido

    def test_enoungh_money(self, setUp):
        recipe = Recipe('Café', 2.0, 3, 4, 5, 2)
        setUp.add_recipe(recipe)
        setUp.add_inventory(10, 10, 10, 10)

        amount_paid = 10.0
        assert setUp.make_coffee(0, amount_paid) == 8.0 # Retorna o troco
