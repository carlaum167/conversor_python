#TEMPERATURE
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
#DISTANCE
def km_para_milha(km):
    return km * 0.621371

def milha_para_km(milha):
    return milha / 0.621371
#WEIGHT
def kg_para_libras(kg):
    return kg * 2.20462

def libras_para_kg(libras):
    return libras / 2.20462
#BULK
def litros_para_galoes(litros):
    return litros * 0.264172

def galoes_para_litros(galoes):
    return galoes / 0.264172
#INVALID OPTION
def invalid_option():
    print("Opção invalida!   D:")
    print("Deseja tentar novamente?")
    print("1. SIM")
    print("2. NÃO")
    sub_escolha = input("Digite o numero da opção desejada ")
    if sub_escolha == '1':
        return menu()
    elif sub_escolha == '2':
        print("programa encerrado")

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
      elif sub_escolha != '1' or '2':
          return invalid_option()

  elif escolha == '2':
      print("1. Quilômetros para Milhas")
      print("2. Milhas para Quilômetros")
      sub_escolha = input("Digite o numero da opção desejada ")
      valor = float(input("Digite o valor a ser convertido "))
      if sub_escolha == '1':
          print(f"{valor} KM é equivalente a {km_para_milha(valor):.2f} milhas")
      elif sub_escolha == '2':
          print(f"{valor} milhas é equivalente a {milha_para_km(valor):.2f} KM")
      elif sub_escolha != '1' or '2':
          return invalid_option()

  elif escolha == '3':
      print("1. Quilos para Libras")
      print("2. Libras para Quilos")
      sub_escolha = input("Digite o numero da opção desejada ")
      valor = float(input("Digite o valor a ser convertido "))
      if sub_escolha == '1':
          print(f"{valor}KG é equivalente a {kg_para_libras(valor):.2f} libras")
      elif sub_escolha == '2':
          print(f"{valor} libras é equivalente a {libras_para_kg(valor):.2f}KG")
      elif sub_escolha != '1' or '2':
          return invalid_option()


  elif escolha == '4':
      print("1. Litros para galões")
      print("2. Galões para litros")
      sub_escolha = input("Digite o numero da opção desejada ")
      valor = float(input("Digite o valor a ser convertido "))
      if sub_escolha == '1':
          print(f"{valor} litros é equivalente a {litros_para_galoes(valor):.2f} galões")
      elif sub_escolha == '2':
          print(f"{valor} litros é equivalente a {galoes_para_litros(valor):.2f} litros")
      elif sub_escolha != '1' or '2':
          return invalid_option()

  else:
      return invalid_option()


if __name__ == "__main__":
    menu()

