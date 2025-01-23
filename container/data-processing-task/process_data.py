from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()

# Load a sample CSV file into a Spark DataFrame
df = spark.read.csv("/app/data/sample_data.csv", header=True, inferSchema=True)

# Perform some data processing (e.g., calculate average of a column)
df_grouped = df.groupBy("category").agg({"value": "avg"})

# Show the processed data
df_grouped.show()

# Save the result as a new CSV file with overwrite mode
df_grouped.write.mode("overwrite").csv("/app/output/processed_data.csv")

# Stop the Spark session
spark.stop()
