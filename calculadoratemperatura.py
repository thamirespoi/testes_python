## Calculadora de conversão de temperatura:

print("========================================================")
print("======= CALCULADORA DE CONVERSÃO DE TEMPERATURA ========")
print("========================================================")

temperaturaCelsius = float(input("Qual a temperaturaCelsius?"))

temperaturaKelvin = temperaturaCelsius + 273.15 
temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32

print("========================================================")
print(f"A temperatura em Celsius convertida em Kelvin é {temperaturaKelvin}.")
print(f"A temperatura em Celsius convertida em Fahrenheit é {temperaturaFahrenheit}.")
      
