valor = int(input('Insira um valor inteiro: '))


while par <= valor:
  
  par = (valor % 2 == 0)
  soma = valor + par

print(f'A soma dos valores é de {soma}')