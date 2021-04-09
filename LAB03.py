from random import choice
lista = ['''
+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

print('''
>>>>>>>>>>Jogo da forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''')

erros = 0
palavras = ['massa', 'casa', 'bola']
escolher = choice(palavras)
caracters = len(escolher)
word = [row for row in escolher]
print("_"*caracters)

while True:
    letra = str(input('Digite uma letra:'))
    if letra not in word:
        erros += 1
        print("errou")
        print(lista[0])
    if letra in word:
        print(letra)

    if erros == 6:
        print("Game over! Você perdeu.")
        break