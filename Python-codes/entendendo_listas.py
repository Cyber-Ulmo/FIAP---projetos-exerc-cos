#criação de listas vazias
lista = []
print(type(lista))
#criação de listas com dados
lista = [1977, 1980, 1983, 1999, 2002, 2005]
#exibição da lista completa
print(lista)
#exibição de uma posição específica da lista
print(lista[3])
#exibição de intervalos na lista
print(lista[1:3])
#iteração da lista
for ano in lista:
    print(ano)
#inclusão de dados na última posição da lista
lista.append(2015)
print(lista)
#inclusão de dados em um índice específico da lista
lista.insert(1, 6000)
print(lista)
#remoção de um elemento em uma posição específica
lista.pop(1)
print(lista)
#remoção do último elemento da lista
lista.pop()
print(lista)
#remoção de um valor específico da lista
lista.remove(1999)
print(lista)
#contagem de um determinado elemento na da lista
print(lista.count(1977))
#inversão da lista
lista.reverse()
print(lista)
#ordenação da lista
lista.sort()
print(lista)
#contagem de elementos da lista
print(len(lista))