Title: Como publicar um artigo
Template: page


##Escrevendo um Artigo para o Blog

Para escrever um artigo para o blog, é necessário apenas criar um arquivo no formato (.rst ou .md) que são linguagens de marcação aceitas pelo Pelican.
Esse arquivo deve ser criado dentro do diretório _``content/articles``_ 

 Um artigo tem um cabeçalho fixo, conforme abaixo (em ReST):


    Título da Página
    ================
    :date: 2015-07-22 14:57
    :author: Nome do Autor
    :category: Tutoriais
    :tags: tutorial, tecnico, pelican, site
    :image: /images/monty-python-knights.jpg

Ou em Markdown:


    Title: Título da Página
    Date: 2015-07-22 14:57
    Author: Nome do Autor
    Category: Tutoriais
    Tags: tutorial, tecnico, pelican, site
    Image: /images/monty-python-knights.jpg

Novamente é tudo muito intuitivo, temos o título do artigo (a primeira linha em ReST, ou a precedida por ``Title:`` em Markdown) 
seguido da data de publicação (no formato ``YYYY-MM-DD HH:MM``).   
Logo abaixo temos o nome do autor, categoria e uma lista de tags. 

A Tag ``:image::`` ou ``Image:`` (em Markdown) faz referência à imagem de capa do artigo, mas é opcional.

Após esse cabeçalho você pode escrever de acordo com a linguagem de marcação escolhida.
 
**Referência:**     
O Modelo deste site foi construido utilizando como referência o site do Grupy-df cuja o link encontra-se abaixo.  
[http://df.python.org.br/blog/como-publicar-no-blog-do-grupy-df/](http://df.python.org.br/blog/como-publicar-no-blog-do-grupy-df/) 
