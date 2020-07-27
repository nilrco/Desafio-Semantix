# Importando as bibliotecas necessarias
import re
from pyspark import SparkContext
from pyspark.sql import Row, SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import (
    countDistinct, col, udf, sum)
from datetime import datetime


# Criação do SparkContext
sc = SparkContext("local", "Data Engineer")
spark = SparkSession(sc)

# Carregando os dados
aug = sc.textFile("NASA_access_log_Aug95.gz")
jul = sc.textFile("NASA_access_log_Jul95.gz")
log = aug.union(jul)

# Criação da função para realizar o pase dos dados
pattern = ""r'(.*) - - \[(.* -0400)\] \"(.*) (/.*[.]\D+)(\b| HTTP/1.0)\" (\d{3}) (.*)'""


def logParsing(log_line):
    line = re.search(pattern, log_line)

    if line is None:

        return "error"

    return Row(
        host=line.group(1),
        timestamp=line.group(2),
        url=line.group(4),
        http=line.group(6),
        bytes=(line.group(7)))


# Criação do RDD e DataFrame
log_rdd = log.map(logParsing).cache()
log_rdd = log_rdd.filter(lambda line: line != "error")

log_df = log_rdd.toDF()

# Questão 1 - Numero de hosts unicos
log_df.agg(countDistinct("host").alias("distinct_host")).show()

log_rdd.map(lambda row: row.host).distinct().count()

# Questão 2 - O total de erros 404.
error_df = log_df.filter("http = '404'")
error_df.count()

error_rdd = log_rdd.filter(lambda row: "404" in row.http)
error_rdd.count()

# Questão 3 - Os 5 URLs que mais causaram erro 404.
error_df.groupBy("url").count().orderBy(
    "count", ascending=False).show(5, truncate=False)

error_rdd.map(lambda row: (row.url, 1)).reduceByKey(
    lambda x, y: x+y).sortBy(lambda x: x[1], False).take(5)

# Questão 4 - Quantidade de erros 404 por dia.
day_rdd = error_rdd.map(lambda row:  (datetime.strptime(
    row.timestamp,  "%d/%b/%Y:%H:%M:%S -0400").strftime("%Y-%m-%d"), 1))     .reduceByKey(lambda x, y: x+y)
day_rdd.take(5)

func = udf(lambda x: datetime.strptime(x,  "%d/%b/%Y:%H:%M:%S -0400").strftime("%Y-%m-%d"))
day_df = error_df.groupBy(func(col("timestamp")).alias("date")).count()
day_df.show()

# Questão 5 - O total de bytes retornados.
bytes_rdd = log_rdd.filter(lambda row: "-" not in row.bytes)
bytes_rdd.map(lambda row: int(row.bytes)).sum()


bytes_df = log_rdd.filter(lambda row: "-" not in row.bytes).toDF()
bytes_df.withColumn("bytes", col("bytes").cast(IntegerType()))
bytes_df.agg(sum('bytes')).show()
