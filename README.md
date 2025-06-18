# 🤖 Bot de Formulário com Django e Selenium

Este projeto é um exemplo completo de automação e backend com **Django** e **Selenium**:

- Um **formulário web** simples para coleta de dados.
- Um **bot automatizado** que preenche e envia formulários usando Selenium.
- **Envio de e-mail** com os dados recebidos.
- Integração com **API externa** (como Google Sheets via Zapier).
- **Testes automatizados** com Django.

---

## ✅ Funcionalidades

- Formulário com campos: `nome`, `e-mail`, `mensagem`
- Salvamento no banco de dados SQLite
- Painel de administração para visualizar os dados
- Envio automático de e-mails após envio do formulário
- Envio automático para Google Sheets via webhook (Zapier)
- Bot com Selenium que preenche e envia múltiplos formulários
- Testes automatizados com `TestCase`

---

## ⚙️ Como instalar

1. **Crie o ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\\Scripts\\activate
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Como executar

1. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` com:

```env
DJANGO_SECRET_KEY=sua_chave_secreta
EMAIL_HOST_USER=seu@email.com
EMAIL_HOST_PASSWORD=sua_senha_de_aplicativo
GOOGLE_SHEETS_WEBHOOK=https://hooks.zapier.com/hooks/catch/123456/abcde
```

> Obs: Para Gmail, ative "senha de app" na sua conta Google.

---

2. **Rode as migrações e o servidor:**

```bash
python manage.py migrate
python manage.py runserver
```

Acesse [http://localhost:8000](http://localhost:8000)

---

3. **Execute o bot Selenium:**

Em outro terminal:

```bash
python selenium_bot/preencher_formulario.py
```

---

## ✅ Rodando os testes

Execute os testes automatizados com:

```bash
python manage.py test
```

---

## 🧪 Estrutura do Projeto

```
form_bot_django/
├── formulario/                  # App principal
│   ├── templates/formulario/
│   │   ├── index.html
│   │   └── sucesso.html
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── selenium_bot/               # Bot em Selenium
│   └── preencher_formulario.py
├── form_site/                  # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── .env
├── manage.py
└── requirements.txt
```

---

## 📡 Integração com Google Sheets (via Zapier)

1. Crie um Zap no [Zapier](https://zapier.com/)
2. Use o evento "Catch Hook" com "Webhooks by Zapier"
3. Copie o link do webhook e cole no `.env` como `GOOGLE_SHEETS_WEBHOOK`
4. Teste enviando um formulário — os dados chegarão na planilha!

---

## 🛠️ Requisitos

- Python 3.9+
- Django 4.x
- Google Chrome + WebDriver (para o bot)
- Conta no Zapier (ou webhook.site como alternativa)

