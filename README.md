# HTTP requests to the NASA Kennedy Space Center WWW server

Projeto baseado em tese de proficiência de spark divido em duas partes

Parte 1 - Responder de forma dissertativa as questão que estão no arquivo desafio engenheiro de dados.pdf.

As respostas para esse desafio estão no arquivo respostas.md

Parte 2 - Realizar algumas tratavidas no dataset Nasa Kennedy Space Center WWW server.

[Fonte oficial do dateset](http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html)

Dados:

 - [Jul 01 to Jul 31, ASCII format, 20.7 MB gzip compressed] <a>ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz</a>, 205.2MB.
 - [Aug 04 to Aug 31, ASCII format, 21.8 MB gzip compressed] <a>ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz</a>, 167.8 MB.

Sobre o dataset: Esses dois conjuntos de dados possuem todas as requisições HTTP para o servidor da NASA Kennedy
Space Center WWW na Flórida para um período específico.
Os logs estão em arquivos ASCII com uma linha por requisição com as seguintes colunas:
- Host fazendo a requisição. Um hostname quando possível, caso contrário o endereço de internet se o nomenão puder ser identificado.
- Timestamp no formato "DIA/MÊS/ANO:HH:MM:SS TIMEZONE"
- Requisição(entre aspas)
- Código do retorno HTTP
- Total de bytes retornados

Questões <br>
Responda as seguintes questões devem ser desenvolvidas em Spark utilizando a sua linguagem de preferência.
1. Número de  hosts únicos.
2. O total de erros 404.
3. Os 5 URLs que mais causaram erro 404.
4. Quantidade de erros 404 por dia.
5. O total de bytes retornados.
