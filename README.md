# 📚 Livre Aqui!

O **Livre Aqui!** é uma aplicação web desenvolvida em **Django** com o objetivo de facilitar o acesso à cultura por meio da divulgação de **livros e filmes em domínio público** ou cuja **distribuição seja legalmente permitida**.

A plataforma reúne obras em um único catálogo, permitindo sua descoberta e distribuição utilizando a tecnologia **BitTorrent**, incentivando também que os usuários continuem compartilhando os arquivos após o download para contribuir com a preservação do acervo.

---

## ✨ Funcionalidades

- 📚 Catálogo de livros
- 🎬 Catálogo de filmes
- 🔎 Pesquisa de obras
- 📄 Página de detalhes de livros e filmes
- 🧲 Download por links magnéticos (BitTorrent)
- ℹ️ Página institucional sobre o projeto

---

## 🛠️ Tecnologias utilizadas

- Python
- Django
- PostgreSQL
- Bootstrap 5
- HTML5
- CSS3
- BitTorrent

---

## 🚀 Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/livre-aqui.git
```

Entre na pasta do projeto:

```bash
cd livre-aqui
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto:

```env
DEBUG=True

SECRET_KEY=sua_chave_secreta

DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

---

## 📁 Estrutura do projeto

```text
catalog/        Página inicial e páginas institucionais
ebook/          Aplicação de livros
movie/          Aplicação de filmes
config/         Configuração do projeto
templates/      Templates HTML
static/         Arquivos estáticos
```

---

## ⚖️ Direitos autorais

O projeto busca disponibilizar **apenas obras em domínio público ou cuja distribuição seja legalmente permitida**.

Caso algum conteúdo tenha sido publicado de forma equivocada, o detentor dos direitos autorais ou seu representante poderá solicitar sua remoção. Após a verificação, o material será removido quando necessário.

---

## 🤝 Contribuindo

Sugestões de melhorias, correções e novas funcionalidades são bem-vindas.

Caso conheça livros ou filmes em domínio público ou cuja distribuição seja legalmente permitida e que ainda não estejam cadastrados, fique à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

---

## 📌 Funcionalidades planejadas

- Filtros por gênero
- Pesquisa avançada
- Página dos autores
- Melhorias na interface
- Ampliação do catálogo
- Internacionalização

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

As obras disponibilizadas pela aplicação possuem licenças próprias ou pertencem ao domínio público. A licença do código-fonte não altera os direitos autorais das obras catalogadas.

---

## 👤 Autor

Desenvolvido por **Robson**.