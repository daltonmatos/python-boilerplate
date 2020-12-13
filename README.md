# Python Boilerplate Cookiecutter

## Como usar?

Primeiramente garanta que você tem o cookiecutter instalado no seu PATH.

```shell
sudo pip install cookiecutter
```

e então crie o seu projeto.

```shell
cookiecutter https://github.com/sixcodes/python-boilerplate.git
```

Após executar o comando acima, você receberá um questionario para responder de acordo com os dados do seu projeto.

As opções estão descritas no arquivo `cookiecutter.json`.

Ao executar essas serão os inputs necessários ou apenas `enter` para aceitar o valor default.

```shell
> cookiecutter https://github.com/sixcodes/python-boilerplate.git
project_name [e.g. 'six-toolbox']: sixcodes
package_name [sixcodes]:
package_version [0.0.1]:
short_description [Great python package]:
author [Jesue Junior]: Test boilerplate
author_email [opensource@sixcodes.com]:
author_username [sixcodes]:
url [https://github.com/sixcodes/sixcodes]:

```

A estrutura do seu projetode pastas e arquivos com esse template será:

```shell
sixcodes
|-- CODE_OF_CONDUCT.md
|-- LICENSE
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- docs-src
|   |-- Makefile
|   |-- _static
|   |-- conf.py
|   `-- index.rst
|-- mypy.ini
|-- pyproject.toml
|-- setup.py
|-- sixcodes
|   |-- __init__.py
|   `-- config.py
`-- tests
    |-- test_config.py
    `-- test_true.py

7 directories, 38 files
```

## O que esse boilerplate entrega


### Github Actions Workflows

O projeto criado já tras alguns workflows do Github Actions:

- `pull-request`: Workflow que roda a cada pull-request aberto. Roda os testes a checagens de lint, format, etc.
- `release`: A cada tag criada com o padrão `X.Y.Z` gera uma publicação no Pypi.

  Para essa publicação você precisa adicionar um secret ao projeto com nome `PYPI_TOKEN`. Mais detalhes na [documentação do Pypi](https://pypi.org/help/#apitoken):


### Pré-configuração para documentação com Sphinx

A configuração do [Sphinx](https://www.sphinx-doc.org/en/master/) já está pronta. O código-fonte da documentação fica em `docs-src/` e a documentação gerada fica em `docs/`, já pronta para ser servida pelo [Github Pages](https://pages.github.com/).

Para gerar sua documentação rode: `pipenv run make-docs`

## Como ajudar?

TODO
