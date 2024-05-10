notas = []

for x in range (5):
    codigo_aluno = input("RM: \n")
    nota = float(input("Nota: \n"))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("Qunatidade de notas: ", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("0 RM", codigo_aluno, "tirou nota: ", nota)
