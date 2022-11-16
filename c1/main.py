import random

options         = ("piedra","papel","tijera")

computer_wins   =0
user_wins       =0
rounds          =1

while True:

    print('*'*10)
    print('Round',rounds)
    print('*'*10)
    print('Puntuacion usuario 🧑', user_wins)
    print('Puntuacion computador 💻', computer_wins)

    user_option     = input("piedra, papel o tijera => ")
    user_option     = user_option.lower()
    computer_option = random.choice(options)

    if not user_option in options:
        print("Esa no es una opcion valida 😪")
        continue

    print("Opcion del Usuario: ", user_option)
    print("Opcion del Ordenador: ", computer_option)

    if (user_option == computer_option):
        print("Esto es un empate 🤔")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("Usuario gana 🧑")
            user_wins +=1
        else:
            print("piedra gana a tijera")
            print("computador gana 💻")
            computer_wins +=1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("Usuario gana 🧑")
            user_wins +=1
        else:
            print("tijera gana a papel")
            print("computador gana 💻")
            computer_wins +=1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("Usuario gana 🧑")
            user_wins +=1
        else:
            print("piedra gana a tijera")
            print("computador gana 💻")
            computer_wins +=1

    if computer_wins==2:
        print("Esta partida la ha ganado el computador 💻 🎉🎊🥇🏆")
        break

    if user_wins==2:
        print("Esta partida la ha ganado el Usuario 🧑 🎉🎊🥇🏆")
        break

    rounds+=1





