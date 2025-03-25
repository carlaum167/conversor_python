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
    print("Invalid option!   D:")
    print("Try again?")
    print("1. YES")
    print("2. NO")
    sub_escolha = input("Enter the number of the desired option ")
    if sub_escolha == '1':
        return menu()
    elif sub_escolha == '2':
        print("program closed")
    else:
        print("Invalid option, try again")
        return invalid_option()

#CONTINUATION
def continuation():
    print("___________________________________")
    print("Do you want to return to the menu?")
    print("1. YES")
    print("2. NO")
    sub_escolha = input("Enter the number of the desired option ")
    if sub_escolha == '1':
        return menu()
    elif sub_escolha == '2':
        print("program closed")
    else:
        print("Invalid option, try again!")
        return continuation()


def menu():
  print("Choose the desired option: ")
  print("1. Temperature")
  print("2. Distance")
  print("3. Weight")
  print("4. Bulk")
  escolha = input("Enter the number of the desired operation: ")

  if escolha == '1':
      print("1. Celsius to Fahrenheit")
      print("2. Farenheit to Celsius")
      valor = float(input("Enter the amount to be converted "))
      sub_escolha = input("Enter the desired conversion number ")
      if sub_escolha == '1':
          print(f"{valor}°C is tantamount to {celsius_para_fahrenheit(valor):.2f}°F")
          return continuation()
      elif sub_escolha == '2':
          print(f"{valor}°F is tantamount to {fahrenheit_para_celsius(valor):.2f}°C")
          return continuation()
      else:
          return invalid_option()

  elif escolha == '2':
      print("1. Kilometers to Miles")
      print("2. Miles to Kilometers")
      valor = float(input("Enter the amount to be converted "))
      sub_escolha = input("Enter the desired conversion number ")
      if sub_escolha == '1':
          print(f"{valor} KM is tantamount to {km_para_milha(valor):.2f} miles")
          return continuation()
      elif sub_escolha == '2':
          print(f"{valor} miles is tantamount to {milha_para_km(valor):.2f} KM")
          return continuation()
      else:
          return invalid_option()

  elif escolha == '3':
      print("1. Kilos to Pounds")
      print("2. Pounds to Kilos")
      valor = float(input("Enter the amount to be converted "))
      sub_escolha = input("Enter the desired conversion number ")
      if sub_escolha == '1':
          print(f"{valor}KG is tantamount to {kg_para_libras(valor):.2f} pounds")
          return continuation()
      elif sub_escolha == '2':
          print(f"{valor} pounds is tantamount to {libras_para_kg(valor):.2f}KG")
          return continuation()
      else:
          return invalid_option()

  elif escolha == '4':
      print("1. Liters to Gallons")
      print("2. Gallons to Liters")
      valor = float(input("Enter the amount to be converted "))
      sub_escolha = input("Enter the desired conversion number ")
      if sub_escolha == '1':
          print(f"{valor} liters is tantamount to {litros_para_galoes(valor):.2f} gallons")
          return continuation()
      elif sub_escolha == '2':
          print(f"{valor} gallons is tantamount to {galoes_para_litros(valor):.2f} liters")
          return continuation()
      else:
          return invalid_option()

  else:
      return invalid_option()


if __name__ == "__main__":
    menu()

