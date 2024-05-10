idade = int(input("Informe sua idade: \n"))

if idade >= 18:
    print("Permitido!")
else:
    print("Negado!")

salario = float(input("Digite o seu salário: \n"))

if salario <= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador Senior")
else:
    print("Gerente de Projetos")