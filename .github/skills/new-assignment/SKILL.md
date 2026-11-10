---
name: new-assignment
description: 'Use whenever creating, adding, structuring, or generating a programming assignment, exercise, homework, or lesson for students in the Mergington High School portal.'
---

# Criar Nova Tarefa de Programação

Use este fluxo para criar uma atividade em `assignments/<id>/` e registrá-la no portal por meio de `config.json`.

## Etapa 1: Coletar requisitos

Se o usuário não informar o conceito de programação, pergunte qual conceito a atividade deve abordar. Identifique também o nível dos alunos, os objetivos de aprendizagem e os requisitos. O script de registro define automaticamente o prazo para sete dias após o cadastro; ele não aceita prazos personalizados.

Leia as [instruções para atividades](../../instructions/assignments.instructions.md), o [guia de atividades](./references/assignment-guide.md) e o [template](../../../templates/assignment-template.md). Consulte uma atividade existente quando precisar confirmar como o código inicial ou os dados são usados.

## Etapa 2: Criar a atividade

1. Escolha um identificador descritivo em kebab-case e confirme que ele não existe em `assignments/` nem em `config.json`.
2. Crie `assignments/<id>/README.md` usando o template e as instruções do projeto.
3. Adicione `starter-code.py` quando ajudar o aluno a começar a implementação. Adicione `data.csv` apenas quando a atividade exigir um conjunto de dados fornecido.
4. Dentro da pasta da atividade, use somente `README.md`, `starter-code.py` e `data.csv`, pois o hook do projeto bloqueia outros nomes.
5. Escreva o README em português claro e acolhedor, preserve a hierarquia exata do template, descreva o objetivo em 1 ou 2 frases e divida o trabalho em tarefas com requisitos observáveis e testáveis. Coloque exemplos de entrada e saída em blocos de código quando forem úteis.
6. Mantenha nomes, parâmetros, entradas e saídas do README consistentes com o código inicial e os dados. Ofereça orientação inicial sem incluir a solução completa, salvo se o usuário pedir.

## Etapa 3: Registrar no portal

Use os scripts incluídos; não edite `config.json` manualmente.

Registre a atividade:

```bash
node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"
```

O prazo é calculado automaticamente para sete dias após o cadastro e incluído em `config.json`.

Registre cada arquivo que deve ser baixado como anexo:

```bash
node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>
```

Os anexos suportados são `starter-code.py` com tipo `python` e `data.csv` com tipo `csv`. Só registre arquivos que existam na pasta da atividade.

## Etapa 4: Verificar

Confirme que a entrada foi adicionada sem duplicar um `id`, que `config.json` continua válido e que todos os anexos apontam para arquivos existentes. Confira também os cabeçalhos do README e a consistência entre os requisitos, o código inicial e os dados.

Ao concluir, informe o identificador, os arquivos criados e o registro no portal. Mencione dados pendentes que o usuário não forneceu.