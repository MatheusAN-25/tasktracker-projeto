# TaskTracker

Aplicação de linha de comando (CLI) em Python para organizar tarefas do dia a dia:
cadastro com prioridade e data de vencimento, e visualização da lista de pendências.
Empacotada com **Docker** para rodar de forma idêntica em qualquer ambiente.

Projeto do **Bootcamp II — Engenharia de Software** (Fase 3: Entrega Final).

- **Autor:** Matheus Andrade Naves
- **Curso:** Ciência de Dados e Machine Learning — Campus Asa Norte

## Problema e solução

Anotações em papel e mensagens dispersas levam ao esquecimento de prazos e à falta de
priorização. O TaskTracker centraliza as pendências em um sistema simples: o usuário
cadastra tarefas, define a urgência de cada uma e visualiza tudo o que ainda precisa ser feito.
O planejamento completo (Fase 1) está em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).

## Funcionalidades

- Menu contínuo: cadastrar tarefa, visualizar tarefas e sair.
- Cada tarefa tem título, descrição, prioridade, data de vencimento e status.
- Status definido automaticamente como `Pendente` no cadastro.
- Mensagem clara quando não há tarefas cadastradas.

## Regras de negócio

1. **Obrigatoriedade:** o título não pode ficar vazio nem conter apenas espaços.
2. **Restrição de valores:** a prioridade aceita somente `Alta`, `Média` (ou `Media`) e `Baixa`.
3. **Validação de data:** a data de vencimento deve estar no formato `DD/MM/AAAA` e não pode estar no passado.

## Tecnologias

- Python 3.11 (apenas biblioteca padrão)
- Docker e Docker Compose
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Como executar com Docker

**Pré-requisito:** [Docker](https://www.docker.com/products/docker-desktop/) instalado e em execução.

```bash
git clone https://github.com/MatheusAN-25/tasktracker-projeto.git
cd tasktracker-projeto
```

### Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker-app
```

### Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm tasktracker-app
```

> A aplicação usa `input()`, então precisa de um terminal interativo. Por isso o `docker run`
> usa `-it`, e o `docker-compose.yml` define `stdin_open: true` e `tty: true`.

## Como executar sem Docker

```bash
python src/main.py
```

> Em alguns sistemas o comando é `python3 src/main.py`.

## Observações

As tarefas ficam armazenadas apenas em memória durante a execução do programa.
