import random
from time import sleep

respostas = ["Sim, vai lá!", "Melhor não!", "Talvez...", "Com certeza!", "Acho que não.",
                 "Por que não?", "Claro!", "Definitivamente não.", "Tente outra vez.", "Sem dúvidas!",
                 "Depende.", "Com toda certeza!", "Nem pense nisso.", "A resposta está no seu coração.",
                 "Pergunte de novo mais tarde.", "Não posso dizer agora.", "Se eu fosse você, sim!",
                 "Não vejo por que não.", "Pode ser.", "Só se for agora!"]

print("  ====   BEM-VINDO(A) AO ÓRACULO  ====")

while True:
    print('''
                  [ 1 ] Fazer uma pergunta
                  [ 2 ] Sair
                  ''')
    escolha = int(input("O que deseja ? "))
    if escolha == 1:
        pergunta = str(input("Faça a sua pergunta: \n"))
        resposta = random.choice(respostas)
        sleep(2)
        print("HUMM..ESTOU PENSANDO")
        sleep(2)
        print(resposta)
    elif escolha == 2:
        print("FIM DO PROGRAMA!!")
