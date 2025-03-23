def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_para_milha(km):
    return km * 0.621371

def milha_para_km(milha):
    return milha / 0.621371

def kg_para_libras(kg):
    return kg * 2.20462

def libras_para_kg(libras):
    return libras / 2.20462

def litros_para_galoes(litros):
    return litros * 0.264172

def galoes_para_litros(galoes):
    return galoes / 0.264172

def menu():
  print("Escolha o tipo de conversão desejada:")
  print("1. Temperatura")
  print("2. Distância")
  print("3. Peso")
  print("4. Volume")
  escolha = input("Digite o número da operação desejada: ")

  if escolha == '1':
      print("1. Celsius para Fahrenheit")
      print("2. Farenheit para Celsius")
      sub_escolha = input("Digite o numero da opção desejada ")
      valor = float(input("Digite o valor a ser convertido "))
      if sub_escolha == '1':
          print(f"{valor}°C é equivalente a {celsius_para_fahrenheit(valor):.2f}°F")
      elif sub_escolha == '2':
          print(f"{valor}°F é equivalente a {fahrenheit_para_celsius(valor):.2f}°C")
