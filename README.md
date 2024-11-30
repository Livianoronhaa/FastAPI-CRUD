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
   

➡️Crie e ative um ambiente virtual:

    python -m venv venv
    .\venv\Scripts\activate
    
➡️Instale as dependências: No diretório do projeto, instale as dependências necessárias:

    pip install -r requirements.txt

➡️Execute a aplicação: Agora, execute o servidor FastAPI com o comando:

    uvicorn main:app --reload

💻O servidor estará disponível em http://127.0.0.1:8000.

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
      "nome": "Desenvolver API",
      "descricao": "Criar a API de gerenciamento de tarefas",
      "projeto_id": 1,
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
        "nome": "Desenvolver API",
        "descricao": "Criar a API de gerenciamento de tarefas",
        "projeto_id": 1,
        "status": "pendente"
      }
    ]

### ✅ Atualizar Tarefa

   Rota: PUT /tarefas/{tarefa_id}  
    Descrição: Atualiza uma tarefa existente, incluindo seu nome, descrição e status.  
    Exemplo de body:  

    {
      "nome": "Desenvolver API - Versão 2",
      "descricao": "Atualizar a API de gerenciamento de tarefas",
      "projeto_id": 1,
      "status": "em andamento"
    }

  Exemplo de URL: http://127.0.0.1:8000/tarefas/1

### ✅ Deletar Tarefa

  Rota: DELETE /tarefas/{tarefa_id}  
    Descrição: Exclui uma tarefa.  
    Exemplo de URL: http://127.0.0.1:8000/tarefas/1  

