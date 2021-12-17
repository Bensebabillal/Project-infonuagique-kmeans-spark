import pandas as pd
from sodapy import Socrata

#paramètres de connexion au dataset
token = "he2su5CXKCNb092y0LyoBdFjH"
mail = "hodoco3185@keagenan.com"
password ="qwerty.0000"

#connexion au endpoint
client = Socrata("data.cityofchicago.org",
                 token,
                 mail,
                 password)

#requête d'aquisition des données de géolocalisation
results = client.get("ijzp-q8t2",select = "id, latitude, longitude", where = "latitude IS NOT NULL" ,limit = 100000)

# Convertion à pandas DataFrame
df = pd.DataFrame.from_records(results)
df["id"] = pd.to_numeric(df["id"], downcast = "integer")
df["latitude"] = pd.to_numeric(df["latitude"], downcast="float")
df["longitude"] = pd.to_numeric(df["longitude"], downcast="float")

from pyspark.sql import SparkSession

#initialisation d'une session spark pour une application "Demo" sur le cluster
masterURL = "spark://spark-master:7077"
#masterURL = "https://1934-132-213-165-116.ngrok.io"

spark = SparkSession.builder.\
        master(masterURL).\
        appName("TrainingModel").\
        config("spark.executor.memory", "512m").\
        getOrCreate()

data = spark.createDataFrame(df)

#construction de la structure qui sera en entrée pour notre algorithme kmeans
from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
                            inputCols=["latitude", "longitude"], 
                            outputCol="features")

data_features = assembler.transform(data)

#entrainement de l'algorithme sur un nombre de cluster = 6 et 10000 coordonnées
from pyspark.ml.clustering import KMeans

kmeans = KMeans(k=8, seed=2)  # 6 clusters here
model = kmeans.fit(data_features.select('features'))

from pyspark.ml.evaluation import ClusteringEvaluator
predictions = model.transform(data_features.select("features"))

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

model.save("./myModel/")