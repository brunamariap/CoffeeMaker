from .recipe import Recipe


class RecipeBook:

    def __init__(self):
        self.recipes = [] 
        self.max_recipes = 3

    def get_recipes(self):
        return self.recipes

    def add_recipe(self, recipe: Recipe):
        if len(self.recipes) == self.max_recipes:
            return False

        if recipe in self.recipes:
            return False

        self.recipes.append(recipe)
        return True

    def delete_recipe(self, recipe_to_delete):
        if recipe_to_delete < 0 or recipe_to_delete >= len(self.recipes):
            return None

        if self.recipes[recipe_to_delete] is not None:
            recipe_name = self.recipes[recipe_to_delete].name
            self.recipes.pop(recipe_to_delete)
            print(f"Receita: {recipe_name} deletada com sucesso")
            return True

    def edit_recipe(self, recipe_to_edit, new_recipe):
        if recipe_to_edit < 0 or recipe_to_edit >= len(self.recipes):
            return None

        if self.recipes[recipe_to_edit] is not None:
            recipe_name = self.recipes[recipe_to_edit].name
            self.recipes[recipe_to_edit] = new_recipe
            print(f"Receita: {recipe_name} editada com sucesso")
            return True
        else:
            return None
