# Smart Benefits Monitor

Pipeline que raspa notícias de cartões e milhas, armazena no MySQL e usa o Gemini para resumir e classificar o impacto de cada notícia.

---

## Requisitos

- Python 3.10+
- MySQL rodando localmente (XAMPP, Docker ou Workbench)
- Chave de API do Google Gemini → [aistudio.google.com](https://aistudio.google.com)

**Dependências Python** (instaladas via `requirements.txt`):

| Lib | Uso |
|-----|-----|
| `requests` | Requisições HTTP para o scraping |
| `beautifulsoup4` | Parse do HTML das páginas |
| `mysql-connector-python` | Conexão e queries no MySQL |
| `google-generativeai` | Integração com o Gemini |
| `python-dotenv` | Leitura do arquivo `.env` |

---

## Instalação

**1. Clone o repositório**
```bash
git clone <url-do-repo>
cd Smart-Benefits-Monitor
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

---

## Configuração

**4. Crie o arquivo `.env`** com base no `env_example`:
```
DB_HOST=localhost
DB_NAME=nome_do_seu_banco
DB_USER=root
DB_PASSWORD=sua_senha

GEMINI_API_KEY=sua_chave_aqui
```

**5. Crie a tabela no MySQL**

Execute o SQL abaixo no seu banco de dados:
```sql
CREATE TABLE noticias_financeiras (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  link VARCHAR(500) UNIQUE NOT NULL,
  texto_completo TEXT NOT NULL,
  data_publicacao VARCHAR(50),
  status_processamento VARCHAR(20) DEFAULT 'PENDENTE',
  resumo_ia TEXT,
  impacto_ia VARCHAR(20),
  data_extracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Uso

**6. Execute o pipeline**
```bash
python main.py
```

O script vai:
1. Raspar as últimas notícias de [melhorescartoes.com.br](https://www.melhorescartoes.com.br/) (Na aba "Cartões de crédito")
2. Salvar as novas notícias no banco (duplicatas são ignoradas automaticamente)
3. Buscar todas com `status_processamento = 'PENDENTE'`
4. Analisar cada uma com o Gemini e atualizar `resumo_ia`, `impacto_ia` e o status para `PROCESSADO`

---

## Estrutura

```
├── main.py           # Orquestra o pipeline
├── scraper.py        # Extrai notícias do site
├── database.py       # Funções de banco de dados
├── ai_analyzer.py    # Integração com o Gemini
├── config.py         # Carrega variáveis do .env
├── env_example       # Modelo do arquivo .env
└── requirements.txt  # Dependências
```
