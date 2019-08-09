#   Una función mas_largo(palabras), cuyo parámetro palabras es una lista de strings, que entregue cuál es el string más largo:
def mas_largo(palabras):
        largo_palabras = []
        for palabra in palabras:
                largo_palabras.append((len(palabra), palabra)) # se agrega el largo y la palabra de cada palabra en una lista.
                largo_palabras.sort() # se ordenan las listas según su largo de menor a mayor.
        print(largo_palabras[-1][1]) # se imprime la palabra más larga, seleccionando el último índice y la palabra correspondiente.


mas_largo(['raton', 'hipopotamo', 'buey', 'jirafa'])
mas_largo(['****', '**', '********', '**'])