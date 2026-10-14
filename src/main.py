"""TaskTracker - versão inicial: menu e loop principal (ainda sem validações)."""

tarefas = []


def exibir_menu():
    print("\n=== TASKTRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def cadastrar_tarefa():
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição (opcional): ")
    prioridade = input("Prioridade (Alta, Média ou Baixa): ")
    data_limite = input("Data de vencimento (DD/MM/AAAA): ")
    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    })
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas():
    if not tarefas:
        print("\nVocê não tem nenhuma tarefa pendente hoje!")
        return
    for i, t in enumerate(tarefas, start=1):
        print(f"\nTarefa {i}")
        print(f"  Título: {t['titulo']}")
        print(f"  Descrição: {t['descricao']}")
        print(f"  Prioridade: {t['prioridade']}")
        print(f"  Vencimento: {t['data_limite']}")
        print(f"  Status: {t['status']}")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
