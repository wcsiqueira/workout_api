
#  Resolução do Desafio Resumo :

**Primeira solicitação Query Parameters: Adicionados aos endpoints de consulta ,modificação em centro_treinamento/routers.py:Adicionamos nome e cpf como parâmetros opcionais na consulta (query),filtro Condicional: Usamos or_ para combinar filtros baseados nos parâmetros ,paginação  feita a adição dos parâmetros limit e offset para paginar os resultado

**Segunda solicitação Resposta Customizada: Definidos novos schemas e ajustados os endpoints para retornar a resposta customizada.
Modificação em centro_treinamento/schemas.py : Definir os schemas customizados de resposta

**Tereira Solicitação Exceção de Integridade: Manipulada e personalizada para retornar uma mensagem específica.

** Quarta Solicitação Paginação: Implementada usando a biblioteca fastapi-pagination
Modificação em centro_treinamento/routers.py

Paginação já foi adicionada nas alterações do endpoint query.
Ajustes no Modelo AtletaModel e CentroTreinamentoModel
Modificação em atleta/models.py adicione os campos nome, cpf, e categoria no modelo AtletaModel.

Obs: Foi necessário um ajuste : Modificação em centro_treinamento/models.py 
Assegurar que CentroTreinamentoModel tem o relacionamento correto com AtletaModel.

# Estrutura resolução desafio :
workout_api/
    contrib/
        __init__.py
        schemas.py
        router.py
         main.py
    centro_treinamento/
        __init__.py
        models.py
        schemas.py
        views.py
    atleta/
        __init__.py
        models.py
        schemas.py
        views.py



# FastAPI
### Quem é o FastAPi?
Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção.
FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

### Async
Código assíncrono apenas significa que a linguagem tem um jeito de dizer para o computador / programa que em certo ponto, ele terá que esperar por algo para finalizar em outro lugar

# Projeto
## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

## Modelagem de entidade e relacionamento - MER
![MER](/mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

## Execução da API

Para executar o projeto, utilizei a [pyenv](https://github.com/pyenv/pyenv), com a versão 3.11.4 do `python` para o ambiente virtual.

Caso opte por usar pyenv, após instalar, execute:

```bash
pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
```
Para subir o banco de dados, caso não tenha o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
make run-docker
```
Para criar uma migration nova, execute:

```bash
make create-migrations d="nome_da_migration"
```

Para criar o banco de dados, execute:

```bash
make run-migrations
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs


   


# Desafio Final
    - adicionar query parameters nos endpoints
        - atleta
            - nome
            - cpf
            - 
    - customizar response de retorno de endpoints
        - get all
            - atleta
                - nome
                - centro_treinamento
                - categoria
    - Manipular exceção de integridade dos dados em cada módulo/tabela
        - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
        - status_code: 303
    - Adicionar paginação utilizando a lib: fastapi-pagination
        - limit e offset
# Referências

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/