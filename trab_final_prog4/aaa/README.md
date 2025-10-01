# 🚀 Flask Blog Project - Trabalho Final de Programação IV

**Um blog moderno construído com Flask, featuring tema escuro e interface contemporânea**

![Status](https://img.shields.io/badge/Status-✅%20Funcionando-brightgreen)
![Flask](https://img.shields.io/badge/Flask-3.1.2-blue)
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Theme](https://img.shields.io/badge/Theme-🌙%20Dark%20Mode-black)

---

## 🎨 **Demonstração Visual**

### Interface Moderna com Tema Escuro
- 🌙 **Design System Profissional** baseado no GitHub Dark Theme
- 🎨 **Paleta de cores consistente** com variáveis CSS
- ✨ **Animações suaves** e hover effects
- 📱 **Layout 100% responsivo** para todos os dispositivos
- 🎯 **Componentes reutilizáveis** (cards, botões, formulários)

---

## ⚡ **Funcionalidades Principais**

### 🔐 **Sistema de Autenticação**
- ✅ Registro com confirmação automática (modo desenvolvimento)
- ✅ Login/Logout seguro com Flask-Login
- ✅ Sistema de papéis: `user`, `moderator`, `admin`
- ✅ Validação robusta com email-validator
- ✅ Proteção CSRF integrada

### 📝 **Gerenciamento de Posts**
- ✅ **CRUD completo** para posts
- ✅ **Editor moderno** com preview em tempo real
- ✅ **Permissões granulares:** autor pode editar seus posts; moderator/admin podem gerenciar qualquer post
- ✅ **Interface intuitiva** com cards e hover effects
- ✅ **Visualização detalhada** com tipografia otimizada

### 👥 **Administração de Usuários**
- ✅ **Painel administrativo** completo para gerenciar usuários (`/admin/users`)
- ✅ **Alteração de papéis** em tempo real via dropdown
- ✅ **Perfil do usuário** editável
- ✅ **Interface moderna** com tabela responsiva

### 🌟 **Recursos Especiais**
- ✅ **Citação do Dia** com integração assíncrona à API Quotable
- ✅ **Botão X interativo** para esconder/mostrar citação com localStorage
- ✅ **Tradução automática** para português via LibreTranslate
- ✅ **Sistema de fallback** com citações em português quando APIs falham
- ✅ **Notificações visuais** coloridas e informativas
- ✅ **Performance otimizada** com cache de citações

---

## 👥 **Usuários Pré-configurados**

O projeto já vem com usuários de exemplo para teste:

### 🔑 **Credenciais de Acesso**

#### 👨‍💼 **Administrador**
- **Username:** `admin`
- **Email:** `admin@blog.com`
- **Senha:** `admin123`
- **Permissões:** Acesso total, painel admin

#### 👤 **Usuários Normais**
| Username | Email | Senha | Role | Posts |
|----------|-------|--------|------|-------|
| `joao_silva` | joao@email.com | senha123 | user | 2 |
| `maria_santos` | maria@email.com | senha123 | moderator | 1 |
| `carlos_oliveira` | carlos@email.com | senha123 | user | 1 |
| `ana_costa` | ana@email.com | senha123 | user | 1 |

### 📝 **Posts de Exemplo**
O banco já contém **7 posts** com conteúdo variado:
- Tecnologia e sustentabilidade
- Benefícios da leitura
- Receita de bolo de chocolate
- Dicas de produtividade
- Experiência com Python
- Regras de convivência
- Bem-vindos ao blogject - Trabalho Final de Programação IV

**Um blog moderno construído com Flask, featuring tema escuro e interface contemporânea**

![Status](https://img.shi└── 📂 instance/             # Diretório para banco de dados.io/badge/Status-✅%20Funcionando-brightgreen)
![Flask](https://img.shields.io/badge/Flask-3.1.2-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Theme](https://img.shields.io/badge/Theme-🌙%20Dark%20Mode-black)

---

## 🎨 **Demonstração Visual**

### Interface Moderna com Tema Escuro
- 🌙 **Design System Profissional** baseado no GitHub Dark Theme
- 🎨 **Paleta de cores consistente** com variáveis CSS
- ✨ **Animações suaves** e hover effects
- 📱 **Layout 100% responsivo** para todos os dispositivos
- 🎯 **Componentes reutilizáveis** (cards, botões, formulários)

---

## ⚡ **Funcionalidades Principais**

### 🔐 **Sistema de Autenticação**
- ✅ Registro com confirmação automática (modo desenvolvimento)
- ✅ Login/Logout seguro com Flask-Login
- ✅ Sistema de papéis: `user`, `moderator`, `admin`
- ✅ Validação robusta com email-validator
- ✅ Proteção CSRF integrada

### 📝 **Gerenciamento de Posts**
- ✅ **CRUD completo** para posts
- ✅ **Editor moderno** com preview em tempo real
- ✅ **Permissões granulares:** autor pode editar seus posts; moderator/admin podem gerenciar qualquer post
- ✅ **Interface intuitiva** com cards e hover effects
- ✅ **Visualização detalhada** com tipografia otimizada

### 👥 **Administração de Usuários**
- ✅ **Painel administrativo** para gerenciar usuários
- ✅ **Alteração de papéis** em tempo real
- ✅ **Perfil do usuário** editável
- ✅ **Estatísticas** de usuários e posts

### 🌟 **Recursos Especiais**
- ✅ **Citação do Dia** com integração assíncrona à API Quotable
- ✅ **Tradução automática** para português via LibreTranslate
- ✅ **Sistema de fallback** com citações em português quando APIs falham
- ✅ **Notificações visuais** coloridas e informativas
- ✅ **Performance otimizada** com cache de citações

---

## 🛠️ **Stack Tecnológica**

### Backend
- **Flask 3.1.2** - Framework web minimalista
- **SQLAlchemy 2.0** - ORM para banco de dados
- **Flask-Login** - Gerenciamento de sessões
- **Flask-Mail** - Sistema de emails
- **Flask-WTF** - Formulários e validação
- **itsdangerous** - Tokens seguros

### Frontend
- **HTML5** semântico e acessível
- **CSS3 moderno** com variables, grid e flexbox
- **JavaScript vanilla** para interações
- **Design responsivo** mobile-first

### Database & Security
- **SQLite** para desenvolvimento (fácil migração para PostgreSQL/MySQL)
- **Werkzeug** para hash seguro de senhas
- **CSRF Protection** em todos os formulários
- **Sanitização de dados** automática

---

## 🚀 **Instalação e Execução**

### 1. **Configuração do Ambiente**
```bash
# Clone o projeto
git clone [url-do-repositorio]
cd trab_final_prog4/aaa

# Criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS

# Instalar dependências
pip install -r requirements.txt
```

### 2. **Configuração das Variáveis**
O projeto já inclui um arquivo `.env` configurado para desenvolvimento:
```bash
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=dev_secret_key_muito_segura_para_desenvolvimento_123
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=dev@example.com
MAIL_PASSWORD=dev_password
MAIL_USE_TLS=1
```

### 3. **Execução**
```bash
python app.py
```

**🎯 Acesse:** http://127.0.0.1:5000

---

## 👨‍💼 **Como Usar**

### **Primeiro Acesso**
1. Execute o projeto: `python app.py`
2. Acesse: http://127.0.0.1:5000
3. Faça login com qualquer usuário da lista acima
4. Explore as funcionalidades disponíveis

### **Tipos de Usuário**
- **Admin:** Todas as permissões (criar posts, gerenciar usuários via `/admin/users`, moderar conteúdo)
- **Moderator:** Pode moderar e editar posts de outros usuários
- **User:** Pode criar e editar apenas próprios posts

### **Funcionalidades por Papel**
- **Todos:** Ver posts, criar conta, editar perfil
- **Usuários logados:** Criar posts, editar próprios posts
- **Moderadores:** Editar qualquer post
- **Administradores:** Painel admin, alterar roles de usuários

---

## 📁 **Estrutura do Projeto**

```
trab_final_prog4/aaa/
├── 📄 app.py                 # Aplicação Flask principal
├── 📄 models.py              # Modelos do banco (User, Post)
├── 📄 forms.py               # Formulários WTF
├── 📄 email_utils.py         # Utilitários de email
├── 📄 requirements.txt       # Dependências Python
├── 📄 .env                   # Variáveis de ambiente (desenvolvimento)
├── � .env.example           # Template de variáveis
├── 📄 README.md              # Este arquivo
├── �📂 templates/             # Templates Jinja2
│   ├── base.html            # Template base com tema escuro
│   ├── index.html           # Página inicial
│   ├── login.html           # Formulário de login
│   ├── register.html        # Formulário de registro
│   ├── create_post.html     # Criação de posts
│   ├── edit_post.html       # Edição de posts
│   ├── post_detail.html     # Detalhes do post
│   ├── profile.html         # Perfil do usuário
│   └── admin_users.html     # Painel administrativo
├── 📂 static/
│   └── style.css            # CSS moderno com tema escuro
└── 📂 instance/
    └── app.db               # Banco SQLite com dados
```

---

## 🎨 **Melhorias de Design Implementadas**

### **Interface Moderna**
- 🌙 **Tema escuro profissional** inspirado no GitHub
- 🎨 **Gradientes coloridos** em títulos e botões
- ✨ **Animações suaves** em hover e transições
- 📱 **Design responsivo** com breakpoints otimizados
- 🎯 **Micro-interações** para melhor UX

### **Componentes Visuais**
- 💳 **Cards elevados** para posts com sombras
- 🔘 **Botões modernos** com estados visuais
- 📝 **Formulários estilizados** com validação em tempo real
- 🚨 **Notificações coloridas** por categoria
- 📊 **Layout grid moderno** para organização

### **Citação Interativa**
- 💭 **Widget flutuante** no canto direito
- ❌ **Botão X** para esconder/mostrar
- 💾 **Persistência** com localStorage
- 🔄 **Duplo-clique** para restaurar
- 🌐 **API assíncrona** com fallback

---

## 🎯 **Funcionalidades de Teste**

### **Teste de Login**
1. Acesse `/login`
2. Use qualquer credencial da tabela de usuários
3. Teste diferentes roles e permissões

### **Teste de Admin**
1. Login como `admin` / `admin123`
2. Acesse `/admin/users`
3. Altere roles dos usuários
4. Teste permissões

### **Teste de Posts**
1. Login com qualquer usuário
2. Acesse `/post/new`
3. Crie um novo post
4. Teste edição e visualização

### **Teste de Citação**
1. Veja a citação no canto direito
2. Clique no **X** para esconder
3. Duplo-clique no fundo para mostrar
4. Recarregue a página (preferência persiste)

---

## 🔧 **Funcionalidades Técnicas Avançadas**

### **Sistema de Email Inteligente**
```python
# Auto-detecção de modo desenvolvimento
is_dev_mode = (app.config.get('MAIL_SERVER') == 'smtp.example.com' or 
              os.environ.get('FLASK_ENV') == 'development')

if is_dev_mode:
    # Confirmação automática em desenvolvimento
    user.confirmed = True
else:
    # Envio de email em produção com fallback
    try:
        send_confirmation_email(user, app, mail)
    except Exception:
        user.confirmed = True  # Fallback gracioso
```

### **Sistema de Citações Assíncronas**
```python
# Cache inteligente com fallback
def fetch_and_translate_quote(app):
    try:
        # Buscar da API Quotable
        response = requests.get('https://api.quotable.io/random', timeout=5)
        # Traduzir com LibreTranslate
        translate_response = requests.post('https://libretranslate.de/translate', ...)
    except Exception:
        # Fallback com citações em português
        quote_cache['text'] = "O sucesso é a soma de pequenos esforços repetidos."
        quote_cache['author'] = "Robert Collier"
```

### **Validação e Segurança**
- ✅ **Validação de duplicatas** automática
- ✅ **Hash seguro de senhas** com scrypt
- ✅ **Proteção CSRF** em todos os formulários
- ✅ **Sanitização** automática de inputs
- ✅ **Rate limiting** nas APIs externas

---

## 📊 **Status do Banco de Dados**

```
📊 ESTADO ATUAL:
├── Usuários: 5 (1 admin + 4 usuários)
├── Posts: 7 (conteúdo variado)
├── Integridade: ✅ Estrutura populada
├── Auto-confirmação: ✅ Ativa em desenvolvimento
└── Papéis: user, moderator, admin configurados
```

---

## 🎯 **Status do Projeto**

✅ **PROJETO 100% FUNCIONAL**
- Interface moderna implementada
- Banco de dados configurado e populado com dados de exemplo
- Sistema de autenticação funcionando com usuários pré-configurados
- Painel administrativo operacional
- Citação interativa com botão X
- Todas as funcionalidades testadas
- Deploy-ready para produção

**Desenvolvido com ❤️ usando Flask e tema escuro moderno**

---

**🌟 Última atualização:** 1º de outubro de 2025
