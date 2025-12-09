#https://www.learnpython.org/pt/Functions

# Defina nossas 3 funções
""" def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# printa uma saudação simples
my_function()

# prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# após esta linha x terá o valor 3!
x = sum_two_numbers(1,2) """

#######################################

""" Exercício

Neste exercício, você usará uma função existente e adicionará a sua própria para criar um programa totalmente funcional.

    Adicione uma função chamada list_benefits() que retorna a seguinte lista de strings: "Mais código organizado", "Código mais legível", "Reutilização de código mais fácil", "Permitindo que os programadores compartilhem e conectem código juntos"

    Adicione uma função chamada build_sentence(info) que recebe um único argumento contendo uma string e retorna uma sentença começando com a string fornecida e terminando com a string " é um benefício das funções!"

    Execute e veja todas as funções trabalhando juntas! """

""" # Modify this function to return a list of strings as defined above
def list_benefits():
    return "Mais código organizado", "Código mais legível", "Reutilização de código mais fácil", "Permitindo que os programadores compartilhem e conectem código juntos"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions() """


##################################################################################################

#https://www.learnpython.org/pt/Classes_and_Objects

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "conversível"
car1.color = "vermelho"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "azul"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())