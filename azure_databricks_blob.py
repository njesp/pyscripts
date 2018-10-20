"""
# Azure CLI upload filer
az login
az storage blob upload  --account-key CtdikXCQ9HLxzsBj3VKf2bF61NDdJLzZ2MElUdoxkFMIl3UZDCftv9dOSBSuFgfoO95nEV1DEK4ZF3gHdF3ZTg== --account-name njn2blob --container-name mappe --file c:/temp/projekt_db_gb.csv --name projekt_db_gb.csv
az storage blob upload  --account-key CtdikXCQ9HLxzsBj3VKf2bF61NDdJLzZ2MElUdoxkFMIl3UZDCftv9dOSBSuFgfoO95nEV1DEK4ZF3gHdF3ZTg== --account-name njn2blob --container-name mappe --file c:/temp/projekt-kontor.csv --name projekt-kontor.csv	
#
"""
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType
from pyspark.sql.functions import sum, desc
# Skaf et håndtag til underliggende Spark (kan være lokal maskine, eller cluster på 1000 maskiner, eller noget imellem)
spark = SparkSession.builder.getOrCreate()
# Set Blob storage op
spark.conf.set("fs.azure.account.key.njn2blob.blob.core.windows.net",
               "CtdikXCQ9HLxzsBj3VKf2bF61NDdJLzZ2MElUdoxkFMIl3UZDCftv9dOSBSuFgfoO95nEV1DEK4ZF3gHdF3ZTg==")
# Indlæs oversigt over Oracle projekter og deres fordeling af pladsforbrug på databaser
projekt_db_gb_type = StructType([
    StructField("projekt", StringType(), True),
    StructField("db", StringType(), True),
    StructField("gbytes", IntegerType(), True)])
projekt_db_gb = spark.read.schema(projekt_db_gb_type).option("header", "true").option(
    "delimiter", ";").csv("wasbs://mappe@njn2blob.blob.core.windows.net/projekt_db_gb.csv")
# Aggreger databasen væk. Resulatet er projektfordelte gbytes.
projekt_gb = projekt_db_gb.groupBy(
    "projekt").agg(sum("gbytes").alias("gbytes"))
# Indlæs oversigt over Oracle projekter og tilhørsfolrhold tik kontorer
projekt_kontor_type = StructType([
    StructField("projekt", StringType(), True),
    StructField("projekt_ejer_kontor", IntegerType(), True)])
projekt_kontor = spark.read.schema(projekt_kontor_type).option("header", "true").option(
    "delimiter", ";").csv("wasbs://mappe@njn2blob.blob.core.windows.net/projekt-kontor.csv").distinct()
# Join dataframes sammen og aggreger, the Spark way
joinExp = projekt_kontor["projekt"] == projekt_gb['projekt']
kontor_gb = projekt_kontor.join(projekt_gb, joinExp).select(
    "projekt_ejer_kontor", "gbytes").groupBy("projekt_ejer_kontor").agg(sum("gbytes").alias("gbytes"))
kontor_gb.sort(desc("gbytes")).show()
# Gammeldags SQL med join og group by
projekt_gb.createOrReplaceTempView("projekt_gb")
projekt_kontor.createOrReplaceTempView("projekt_kontor")
sql_text = """\n
select c.projekt_ejer_kontor, sum (c.gbytes) gbytes
    from (select a.gbytes,
                 b.projekt_ejer_kontor
            from projekt_gb a join projekt_kontor b on a.projekt = b.projekt) c
group by c.projekt_ejer_kontor
"""
spark.sql(sql_text).sort(desc("gbytes")).show()
