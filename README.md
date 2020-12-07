# {{cookiecutter.project_name}}

A ideia desse projeto é já ser um "start" para seu projeto python. O que temos aqui são configurações pré prontas para que você possa se dedicar inteiramente ao código do seu projeto.


## Pipfile

O Pipfile já tráz algumas dependencias de desenvolvimento, como:

```
asynctest = "==0.12.1"
pytest = "==6.1.2"
pytest-cov = "==2.10.1"
pytest-mock = "==3.3.1"
codecov = "==2.0.17"
mypy = "==0.782"
black = "==19.10b0"
isort = "==5.1.4"
lxml = "==4.6.2"
sphinx = "==3.2.1"
sphinx-issues = "==1.2.0"
sphinx-intl = "==2.0.1"
safety = "==1.9.0"
flake8 = "==3.8.4"
flake8-bugbear = "==20.11.1"
bandit = "==1.6.3"
pre-commit = "==2.9.2"
```

O Pipfile já vem com alguns scripts que ajudam nas tarefas do dia a dia e nas checagens do CI.

- ``pipenv run test``

    Roda os testes do projeto. Esse script está configurado para medir a cobertura do pacote ``{{cookiecutter.project_name}}``. Esse pacote deve ser ajustado para o pacote onde seu código vai ficar.

- ``pipenv run lint``

    Roda o ``mypy`` para fazer checagem estática de tipos no código.

- ``pipenv run fmt`` e ``pipenv run fmt-check``

    Roda o black para formatar o código. O comando ``pipenv run fmt-check`` apenas checa se alguma formatação seria necessária. É útil para rodar no processo de CI.

- ``pipenv run isort`` e ``pipenv run isort-check``

    Formata o código ordenando os imports usando o projeto isort. O comando ``pipenv run isort-check`` apenas checa se algum import precisa ser reformatado. É útil para rodar no processo de CI.


# Pre-commit Hooks

Ao instalar o `pre-commit`, todas as vezes que realizar um novo commit, será checado todos os pontos de qualidade do
codigo, como codestyle, testes, imports e por aí vai.

Os comandos abaixo devem ser executados apenas quando é feito o clone do projeto.

```shell
pre-commit install
pre-commit install --hook-type pre-puh
```

# CI/CD

Esse repositorio já possui alguns workflows do Github Actions pré-configurados. Os workflows são:

- `.github/workflows/pull-request.yaml`

    Esse workflow roda em cada PR aberto no projeto. Roda os testes em múltiplas versões do python e faz checagem de formatação de código, lint (com mypy) e formatação de imports (com isort).

    Esse workflow faz também upload do relatório de coverage para o [codeclimate](https://codeclimate.com). Perceba que o upload é feito em apenas um versão do python, isso porque o codeclimate rejeita múltiplos upload para um mesmo commit, então precisamos escolher uma das rodadas de teste para fazer o upload.

    Para que o upload para o codeclimate funciona você precisa criar um token no CodeClimate e colocar esse token como um secret no seu repositório. O Nome do secret **deve ser**: ``CC_TEST_REPORTER_ID``. Mais sobre a documentação do codeclimate com githubactions: https://docs.codeclimate.com/docs/github-actions-test-coverage

## Changelog Automático

Esse projeto já vem com o [release-drafter](https://github.com/release-drafter/release-drafter) configurado. Dessa forma, a cada PR megeado na branch [``main``](https://github.blog/changelog/2020-10-01-the-default-branch-for-newly-created-repositories-is-now-main/) (e também na ``master`` para repositório legados) uma Release Draft será atualizada mencionando esse PR.

Para fazer uso dessa opção, basta criar quatro labels em seu projeto:

- ``feature``
- ``bug``
- ``docs``
- ``breaking-change``

Todos os PRs que tievem uma (ou mais) dessas labels e forem mergeados pra branch principal, uma release Draft será automaticamente atualizada.

Essa configuração do release-drafter também já calcula a próxima versão baseado no [SemVer](https://semver.org). A configuração é a seguinte:

- A label ``breaking-change`` aumenta a ``major`` version;
- A label ``feature`` aumenta a ``minor`` version;
- A label ``bug`` aumenta a ``patch`` version;
- PR sem label também aumenta a ``patch`` version;

Não se esqueça de de ajustar o links para o seu projeto no arquivo ``.github/release-drafter.yml``.

# Pydantic - Configuração baseada em variáveis de ambiente

Para facilitar na criação de um novo serviço e seguindo as boas práticas definidas no [12factors](https://12factor.net/config) sobre configurações.
Adicionamos o uso no pydantic para criar e validar essas informações para nós.

Exemplo de uso:

```python
    from config import settings

    print(settings.DEBUG)
```

Para configurar uma variável de ambiente é necessário ficar atento ao prefixo.
o default do projeto verificar inicialmente para uma variável de ambiente chamada `NAMESPACE`caso não a
encontre o prefixo será `DEV_`, o que isso significa?

O uso ficará da seguinte forma quando configuramos o namespace sempre adicionaremos o prefixo no
momento de exportar as variaveis de ambiente.

```python
    NAMESPACE=PROD PROD_DEBUG=False python main.py
```

Caso não definimos nenhum namespace, o prefixo será `DEV`, ou seja

```python
    DEV_REDIS_PORT=1234 python main.py
```

Lembrando que dentro da sua aplicação o que vale é justamente o nome que foi definido no arquivo config.py, sem o prefixo.



# Sphinx Docs

Esse repositório tem o sphinx configurado. Isso premite escrever a documentação do seu projeto e até mesmo usar o Github Pages para hospedá-la.

Antes de começar a usar, ajuste as variáveis no início do arquivo ``docs-src/conf.py``. A documentação, em formato html, é gerada na pasta ``docs/``.

Para gerar a documentação basta rodar: ``pipenv run make-docs``.

Para conseguir gerar a documentação é preciso ter o ``make`` instalado.
