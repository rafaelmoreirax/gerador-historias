import random

def gerar_historia():
    personagens = ["um dragão", "uma princesa", "um pirata", "um astronauta", "um robô"]
    lugares = ["na floresta encantada", "no espaço sideral", "em uma ilha deserta", "no castelo antigo", "na cidade futurista"]
    objetivos = ["encontrar um tesouro", "salvar o mundo", "descobrir um segredo", "vencer uma batalha", "fazer um novo amigo"]
    complicacoes = ["enfrentando monstros", "lutando contra o tempo", "desvendando enigmas", "escapando de armadilhas", "superando medos"]

    personagem = random.choice(personagens)
    lugar = random.choice(lugares)
    objetivo = random.choice(objetivos)
    complicacao = random.choice(complicacoes)

    historia = (
        f"Certa vez, {personagem} estava {lugar}, com a missão de {objetivo}. "
        f"No caminho, ele/ela ficou {complicacao} e teve que usar toda sua coragem para continuar."
    )
    return historia

def main():
    print("=== Gerador de Histórias Aleatórias ===")
    while True:
        input("Pressione ENTER para gerar uma história ou digite 'sair' para encerrar: ")
        historia = gerar_historia()
        print(f"\n📖 {historia}\n")
        comando = input("Quer outra história? (ENTER para sim / 'sair' para não): ").strip().lower()
        if comando == 'sair':
            print("Até a próxima! Continue criando histórias incríveis!")
            break

if __name__ == "__main__":
    main()
