# EcoVista Back-End

Este é o repositório do back-end do projeto EcoVista, desenvolvido utilizando Django Ninja Extra.

## Requisitos

- Python 3.8+
- Django 3.2+
- Django Ninja Extra

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/EcoVista-Back-End.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd EcoVista-Back-End
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:
    ```env
    DEBUG=True
    SECRET_KEY=sua-chave-secreta
    DATABASE_URL=sqlite:///db.sqlite3
    ```

2. Aplique as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Criando os APPS:
    ```bash
    python manage.py create_module_app token
    ```
4. Deletando os APPS:
    ```
    python manage.py delete_module_app token
    ```

5. Crie um superusuário para acessar a documentação:
    ```bash
    python manage.py createsuperuser
    ```
    Preencha os campos solicitados:
    - Email
    - Password
    - Username

## Executando o Projeto

1. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

2. Acesse o projeto em `http://127.0.0.1:8000/`.

## Endpoints

Os endpoints da API estão documentados automaticamente pelo Django Ninja Extra e podem ser acessados em `http://127.0.0.1:8000/api/v1/docs`.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Faça commit das suas alterações:
    ```bash
    git commit -m 'feat(<Nome do app alterado>): adiciona nova funcionalidade'
    ```
4. Envie para o repositório remoto:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request.

## Arquitetura do Projeto

O projeto EcoVista Back-End segue uma arquitetura em camadas, dividida em Repository, Models e Controller. Abaixo está uma descrição das pastas e da estrutura do projeto:

### Estrutura de Pastas

Esse é um exemplo da arquitetura do projeto

- `EcoVista_BackEnd/`
    - `apps/`
        - `token/`
            - `migrations/`
            - `models.py`
            - `views.py`
            - `serializers.py`
            - `urls.py`
            - `services.py`
            - `repositories.py`
    - `core/`
        - `settings.py`
        - `urls.py`
        - `wsgi.py`
    - `manage.py`
    - `requirements.txt`

### Camadas

#### Repository

A camada de Repository é responsável pela comunicação direta com o banco de dados. Ela contém classes e métodos que realizam operações de CRUD (Create, Read, Update, Delete). No projeto, essa camada está representada pelos arquivos `repositories.py` dentro de cada app.

#### Services

A camada de Services contém a lógica de negócios da aplicação. Ela é responsável por implementar as regras de negócio e orquestrar as operações entre as diferentes camadas. No projeto, essa camada está representada pelos arquivos `services.py` dentro de cada app.

#### Controller

A camada de Controller gerencia a lógica de aplicação e a interação entre as camadas de Models e Repository. No Django, essa camada é representada pelos arquivos `controllers.py`, que contêm as views responsáveis por processar as requisições HTTP e retornar as respostas apropriadas.

### Exemplo de Arquitetura em um App

#### `token/models.py`
Define os modelos relacionados ao token, como a estrutura de dados e as relações.

#### `token/repositories.py`
Contém classes e métodos para operações de CRUD relacionadas aos modelos de token.

#### `token/controller.py`
Gerencia as requisições HTTP relacionadas aos tokens, utilizando os modelos e repositórios para processar os dados.

Essa arquitetura em camadas ajuda a manter o código organizado, facilitando a manutenção e a escalabilidade do projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
