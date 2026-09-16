#this code is a simple example of a Python script that prints "Hello, World!" to the console.
print ("hello world")

ingredients = ["flour", "sugar", "butter", "eggs", "milk"]

if "sugar" in ingredients and "flour" in ingredients:
    print ("Sugar and flour are in the ingredients list.")
else:
    print ("Either sugar or flour is missing from the ingredients list.")


#this function checks if the essential ingredients for making a cake are present in the provided list of ingredients. If they are, it prints a message indicating that a cake can be made and lists the ingredients. If not, it informs the user that essential ingredients are missing.
def make_cake(ingredients):
    if "flour" in ingredients and "sugar" in ingredients and "eggs" in ingredients:
        print("Making a cake with the following ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
    else:
        print("Cannot make a cake. Missing essential ingredients.")

# Example usage of the make_cake function
make_cake(ingredients)

