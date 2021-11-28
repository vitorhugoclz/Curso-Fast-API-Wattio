# Como Executar projeto

crie um ambiente [https://docs.python.org/pt-br/3/library/venv.html](virtual python) e inicializa. Após inicializar o ambiente instale as dependencias contidas em 
`requirements.txt` com comando abaixo

```pip install -r requirements.txt```

Já com as dependecias instaladas execute o comando a seguir para inicializar o banco de dados

```alembic upgrade head```

Após inicializar o banco de dados no diretório raiz do projeto execute o comando para iniciar a aplicação

```uvicorn main:app```

caso ocorra conflito na porta padrão (8000) é possível especificar a porta com comando `--port` e logo afrente o numero da porta TCP a ser utilizada

Para verificar o swagger da aplicação e fazer alguns testes basta acessar a url [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) caso tenha trocado a porta troque o valor 8000 pelo da porta selecionada.

