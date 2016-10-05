#Grupo It in Dublin - BR

[![Build Status](https://travis-ci.org/itindublin/itindublin.github.io.svg?branch=develop)](https://travis-ci.org/itindublin/itindublin.github.io)

[![npm version](https://badge.fury.io/js/npm.svg)](https://badge.fury.io/js/npm)
[![npm version](https://badge.fury.io/js/bower.svg)](https://badge.fury.io/js/bower)

# [Site do Grupo](https://itindublin.github.io/)


## Summary

- [About](#about)
- [Request](#request)
- [Dependencies](#dependencies)
- [Contributing](#contributing)



Seja bem vindo!

Costumamos nos encontrar todo primeiro sábado do mês, às 18:00,

Local: Pub "Doyles In Town" - www.doylesintown.com
9 College Street, Dublin 2
Próximo à Trinity College e ao Bank of Ireland
[https://goo.gl/maps/GBhYSCg9JUm](https://goo.gl/maps/GBhYSCg9JUm)
Chegando lá subam as escadas. Perguntem no bar pelo "IT Meetup" caso não encontrem.

Temos uma lista de discussão nos grupos do google, [https://groups.google.com/forum/#!forum/it-irlanda-br](https://groups.google.com/forum/#!forum/it-irlanda-br)

Um grupo no slack [http://itindublin.slack.com/messages/general/](http://itindublin.slack.com/messages/general/)

Veja aqui como contribuir com a [wiki](https://itindublin.github.io/como-contribuir-com-a-wiki)
ou postar artigos no [blog](https://itindublin.github.io/como-publicar-um-artigo).


***


###Rodando o projeto localmente

Se você é programador ou tem o minimo de conhecimento de Python siga
as instruções abaixo para rodar o projeto na sua máquina.

####Fork do Repositório

- Faça um fork desse repositório
- Faça um clone do seu fork


    git clone  git@github.com:usuario/ITinDublin.github.io


####Preparando o Ambiente

Criar o ambiente de uso do Pelican é muito simples, pra isso você vai precisar de:

- Python 2.7;
- VirtualEnv;

Primeiro abra um terminal e crie um [virtualenv][https://virtualenv.readthedocs.io/en/latest/]
para o Python 2.7 (note que este passo não é obrigatório, mas é uma boa prática):
O virtualenv pode ser criado em qualquer pasta, mas
caso crie dentro da pasta do projeto pode usar o nome de _.venv_ que a pasta sera ignorada pelo github

####Instalar dependências

- Entrar na pasta do projeto
- Com o virtualenv ativado instale as dependências.


    pip install -r requirements.txt

####Rodar Projeto

Para rodar o projeto existem duas formas:

######Utilizando os comandos _make_


    make html

O comando _make html_ irá gerar todo html do site e jogar na pasta _output_ .
Agora vamos iniciar o servidor


    make serve

Pronto servidor iniciado, acesse http://localhost:8000/

A cada alteração nos arquivos do projeto é necessário rodar os comandos novamente.

######Utilizando script

Iniciando o servidor por esse script é possível testar o site localmente enquanto você realiza as modificações.

Para utilizar o script para iniciar basta executar o comando:


    ./develop_server.sh start


Então basta visitar o endereço http://localhost:8000/

Para finalizar o servidor use:


    ./develop_server.sh stop


Após realizar as alterações e testes, faça o commit para o seu repositório local e depois nos envie um PULL Request.



## Contributing


em fases de testes:

Grunt

Npm

Grunt Tasks

```json
"grunt-contrib-concat": "*",
"grunt-contrib-cssmin": "^1.0.2",

```


