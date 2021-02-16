from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
import requests
from pyspark.sql.types import BooleanType


def validateUrl(url):
    try:
        r = requests.head(url)
        if r.status_code >= 200 and r.status_code < 400:
            return True
        return False
    except:
        return False

validateUrlUDF = udf(validateUrl, BooleanType())

def checkValidUrls(frame):
    frame = frame.filter(validateUrlUDF(frame.url))
    frame.show()

