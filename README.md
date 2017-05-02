# Grupo It in Dublin 🇧🇷
> [Site do Grupo](https://itindublin.github.io/)

[![Build Status](https://travis-ci.org/ITinDublin/ITinDublin.github.io.svg?branch=develop)](https://travis-ci.org/ITinDublin/ITinDublin.github.io)
[![npm version](https://badge.fury.io/js/npm.svg)](https://badge.fury.io/js/npm)
[![npm version](https://badge.fury.io/js/bower.svg)](https://badge.fury.io/js/bower)

## Sumário

- [Sobre](#sobre)
- [Rodando o projeto localmente](#repositorio-local)
- [Contribuição](#contruibuicao) 

## <a name="sobre"></a>Seja Bem-Vindo!

### Encontros
Costumamos nos encontrar todo primeiro sábado do mês, às 18:00.

* **Local:** Pub _[Doyles In Town](www.doylesintown.com)_
* **Endereço:** [9 College Street, Dublin 2](https://goo.gl/maps/GBhYSCg9JUm) (Próximo à Trinity College e ao Bank of Ireland)

Chegando lá, suba as escadas. Caso não encontre, perguntem no bar pelo "**IT Meetup**".

### Discussões
Temos alguns canais para discurtimos coisas relacionadas sobre a área de IT em Dublin e tópicos relacionados:

* [Grupo do Google](https://groups.google.com/forum/#!forum/it-irlanda-br)
* [Grupo no Slack](http://itindublin.slack.com/messages/general/)
* [Site do Grupo](https://itindublin.github.io/)
* [Wiki](https://itindublin.github.io/wiki)

***

## <a name="repositorio-local"></a>Rodando o projeto localmente

Se você é programador ou tem o minimo de conhecimento de Python siga
as instruções abaixo para rodar o projeto na sua máquina.

> Este projeto utiliza o Pelican. Assim, antes de mais nada é preciso ter instalado em sua máquina:
> - Python 2.7
> - VirtualEnv


1. Faça um fork deste repositório no seu github e em seguida, faça o clone dele em sua máquina:

```sh
$ git clone  git@github.com:usuario/ITinDublin.github.io
```

2. Abra o terminal e crie um [virtualenv](https://virtualenv.readthedocs.io/en/latest/) para o  Python 2.7 (note que este passo não é obrigatório, mas é uma boa prática). O virtualenv pode ser criado em qualquer pasta, mas caso crie dentro da pasta do projeto pode usar o nome de _.venv_ que a pasta sera ignorada pelo git.

### Instalando as dependências

1. Entre na pasta do projeto:
```sh
$ cd ITinDublin.github.io
```

2. Com o virtualenv ativado instale as dependências:
```sh
$ pip install -r requirements.txt
```

### Rodando o Projeto

Existem duas maneiras para executar o projeto:

#### Utilizando os comandos _make_

O comando _make html_ irá gerar todo html do site e jogar na pasta _output_ .

```sh
$ make html
```

Agora vamos iniciar o servidor

```language
$ make serve
```

Agora basta acessar o seu iplocal na porta 8000: 
> http://localhost:8000/

A cada alteração nos arquivos do projeto é necessário rodar os comandos novamente.

#### Utilizando script

Iniciando o servidor por esse script é possível testar o site localmente enquanto você realiza as modificações.

Para utilizar o script para iniciar basta executar o comando:

```sh
$ ./develop_server.sh start
```

Agora basta acessar o seu iplocal na porta 8000: 
> http://localhost:8000/

Para encerrar o servidor utilize o comando:

```sh
$ ./develop_server.sh stop
```

Após realizar as alterações e testes, faça o commit para o seu repositório local e depois nos envie um **Pull Request**.


## <a name="contruibuicao"></a>Gostaria de contribuir?

Não possui conhecimento em desenvolvimento ou github? Sem problema, apenas crie um issue clicando [aqui](https://github.com/ITinDublin/ITinDublin.github.io//issues/new?title=New%20Request:) e contribua!

Você pode adicionar *fontes*, *imagens* ou qualquer arquivo que desejar.

Também é possível [contribuir com a nossa wiki](https://itindublin.github.io/como-contribuir-com-a-wiki)  ou [postar artigos no Blog](https://itindublin.github.io/como-publicar-um-artigo).



## Em fase de Testes

Grunt

Npm

Grunt Tasks

```json
"grunt-contrib-concat": "*",
"grunt-contrib-cssmin": "^1.0.2",

```