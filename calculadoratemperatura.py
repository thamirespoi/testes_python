## Calculadora de conversão de temperatura:

# Celsius para Farenheit: celsius * 1.8 + 32
# Celsius para Kelvin: celsius + 273.13

print("========================================================")
print("========= CALCULADORA CONVERSÃO DE TEMPERATURA =========")
print("========================================================")

temperaturaCelsius = float(input("Qual a temperaturaCelsius?"))

temperaturaKelvin = temperaturaCelsius + 273.15 
temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32

print("========================================================")
print(f"A temperatura em Celsius convertida em Kelvin é {temperaturaKelvin}.")
print(f"A temperatura em Celsius convertida em Fahrenheit é {temperaturaFahrenheit}.")
      
