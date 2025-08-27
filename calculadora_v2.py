def adicao(a, b):
    return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  if b == 0:
    return 
  else:
    return a / b

def calculadora(num1, num2, operacao):
  operacao = operacao.lower() 
  
  if operacao == 'adicao' or operacao == '+':
    resultado = adicao(num1, num2)
  elif operacao == 'subtracao' or operacao == '-':
    resultado = subtracao(num1, num2)
  elif operacao == 'multiplicacao' or operacao == '*':
    resultado = multiplicacao(num1, num2)
  elif operacao == 'divisao' or operacao == '/':
    resultado = divisao(num1, num2)
  else:
    resultado = "Operação inválida. Por favor, use +, -, *, / ou o nome da operação."
  
  return resultado
saida = ""

while saida.lower() != 'n':
  
  num1_str = input("Digite o primeiro número: ")
  
  num2_str = input("Digite o segundo número: ")
  
  operacao = input("Digite a operação (+, -, *, / ou o nome): ")
  
  try:
    num1 = float(num1_str)
    num2 = float(num2_str)
    
    resultado = calculadora(num1, num2, operacao)
    
    print('Resultado da operação:', resultado)
    
  except ValueError:
    print("Entrada inválida. Por favor, digite números válidos.")
  
  saida = input("Deseja continuar? (S/N): ")