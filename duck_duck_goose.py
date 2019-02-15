def duckduckgoose(numero,lista):
    for i in range(lista):
        if i==numero:
            return lista[i]
        else:
            continue
lista=["carlos","gonzalo","helena","pablo","sara","lucia"]
jugador = duckduckgoose(4,lista)
print(jugador)
