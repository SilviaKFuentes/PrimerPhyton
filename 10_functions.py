###Functions###

def my_function ():
    print("Esto es una función")
  
my_function()
my_function()
my_function()

# Función que suma dos valores y los imprime
def sum_two_values(first_value: int, second_value: int):
    print(first_value + second_value)

# Llamadas a la función
sum_two_values(5, 7)            # Enteros → imprime 12
sum_two_values(54754, 71231)    # Números grandes → imprime 125985
sum_two_values("5", "7")        # Cadenas → imprime "57" (concatenación)
sum_two_values(1.4, 5.2)        # Flotantes → imprime 6.6


# Función que suma dos valores y retorna el resultado
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value


my_result = sum_two_values_with_return(10 , 5)
print(my_result)