# 📘 Assignment: Containerize uma API Python com Docker

## 🎯 Objective

Aprender a containerizar uma aplicação API em Python (FastAPI) criando um `Dockerfile`, construindo a imagem e executando o container localmente.

## 📝 Tasks

### 🛠️ Criar a aplicação FastAPI

#### Description

Implemente uma API simples usando FastAPI com rotas para testar se o serviço está funcionando.

#### Requirements
Completed program should:

- Ter um endpoint root `/` que retorne uma mensagem JSON de boas-vindas.
- Ter um endpoint `GET /items/{item_id}` que retorne um objeto JSON com `id` e `name`.
- Código de exemplo disponível em `app/main.py`.

### 🛠️ Escrever o `Dockerfile`

#### Description

Escreva um `Dockerfile` que instala dependências, copia o código e execute a aplicação com `uvicorn`.

#### Requirements
Completed program should:

- Usar uma imagem base Python (por exemplo `python:3.11-slim`).
- Instalar dependências a partir de `requirements.txt`.
- Expor a porta `8000` e rodar o servidor com `uvicorn`.

### 🛠️ Construir e executar o container

#### Description

Construa a imagem Docker e execute o container localmente, verificando os endpoints com `curl`.

#### Requirements
Completed program should:

- Incluir instruções para construir: `docker build -t dockerize-api .`.
- Incluir instruções para executar: `docker run -p 8000:8000 dockerize-api`.
- Mostrar como testar o endpoint: `curl http://localhost:8000/`.


## 📎 Arquivos fornecidos

- `app/main.py` — exemplo de aplicação FastAPI.
- `requirements.txt` — dependências.
- `Dockerfile` — arquivo para construir a imagem.

## ⏱️ Tempo estimado

Aproximadamente 1–2 horas.
