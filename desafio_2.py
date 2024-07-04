itens = []
contador = 0

while contador < 3:
  
   item = input("Informe o equipamento (limite de 3 itens): ")
   
   itens.append(item)
   
   contador += 1
  
print("Lista de Equipamentos:")  
for item in itens:
    
    print(f"- {item}")
    