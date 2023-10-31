from src.recipe import Recipe
from src.coffee_maker import CoffeeMaker



class Main:
    def __init__(self,):
        self.coffee_maker = CoffeeMaker()
    
    def menu(self):
        print("================================")
        print("1. Adicionar uma receita")
        print("2. Excluir uma receita")
        print("3. Editar uma receita")
        print("4. Adicionar inventário")
        print("5. Verificar inventário")
        print("6. Fazer café")
        print("0. Sair\n")
        print("================================")

        user_input = input("Digite o número correspondente à ação desejada: ")

        try:
            user_input = int(user_input)
            if 0 <= user_input <= 6:
                if user_input == 1:
                    self.add_recipe()
                elif user_input == 2:
                    self.delete_recipe()
                elif user_input == 3:
                    self.edit_recipe()
                elif user_input == 4:
                    self.add_inventory()
                elif user_input == 5:
                    self.check_inventory()
                elif user_input == 6:
                    self.make_coffee()
                elif user_input == 0:
                    exit(0)
            else:
                print("Por favor, insira um número de 0 a 6.")
                self.menu()
        except ValueError:
            print("Insira um número de 0 a 6.")
            self.menu()

    def add_recipe(self):
        name = input("\nInsira o nome da receita: ")
        price = input("\nInsira o preço da receita: R$")
        coffee = input("\nInsira a quantidade de café na receita: ")
        milk = input("\nInsira a quantidade de leite na receita: ")
        sugar = input("\nInsira a quantidade de açúcar na receita: ")
        chocolate = input("\nInsira a quantidade de chocolate na receita: ")

        recipe = Recipe(name, float(price), int(coffee), int(milk), int(sugar), int(chocolate))
        self.coffee_maker.add_recipe(recipe)

        self.menu()

    def select_recipe(self, message: str):
        selection = input(message)
        recipe_index = None
        
        try:
            recipe_index = int(selection) - 1
            if 0 <= recipe_index < len(self.coffee_maker.get_recipes()):
                return recipe_index
        except:
            print("Selecione uma receita válida")
            return None

    def delete_recipe(self):
        recipes = self.coffee_maker.get_recipes()
        for i, recipe in enumerate(recipes):
            if recipe is not None:
                print(f"{i+1}. {recipe.name}")

        recipe_to_delete = self.select_recipe("Selecione o número da receita a ser excluída: ")

        if recipe_to_delete is None:
            self.menu()

        recipe_deleted = self.coffee_maker.delete_recipe(recipe_to_delete)

        if recipe_deleted is not None:
            print(f"{recipe_deleted} excluído com sucesso.\n")
        else:
            print("A receita selecionada não existe e não pode ser excluída.\n")

        self.menu()

    def edit_recipe(self):
        recipes = self.coffee_maker.get_recipes()
        # print(recipes)
        print('none', self.coffee_maker.get_recipes())
        for i, recipe in enumerate(recipes):
            if recipe is not None:
                print(f"{i+1}. {recipe.name}")

        recipe_to_edit = self.select_recipe("Selecione o número da receita a ser editada: ")

        if recipe_to_edit is None:
            self.menu()

        name = input("\nInsira o nome da receita: ")
        price = input("\nInsira o preço da receita: R$")
        coffee = input("\nInsira a quantidade de café na receita: ")
        milk = input("\nInsira a quantidade de leite na receita: ")
        sugar = input("\nInsira a quantidade de açúcar na receita: ")
        chocolate = input("\nInsira a quantidade de chocolate na receita: ")

        recipe = Recipe(name, float(price), int(coffee), int(milk), int(sugar), int(chocolate))
        edited_recipe = self.coffee_maker.edit_recipe(recipe_to_edit, recipe)

        if edited_recipe:
            print("Receita editada com sucesso.")
        else:
            print("Não foi possível editar a receita")
        
        self.menu()

    def add_inventory(self):
        coffee = int(input("Insira a quantidade de café para adicionar ao inventário: "))
        milk = int(input("Insira a quantidade de leite para adicionar ao inventário: "))
        sugar = int(input("Insira a quantidade de açúcar para adicionar ao inventário: "))
        chocolate = int(input("Insira a quantidade de chocolate para adicionar ao inventário: "))

        self.coffee_maker.add_inventory(coffee, milk, sugar, chocolate)

        self.menu()

    def check_inventory(self):
        print(self.coffee_maker.check_inventory())
        self.menu()

    def make_coffee(self):
        recipes = self.coffee_maker.get_recipes()

        if len(recipes) == 0:
            print("Não existe nenhuma receita cadastrada!")
            self.menu()

        for i, recipe in enumerate(recipes):
            if recipe is not None:
                print(f"{i+1}. {recipe.name}")
    
        recipe_to_purchase = self.select_recipe("Selecione o número da receita a ser comprada: ")

        if recipe_to_purchase is None:
            self.menu()

        try:
            amount_paid = float(input("Insira o valor que deseja pagar: R$"))
        except ValueError:
            print("Insira um número válido")
            self.menu()
        
        change = self.coffee_maker.make_coffee(recipe_to_purchase, amount_paid)

        if change == amount_paid:
            print("Valor insuficiente para compra!")
        else:
            print(f"Obrigada por comprar {self.coffee_maker.get_recipes()[recipe_to_purchase].name}")
        
        if change != 0:
            print(f"Seu troco é: R$ {change}\n")

        self.menu()

if __name__ == "__main__":
    coffee_maker = Main()
    print("Bem-vindo ao CoffeeMaker!\n")
    coffee_maker.menu()
