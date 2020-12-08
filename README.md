# Python Boilerplate Cookiecutter

## Como usar?

Primeiramente garanta que você tem o cookiecutter instaaldo no seu PATH.

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
|-- docs
|   |-- _sources
|   |   `-- index.rst.txt
|   |-- _static
|   |   |-- _stemmer.js
|   |   |-- alabaster.css
|   |   |-- basic.css
|   |   |-- custom.css
|   |   |-- doctools.js
|   |   |-- documentation_options.js
|   |   |-- file.png
|   |   |-- jquery-3.5.1.js
|   |   |-- jquery.js
|   |   |-- language_data.js
|   |   |-- minus.png
|   |   |-- plus.png
|   |   |-- pygments.css
|   |   |-- searchtools.js
|   |   |-- translations.js
|   |   |-- underscore-1.3.1.js
|   |   `-- underscore.js
|   |-- genindex.html
|   |-- index.html
|   |-- objects.inv
|   |-- search.html
|   `-- searchindex.js
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

## Como ajudar?

TODO
