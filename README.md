# 🤖 Bot de Formulário com Django e Selenium

Este projeto cria um formulário web com Django e um bot em Selenium que preenche e envia os dados automaticamente.

## Funcionalidades

- Formulário com nome, e-mail e mensagem.
- Dados salvos no banco de dados via Django.
- Interface de administração para visualizar os envios.
- Bot com Selenium que preenche múltiplos formulários automaticamente.

## Como usar

1. Crie o ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

2. Rode o servidor:

```bash
python manage.py migrate
python manage.py runserver
```

3. Em outro terminal, execute o bot:

```bash
python selenium_bot/preencher_formulario.py
```

---
