soma = 0
menorNota = 1000
maiorNota = 0
for x in range(7): 
    nota = float(input("digite uma nota: "))
    if nota < menorNota:
        menorNota = nota
    elif nota > maiorNota:
        maiorNota = nota
    soma = soma + nota
media = ((soma - menorNota - maiorNota) /5) 
print(media)