# 🧑‍🎓 Sistema de Registro de Alunos (CRUD + RA)

Este projeto traz um **sistema de alunos simples e eficiente**, desenvolvido em **Python com SQLAlchemy**, que permite **encontrar seu RA apenas digitando o seu nome**! 🧾  

Com ele, é possível cadastrar, listar, atualizar e remover alunos, além de usar a função especial **“Registro do Aluno (RA)”**, onde basta informar o nome e o sistema retorna automaticamente o **e-mail cadastrado**.  
Ideal para escolas, cursos e cadastros rápidos de estudantes. 🚀

---

## 🚀 Tecnologias utilizadas

- **Python 3.10+**
- **SQLAlchemy**
- **SQLite3**

---

## 📂 Estrutura do Projeto

📦 meu_sistema

┣ 📜 crud_alunos.py

┣ 📜 alunos.db

┗ 📜 README.md

---

## ⚙️ Como executar o projeto

### 1️⃣ Clonar o repositório

### 2️⃣ Instalar as dependências

pip install sqlalchemy

### 3️⃣ Executar o sistema

python crud_alunos.py

🧩 Funcionalidades

Função 	Descrição

➕ Adicionar aluno	Cadastra nome e e-mail de um novo aluno

📋 Listar alunos	Mostra todos os alunos cadastrados

✏️ Atualizar aluno	Edita nome e/ou e-mail de um aluno existente

🗑️ Deletar aluno	Remove um aluno do banco de dados

🧾 RA (Registro do Aluno)	Busca o e-mail de um aluno informando apenas o nome

### 🧠 Exemplo de uso

=== SISTEMA DE ALUNOS ===

1 - Adicionar aluno

2 - Listar alunos

3 - Atualizar aluno

4 - Deletar aluno

5 - RA (Registro do Aluno)

0 - Sair

## Exemplo:

java
Copiar código
Digite o nome do aluno: Maria
📧 O e-mail de Maria é: maria@escola.com
🗃️ Banco de Dados
O projeto utiliza SQLite como banco local (alunos.db).
O SQLAlchemy gerencia automaticamente a criação da tabela alunos com os seguintes campos:

Campo	Tipo	Descrição

id	INTEGER	Identificador único

nome	TEXT	Nome do aluno

email	TEXT	E-mail do aluno (único)

## Exemplo 2: 

Maria quer saber o seu RA e seu email, mas ela nao sabe, a o inves de ir perguntar na secretaria, esse sistema mostra para ela o seu RA e seu email apenas com o seu nome completo, usando o banco de dados com todos os RAs optimizaria o processo de busca.

## 📄 Licença
Este projeto é de uso livre.

Sinta-se à vontade para modificar, estudar e compartilhar 🚀

### 👨‍💻 Autor

📧 gabrielriosmoia@.com

💻 github.com/GabrielMoia


---
