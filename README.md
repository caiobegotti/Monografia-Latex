Monografia-Latex
================

Template Latex para monografias da UFPR, de acordo com normas da ABNT (na medida do possível).

É um inferno formatar uma monografia, quanto mais nos padrões da ABNT, e com variações da universidade. E ainda em Latex. Então esse template serve para graduandos que são chatos com tipografia e qualidade gráfica da monografia, como eu fui.

![alt text](https://github.com/caio1982/Monografia-Latex/blob/master/Monografia.gif "Demo")

Como compilar
=============

Sugiro o TexMaker para editar e compilar o documento, mas se quiser fazer manualmente:

    pdflatex -shell-escape Monografia.tex

Para atualizar a bibliografia .bib:

    bibtex Monografia.bib
