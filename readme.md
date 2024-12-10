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

## Executando o Projeto

1. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

2. Acesse o projeto em `http://127.0.0.1:8000/`.

## Endpoints

Os endpoints da API estão documentados automaticamente pelo Django Ninja Extra e podem ser acessados em `http://127.0.0.1:8000/api/docs`.

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

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.