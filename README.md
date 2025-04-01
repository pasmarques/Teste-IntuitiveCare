# Teste-IntuitiveCare
Repositório para guardar os códigos do teste da vaga de estágio


O maior projeto foi o do teste 4, por isso criei um read.me para ele

```
operadoras-busca/  
│── backend/  
│   ├── app.py  # Código do Flask  
│   ├── Relatorio_cadop.csv  # Arquivo de dados  
│   ├── requirements.txt  # Dependências do Flask  
│   ├── postman_collection.json  # Arquivo do Postman  
│   └── README.md  # Instruções para rodar o backend  
│  
│── frontend/  
│   ├── src/  
│   │   ├── components/  
│   │   │   ├── BuscaOperadora.vue  # Componente Vue  
│   │   ├── App.vue  # Arquivo principal  
│   │   ├── main.js  # Configuração Vue  
│   ├── package.json  # Dependências do Vue.js  
│   ├── vite.config.js  # Configuração do Vite  
│   └── README.md  # Instruções para rodar o frontend  
│  
│── .gitignore  
│── README.md  # Instruções gerais  
```

---

```md
# Busca de Operadoras de Saúde

Este projeto contém um backend em Flask e um frontend em Vue.js para pesquisar operadoras de saúde a partir de um arquivo CSV.

## 📌 Como Rodar

### 🔹 Backend (Flask)
1. Instale o Python 3 e crie um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Rode o servidor:
   ```sh
   python api.py
   ```
4. O backend estará disponível em `http://127.0.0.1:5000`.

### 🔹 Testando no Postman
- Importe `postman_collection.json` no Postman.  
- Faça uma requisição GET para `http://127.0.0.1:5000/buscar?termo=saude`.

### 🔹 Frontend (Vue.js)
1. Instale o Node.js e o Vue.js:
   ```sh
   npm install -g @vue/cli
   ```
2. Vá para a pasta `frontend/` e instale as dependências:
   ```sh
   cd frontend
   npm install
   ```
3. Inicie o servidor:
   ```sh
   npm run dev
   ```
4. Acesse `http://localhost:5173` no navegador.

## 📜 Licença
MIT License
```
