# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  
  if consumo < 0:
    return 'Consumo inválido. Insira um valor positivo.'
    
  elif consumo < 10:
    return 'Plano Essencial Fibra - 50Mbps'
  
  elif consumo < 20:
    return 'Plano Prata Fibra - 100Mbps'
  
  else:
    return 'Plano Premium Fibra - 300Mbps'
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

try:
  # Solicita ao usuário que insira o consumo médio mensal de dados:
  consumo = float(input('Insira um valor: '))
  # Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
  
  print(recomendar_plano(consumo))
  
except ValueError:
  print('Valor inserido inválido, favor insira um número positivo.')