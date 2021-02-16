from pyspark.sql import SparkSession

PATH = 'C:/Users/jerry/PycharmProjects/ETLUrlValidator/input/urls.csv'

def readCSV():
    spark = SparkSession.builder \
        .master('local') \
        .appName('urlExtract') \
        .config("k1", "v1") \
        .getOrCreate()

    spark.sparkContext.addFile(PATH)
    return spark.read.csv(PATH, header=True)
