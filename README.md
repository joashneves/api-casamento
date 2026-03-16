# API Casamento

Esta é a API de backend para o site de casamento, desenvolvida com Flask e PostgreSQL. Ela gerencia confirmações de presença (RSVP), lista de presentes e galeria de fotos.

## 🚀 Tecnologias

- **Python 3.9**
- **Flask**: Framework web
- **Flask-SQLAlchemy**: ORM para banco de dados
- **PostgreSQL**: Banco de dados relacional
- **Docker & Docker Compose**: Containerização
- **Git LFS**: Gerenciamento de arquivos de imagem grandes

## 🛠️ Configuração e Execução

### Pré-requisitos
- Docker e Docker Compose instalados.
- Git LFS instalado (`git lfs install`).

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz com as seguintes variáveis:
```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=casamento
ADMIN_USERNAME=seu_usuario
ADMIN_PASSWORD=sua_senha
DATABASE_URL=postgresql://admin:admin@database:5432/casamento
```

### Rodando com Docker
Para subir o ambiente de desenvolvimento:
```bash
docker compose -f infra/compose.yaml up --build
```
A API estará disponível em `http://localhost:5000`.

## 📌 Endpoints da API

### Autenticação
- `POST /api/login`: Validação de credenciais de admin.

### RSVP (Confirmação de Presença)
- `POST /api/rsvp`: Envia uma nova confirmação.
- `GET /api/rsvps`: Lista todos os RSVPs (Livre).
- `GET /api/rsvps/<id>`: Detalhes de um RSVP (Admin).
- `PUT /api/rsvps/<id>`: Atualiza um RSVP (Admin).
- `DELETE /api/rsvps/<id>`: Remove um RSVP (Admin).

### Presentes
- `GET /api/gifts`: Lista todos os presentes.
- `POST /api/gifts`: Adiciona um novo presente (Admin).
- `PUT /api/gifts/<id>`: Atualiza um presente (Admin).
- `DELETE /api/gifts/<id>`: Remove um presente (Admin).
- `POST /api/gifts/<id>/claim`: Marca um presente como escolhido por um convidado.

### Imagens
- `GET /api/images`: Lista os nomes de todos os arquivos na galeria.
- `GET /api/images/<filename>`: Serve o arquivo de imagem individual.

## 📸 Git LFS e Imagens
O projeto utiliza **Git LFS** para armazenar as fotos do casamento em `imagensDeCasamento/`. 
Se as imagens não estiverem aparecendo ou apresentarem erro 304 (Not Modified) sem exibir conteúdo, certifique-se de que os arquivos reais foram baixados:
```bash
git lfs pull
```

No deploy (como Vercel ou Docker), o ambiente deve ter suporte ao Git LFS para que os arquivos não sejam apenas ponteiros de texto.

## 🗄️ Estrutura do Projeto
```text
├── app.py              # Ponto de entrada da aplicação
├── models/             # Modelos do SQLAlchemy
├── routes/             # Blueprints do Flask (Rotas)
├── utils/              # Utilitários e Decoradores
├── imagensDeCasamento/ # Pasta de fotos (Gerenciada por LFS)
├── infra/              # Arquivos de infraestrutura (Docker)
└── .env.development    # Exemplo de configurações
```
