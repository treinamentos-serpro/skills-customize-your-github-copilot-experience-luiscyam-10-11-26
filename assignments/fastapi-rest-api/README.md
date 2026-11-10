# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST simples com FastAPI para praticar rotas HTTP, validação de dados com Pydantic e respostas com códigos de status apropriados. A API gerenciará tarefas em memória, sem banco de dados.

## 📝 Tarefas

### 🛠️ Criar a aplicação e o endpoint de saúde

#### Descrição

Complete o endpoint de saúde no código inicial e execute a aplicação localmente. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos

O programa concluído deve:

- Responder a uma requisição `GET /health` com o JSON `{"status": "ok"}`.
- Permitir que a documentação interativa da API seja acessada em `/docs`.

### 🛠️ Criar e listar tarefas

#### Descrição

Implemente os endpoints para listar as tarefas existentes e adicionar uma nova tarefa. Armazene os dados em memória usando as estruturas já declaradas no código inicial.

#### Requisitos

O programa concluído deve:

- Responder a `GET /tasks` com a lista de tarefas; inicialmente, a lista deve estar vazia.
- Aceitar em `POST /tasks` um JSON com `title` e, opcionalmente, `completed`.
- Atribuir um identificador inteiro único a cada tarefa criada; `completed` deve ser `false` quando não for enviado.
- Retornar a tarefa criada com o código HTTP `201 Created`.

Exemplo de requisição:

```json
{"title": "Estudar FastAPI"}
```

### 🛠️ Consultar, validar e excluir tarefas

#### Descrição

Implemente a consulta e a exclusão de tarefas por identificador e valide os dados recebidos na criação.

#### Requisitos

O programa concluído deve:

- Responder a `GET /tasks/{task_id}` com a tarefa correspondente ou retornar `404 Not Found` quando ela não existir.
- Recusar títulos vazios usando validação do Pydantic e retornar `422 Unprocessable Entity` para dados inválidos.
- Excluir a tarefa em `DELETE /tasks/{task_id}` e retornar `204 No Content` quando a exclusão for bem-sucedida.
- Retornar `404 Not Found` ao tentar excluir uma tarefa inexistente.