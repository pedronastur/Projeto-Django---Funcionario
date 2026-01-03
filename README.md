📌 Apresentação do Projeto

Projeto Django – Gerenciamento de Funcionários


🧠 1. Visão Geral

Este projeto é um sistema web construído com o framework Django (Python) para gerenciar informações de funcionários de uma organização.
Ele permite funcionalidades básicas de cadastro e gerenciamento de dados de funcionários, seguindo os princípios de aplicações web modernas com separação entre dados, lógica e apresentação. 


🛠️ 2. Tecnologias Utilizadas

✔ Python – Linguagem principal do backend
✔ Django – Framework web de alto nível que facilita o desenvolvimento rápido, seguro e organizado de aplicações web seguindo o padrão MVC/MTV. 
✔ HTML / CSS – Estrutura de apresentação das páginas
✔ Banco de Dados SQLite – Banco leve para persistência de dados (default do Django)


📂 3. Estrutura do Projeto

O projeto segue a estrutura típica de um app Django:

📦 Projeto-Django---Funcionario
├── manage.py              # Script de execução e gerenciamento
├── config/                # Configurações Django (settings, urls, wsgi)
├── website/               # Aplicação principal com lógica de funcionários
├── requirements.txt       # Dependências do projeto
├── .gitignore             # Arquivos ignorados pelo Git
└── db.sqlite3             # Banco de dados (SQLite)

Essa divisão facilita a organização do código e escalabilidade do projeto. 


🚀 4. Funcionalidades Principais

✔ CRUD de Funcionários – criar, listar, editar e excluir registros de funcionários
✔ Validação e Formulários – uso de formulários Django para entrada segura de dados
✔ Sistema de URLs e Views – navegação entre diferentes páginas da aplicação
✔ Admin Django (opcional) – painel administrativo padrão do Django para gestão dos dados

(Obs.: dependendo do código disponível no repositório, você pode adicionar mais funcionalidades específicas aqui.)


📌 5. Justificativa Técnica

O uso do Django permite:

✅ Organização pelo padrão MTV (Model-Template-View), facilitando manutenção e expansão. 
✅ Utilização do ORM para manipular banco de dados sem SQL explícito. 
✅ Sistema de administração pronto para uso. 

Essas características tornam o Django ideal para sistemas como esse de gerenciamento de dados.


⚙️ 6. Como Rodar o Projeto (Setup)

Passo a passo:

1. Clonar o repositório
git clone https://github.com/pedronastur/Projeto-Django---Funcionario

2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3. Instalar dependências
pip install -r requirements.txt

4. Aplicar migrações do banco
python manage.py migrate

5. Rodar o servidor
python manage.py runserver



📈 7. Possíveis Melhorias Futura

➡️ Implementar autenticação de usuários para controlar acesso ao sistema.
➡️ Adicionar filtros e pesquisa de funcionários por nome ou setor.
➡️ Criar um dashboard com gráficos/estatísticas.
➡️ Realizar deploy em produção (Heroku, PythonAnywhere, Render etc.). 
Medium

💡 8. Conclusão

Este projeto demonstra a construção de uma aplicação web funcional com Django, abordando conceitos fundamentais como MVC/MTV, ORM, CRUD e boa organização de código. Ele serve tanto como uma base prática de estudo quanto como um MVP para sistemas maiores de gestão de recursos humanos.
