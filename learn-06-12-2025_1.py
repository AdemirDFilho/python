#https://www.learnpython.org/pt/String_Formatting

""" Você precisará escrever uma string de formatação que imprima os dados usando a seguinte sintaxe: 
Hello John Doe. Your current balance is $53.44. """


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

#print("%s %s %s. Your current balance is $%f" % (format_string, data))

#print("%s" % data)

#print("a variavel é %s" % (format_string))

#print(type(data))