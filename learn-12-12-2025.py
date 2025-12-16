#https://www.learnpython.org/pt/Exception_Handling

""" # Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name(): 
    return actor["last_name"]

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name()) """

# Exercício Trate todas as exceções! Pense nas lições anteriores para retornar o sobrenome do ator.

""" actor = {"name": "John Cleese", "rank": "awesome"}
x = actor["name"]
print(x)
y = x.split(" ")
print(y)
print(type(y))
print(y[1])
z = y[1]
print(z) """

#minha tentativa de resposta = FALHA

""" # Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name(): 
    for i in actor:
        x = actor["name"]
        y = x.split(" ")
        z = y(1)
        except IndexError : 
            
        return z

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name()) """

#______________________SOLUÇÃO__________________

actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    return actor["name"].split()[1]

get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())