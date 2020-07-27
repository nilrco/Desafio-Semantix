
## 1 - Qual  o  objetivo do comando cache em Spark ?
**R: O comando cache é responsavel por armazenar os dados em memoria, ele deve ser utilizando quando você deseja reutilizar os dados em diversos processos dentro do seu código ou para armazenar esses dados em mémoria após operações complexas facilitando assim a sua recuperação em caso de falhas.**

## 2 - O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce.Por quê ?
**R: Porque o Spark pode realizar todo o processamento em memória, enquanto o MapReduce necessita executar gravação e leitura em disco durante o processamento que consequementente é mais lento.**

## 3 - Qual é a função do SparkContext ?
**R: O SparkContext é um ponto de entrada para todas as funcionalidades do Spark, facilitando assim o acesso da sua aplicação ao cluster. Ele da as coordenadas de varias aplicações Spark dentro do cluster.
É necessario realizar a criação do SparkConf antes do SparkContext, caso você esteja utilziando Spark-shell essas criações são realizadas de forma automatica.**

## 4 - Explique com suas palavras o que é *Resilient Distributed Datasets (RDD)*.
**R: É uma coleção distribuída imutável de elementos de seus dados, que fica particionada entre os nós do cluster que pode ser operada por uma API de baixo nível que oferece tranformações e ações. RDD's não podem ser modificados diretamente portanto a cada operação é necessario realizar uma criação de novos RDD's, outro ponto é que eles são altamentes tolerantes a falhas e operão em paralelo caso neccessário.**

## 5 - GroupByKey é  menos eficiente que reduceByKey em grandes dataset.Por quê?
**R: Utilizar reduceByKey funciona melhor em grande conjunto de dados. Isso ocorre porque o Spark sabe combinar a saída com uma chave comum em cada partição antes de embaralhar os dados pelo cluster, gerando assim menor trafego de dados na rede.**

## Explique o que o código Scala abaixo faz.
val textFile = sc.textFile("hdfs://...") <br>
val counts = textFile.flatMap(line=>line.split(" ")) <br>
&nbsp;&nbsp;&nbsp;&nbsp;.map(word=>(word, 1))<br>
&nbsp;&nbsp;&nbsp;&nbsp;.reduceByKey(_+ _)<br>
counts.saveAsTextFile("hdfs://...")<br><br>
**R: Realiza a leitura de um arquivo texto do HDFS, apos isso processa uma contagem de palavras dentro de esse arquivo. Apos esse processamento salva o resultado em formato text dentro do hdfs**
