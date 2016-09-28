Title: Teste

Pensando na possibilidade de mantermos um site para a comunidade de maneira mais colaborativa onde qualquer um possa contribuir com conteúdo de maneira rápida, surgiu a idéia de utilizarmos o GitHub Pages.

Este projeto utiliza [Pelican](http://blog.getpelican.com/) como gerador de páginas estáticas e [Travis-CI](https://travis-ci.org/) para realizar a integração contínua.


##Vantagens

1. Basta ter uma conta no GitHub
2. Edição via internet
3. Site sem senha e com versionamento

Todos podem contribuir com o conteúdo do wiki

Se vc nao tem conhecimento de git ou github apenas crie um issue você precisa apenas de uma conta do github para fazer isso.

##Criando uma Página na wiki

Para criar uma página na wiki, você pode olhar o exemplo de uma página no diretório ``pages/``.
O Pelican suporta a linguagem de marcação ReStructured Text e Markdown . 

Uma página tem um cabeçalho fixo, conforme abaixo (em ReST):

.. code-blocK:: rst

    Título da Sua Página
    =================================
    
Ou em Markdown:

.. code-blocK:: markdown

    Title: Como Publicar No Blog Do Grupy-Df
    Date: 2015-07-22 14:57
    Author: Magnun Leno
    Category: Tutoriais
    Tags: tutorial, tecnico, pelican, site
    Image: /images/monty-python-knights.jpg


