import random
from os import system, name


def limpa_tela():
    if name == 'nt':  # Windows
        _ = system('cls')
    else:  # Linux/Mac
        _ = system('clear')


def game():
    limpa_tela()
    print('Bem-vindo ao jogo da forca!')
    print('Adivinhe a palavra')

    palavras = ['banana', 'uva', 'abacate', 'morango', 'laranja']
    palavra = random.choice(palavras)  # Escolhe uma palavra aleatória

    letras_descobertas = ['_' for letra in palavra]

    chance = 6
    letras_erradas = []

    while chance > 0:
        print(''.join(letras_descobertas))
        print('\nChances Restantes:', chance)
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print('Por favor, digite apenas uma letra válida.')
            continue

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chance -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            limpa_tela()
            print("\nVocê venceu! A palavra era:", palavra)
            break

    if chance == 0:
        print("\nVocê perdeu! A palavra era:", palavra)


if __name__ == '__main__':
    game()