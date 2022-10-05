#crear funciones
#llamarlas
#varios argumentos
#Argumentos variables *args
#Argumentos variables de llave valor **kwargs

# def dinamic_add(*args):
#     #print(args, type(args))
#     add=0
#     for i in args:
#         add+=i
#     return add


# print(dinamic_add(9, 9, 9, 9, 9))

payload = {
    'title': 'Calladita', 
    'artist': 'Bad bunny', 
    'album': 'quien sabe', 
    'genre': 'arte', 
}

def favorite_song(**songs):

    title = songs['data']['title']
    artist = songs['data']['artist']
    # album = songs['data']['album']

    return f'the song is {title} for {artist}'

print(favorite_song(data=payload))