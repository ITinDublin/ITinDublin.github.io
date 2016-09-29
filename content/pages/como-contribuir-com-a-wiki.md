Title: Como contribuir com a Wiki
Template: page

Pensando na possibilidade de mantermos um site para a comunidade de maneira mais colaborativa onde qualquer um possa contribuir com conteúdo de maneira rápida, surgiu a idéia de utilizarmos o GitHub Pages.

Este projeto utiliza [Pelican](http://blog.getpelican.com/) como gerador de páginas estáticas e [Travis-CI](https://travis-ci.org/) para realizar a integração contínua.


Repo: [https://github.com/itindublin/itindublin.github.io](https://github.com/itindublin/itindublin.github.io)


##Vantagens

1. Basta ter uma conta no GitHub
2. Edição via internet
3. Site sem senha e com versionamento

Todos podem contribuir com o conteúdo do wiki

Se vc nao tem conhecimento de git ou github apenas crie um issue você precisa apenas de uma conta do github para fazer isso.

##Criando uma Página na wiki

Para criar uma página na wiki, você pode olhar o exemplo de uma página no diretório `_content/pages/wiki_`.  
O seu arquivo deve ser criado nessa pasta.  
O Pelican suporta a linguagem de marcação ReStructured Text e Markdown . 

Uma página tem que ter obrigatóriamente um cabeçalho fixo, conforme abaixo (em ReST):


    Título da Sua Página
    ====================
    
Ou em Markdown:


    Title: Título da Sua Página

Após esse cabeçalho você pode escrever de acordo com a linguagem de marcação escolhida.


**Importante**  

- Por padronização o nome do arquivo deve ser o título da página em caixa baixa separada por `-`  
  ex: _titulo-da-pagina_   

  
Caso tenha dificuldades para escrever Markdown ou reStructuredText, veja esses editores online que auxiliam sua escrita:

 - [StackEdit](https://stackedit-beta.herokuapp.com)  
 - [Dillinger](http://dillinger.io/)  
 - [Prose](http://prose.io/)

  