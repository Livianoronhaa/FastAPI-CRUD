# Sistema de Gerenciamento de Projetos e Tarefas

Este projeto é uma API construída com FastAPI para gerenciamento de **projetos** e **tarefas**. O sistema permite gerenciar de forma simples e eficiente tanto projetos quanto as tarefas associadas a eles. Ele oferece funcionalidades para criação, edição e exclusão de projetos e tarefas, facilitando o gerenciamento de fluxos de trabalho em um ambiente de desenvolvimento ou outras áreas que necessitam de controle sobre projetos e suas respectivas tarefas.

## O Problema que o Projeto Resolve

Este sistema resolve o problema de gerenciamento desorganizado de **projetos** e **tarefas**, permitindo que os usuários:

- Criem e organizem projetos de forma simples.
- Associem tarefas específicas a cada projeto.
- Atualizem informações sobre projetos e tarefas (como nome e status).
- Excluam projetos e tarefas quando não forem mais necessários.

Isso ajuda a manter o controle sobre o progresso de projetos e tarefas, oferecendo uma estrutura clara e eficiente para gerenciamento.

## Como Instalar e Executar o Projeto

### Requisitos

- Python 3.7 ou superior.
- `pip` para gerenciar dependências.

### Passos para Instalação

➡️Clone o repositório

➡️Construa e inicie os contêineres

    docker-compose up --build -d

➡️Acesse a aplicação

    http://localhost:8080

Importe a Coleção para o Postman

# Rotas da API

## Projetos

### ✅ Criar Projeto

Rota: POST /projetos  
 Descrição: Cria um novo projeto.  
 Exemplo de body:

    {
      "nome": "Projeto de Desenvolvimento"
    }

### ✅ Listar Projetos

Rota: GET /projetos  
 Descrição: Retorna todos os projetos cadastrados.  
 Exemplo de resposta:

    [
      {
        "id": 1,
        "nome": "Projeto de Desenvolvimento"
      }
    ]

### ✅ Atualizar Projeto

Rota: PUT /projetos/{projeto_id}  
 Descrição: Atualiza o nome de um projeto existente.  
 Exemplo de body:

        {
          "nome": "Novo Nome do Projeto"
        }

Exemplo de URL: http://127.0.0.1:8000/projetos/1

### ✅ Deletar Projeto

Rota: DELETE /projetos/{projeto_id}  
 Descrição: Exclui um projeto.  
 Exemplo de URL: http://127.0.0.1:8000/projetos/1

## Tarefas

### ✅ Criar Tarefa

Rota: POST /tarefas  
 Descrição: Cria uma nova tarefa associada a um projeto.  
 Exemplo de body:

    {
    "id": 1,
    "nome": "Tarefa 1",
    "descricao": "Descrição da tarefa 1",
    "projeto_id": 1,
    "usuario_id": 1,
    "status": "pendente"

}

### ✅ Listar Tarefas por Projeto

Rota: GET /tarefas/{projeto_id}  
 Descrição: Retorna todas as tarefas associadas a um projeto.  
 Exemplo de URL: http://127.0.0.1:8000/tarefas/1  
 Exemplo de resposta:

    [
      {
        "id": 1,
        "nome": "Tarefa 1",
        "descricao": "Descrição da tarefa 1",
        "projeto_id": 1,
        "usuario_id": 1,
        "status": "pendente"
      }
    ]

### ✅ Atualizar Tarefa

Rota: PUT /tarefas/{tarefa_id}  
 Descrição: Atualiza uma tarefa existente, incluindo seu nome, descrição e status.  
 Exemplo de body:

    {
      "id": 1,
      "nome": "Tarefa 1",
      "descricao": "Descrição da tarefa 1",
      "projeto_id": 1,
      "usuario_id": 1,
      "status": "Concluído"
    }

Exemplo de URL: http://127.0.0.1:8000/tarefas/1

### ✅ Deletar Tarefa

Rota: DELETE /tarefas/{tarefa_id}  
 Descrição: Exclui uma tarefa.  
 Exemplo de URL: http://127.0.0.1:8000/tarefas/1

## Usuários

### ✅ Criar Usuário

Rota: POST /usuarios  
 Descrição: Cria um novo usuário.
Exemplo de body:

    {

"nome": "João Silva",
"email": "joao.silva@example.com",
"senha": "senha123"
}

### ✅ Listar Todos os Usuários

Rota: GET /usuarios
Descrição: Retorna todos os usuários cadastrados.
Exemplo de URL: http://127.0.0.1:8000/usuarios
Exemplo de resposta:

    [

{
"id": 1,
"nome": "João Silva",
"email": "joao.silva@example.com"
},
{
"id": 2,
"nome": "Maria Oliveira",
"email": "maria.oliveira@example.com"
}
]

### ✅ Obter Usuário por ID

Rota: GET /usuarios/{usuario_id}
Descrição: Retorna os detalhes de um usuário específico pelo ID.
Exemplo de body:

    {

"id": 1,
"nome": "João Silva",
"email": "joao.silva@example.com"
}

Exemplo de URL: http://127.0.0.1:8000/usuarios/1

### ✅ Atualizar Usuário

Rota: PUT /usuarios/{usuario_id}
Descrição: Atualiza as informações de um usuário existente, como nome e email.

Exemplo de body:

    {

"nome": "João Silva Atualizado",
"email": "joao.silva.novo@example.com",
"senha": "novaSenha123"
}

Exemplo de URL: http://127.0.0.1:8000/usuarios/1

### ✅ Deletar Usuário

Rota: DELETE /usuarios/{usuario_id}
Descrição: Exclui um usuário pelo ID.

Resposta Esperada:

{
"mensagem": "Usuário deletado com sucesso!"
}

Exemplo de URL: http://127.0.0.1:8000/usuarios/1
