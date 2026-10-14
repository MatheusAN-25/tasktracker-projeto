"""TaskTracker - aplicação CLI para cadastro e visualização de tarefas.

Autor: Matheus Andrade Naves
Bootcamp II - Fase 2 (Entrega Intermediária)

Implementa a "receita lógica" e as regras de negócio do Planejamento (Fase 1):
  1. Obrigatoriedade: o título não pode ficar vazio.
  2. Restrição de valores: prioridade só aceita Alta, Média ou Baixa.
  3. Validação de data: não é possível cadastrar vencimento no passado.
"""

from datetime import date, datetime

PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

FORMATO_DATA = "%d/%m/%Y"

tarefas = []


def solicitar_titulo():
    """Passos 1-3 do cadastro: pede o título até que não esteja em branco."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar em branco.")


def solicitar_prioridade():
    """Passo 4 do cadastro: pede a prioridade até ser Alta, Média/Media ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Erro: prioridade inválida. Use Alta, Média (ou Media) ou Baixa.")


def solicitar_data_vencimento():
    """Pede a data de vencimento (DD/MM/AAAA) e bloqueia datas no passado."""
    while True:
        entrada = input("Data de vencimento (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, FORMATO_DATA).date()
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA (ex.: 25/12/2026).")
            continue
        if data < date.today():
            print("Erro: a data de vencimento não pode estar no passado.")
            continue
        return data.strftime(FORMATO_DATA)


def exibir_menu():
    print("\n=== TASKTRACKER ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def cadastrar_tarefa():
    print("\n--- Cadastrar nova tarefa ---")
    titulo = solicitar_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = solicitar_prioridade()
    data_limite = solicitar_data_vencimento()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def listar_tarefas():
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Você não tem nenhuma tarefa pendente hoje!")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {i}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Vencimento:  {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")


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