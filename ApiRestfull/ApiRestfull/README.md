# Task Management API 📝

Este é um projeto simples **FastAPI** para gerenciar uma lista de tarefas. Ele fornece funcionalidades básicas de CRUD e capacidades de busca, tornando-o um ótimo ponto de partida para aprender FastAPI.


## Funcionalidades ✨

- 📋 Listar todas as tarefas.
- 🔍 Recuperar uma tarefa pelo ID.
- ➕ Adicionar uma nova tarefa.
- ✏️ Atualizar os detalhes de uma tarefa existente.
- ❌ Deletar uma tarefa.

---

## Endpoints 🌐

### 1. **Listar Todas as Tarefas** 📋
**GET** `/tasks`

Recupera a lista de todas as tarefas.

**Resposta:**
```json
{
  "status": "success",
  "message": "Tasks retrieved successfully.",
  "data": [...]
}
```

---

### 2. **Recuperar Tarefa pelo ID** 🔍
**GET** `/tasks/{task_id}`

Recupera os detalhes de uma tarefa usando seu ID único.

**Resposta (se encontrada):**
```json
{
  "status": "success",
  "message": "Task retrieved successfully.",
  "data": {...}
}
```


---

### 3. **Adicionar uma Nova Tarefa** ➕
**POST** `/tasks`

**Request Body:**
```json
{
  "title": "Nova Tarefa",
  "description": "Descrição da nova tarefa",
  "status": "pendente"  // Valores permitidos: "pendente", "em_progresso", "completada"
}
```

**Resposta:**
```json
{
  "status": "success",
  "message": "Task added successfully.",
  "data": {
    "id": 1,
    "title": "Nova Tarefa",
    "description": "Descrição da nova tarefa",
    "status": "pendente"
  }
}
```

---

### 4. **Atualizar uma Tarefa** ✏️
**PUT** `/tasks/{task_id}`

**Request Body:**
```json
{
  "title": "Tarefa Atualizada",
  "description": "Descrição atualizada da tarefa",
  "status": "em_progresso"  // Valores permitidos: "pendente", "em_progresso", "completada"
}
```

**Resposta:**
```json
{
  "status": "success",
  "message": "Task updated successfully.",
  "data": {
    "id": 1,
    "title": "Tarefa Atualizada",
    "description": "Descrição atualizada da tarefa",
    "status": "em_progresso"
  }
}
```

---

### 5. **Deletar uma Tarefa** ❌
**DELETE** `/tasks/{task_id}`

Deleta uma tarefa pelo seu ID.

**Resposta:**
```json
{
  "status": "success",
  "message": "Task deleted successfully."
}
```

---

## Comandos do Ambiente Conda ⚙️

Aqui estão alguns comandos úteis para gerenciar seus ambientes Conda:

- 🌱 **Ver ambientes criados**:
  ```bash
  conda info --envs
  ```

- ❌ **Remover um ambiente**:
  ```bash
  conda env remove --name pweb1
  ```

- 🆕 **Criar um novo ambiente**:
  ```bash
  conda create --name pweb1 pip python=3.13
  ```

- 🔄 **Ativar um ambiente**:
  ```bash
  conda activate pweb1
  ```

- 🚪 **Desativar um ambiente**:
  ```bash
  conda deactivate
  ```

## Como Executar 🚀

### Pré-requisitos

- 🐍 Python 3.9 ou superior instalado.
- 🛠 Instalar dependências.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/Mandysan123/FastAPI---Amanda-Morais.git
   cd .\FastAPI---Amanda-Morais\apirestfull
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor de desenvolvimento:
   ```bash
   uvicorn main:app --reload
   ```

4. Abra seu navegador e navegue para:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📄
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 📚

5. Link da Coleção no Postman
   - https://abrir.link/TNqwA 🔗
