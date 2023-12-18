from sys import getsizeof
"""
Generator Expressions é uma forma mais rápida para listas, dicionários etc.
    - Usa menos memporia alocada
    - Valores em bytes
"""

numbers = [x * 10 for x in range(15)]
print(type(numbers))
print(numbers)
print(getsizeof(numbers))

numbers_generator = (x * 10 for x in range(15))
print(type(numbers_generator))
print(getsizeof(numbers_generator))
print(list(numbers_generator))
