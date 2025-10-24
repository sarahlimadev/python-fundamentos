# 6. Faça uma função que recebe uma temperatura em Celsius e retorna Fahrenheit e Kelvin (retorno múltiplo!)
def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return (fahrenheit, kelvin)

print(converter_temperatura(25))