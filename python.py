nome = input("Digite o nome do atleta: ")
ListaDeNotas = []
for i in range (7):
    numero = int(input('digite uma nota: '))
    if numero != 0:
        ListaDeNotas.append(numero)
    else:
        loop = False
minimo = min(ListaDeNotas)
maximo = max(ListaDeNotas)
if (minimo and maximo in ListaDeNotas):
    ListaDeNotas.remove(minimo)
    ListaDeNotas.remove(maximo)
soma = sum(ListaDeNotas) 
media = soma/5
print ("A nota final foi de: {} para o atleta: {}" .format(media, nome))
