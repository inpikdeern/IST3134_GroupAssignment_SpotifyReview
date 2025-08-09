from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

positive_keywords = ["good", "great", "excellent", "love", "awesome", "best", "amazing", "fantastic", "perfect"]
negative_keywords = ["bad", "worst", "terrible", "awful", "hate", "poor", "boring", "problem", "issue"]

def classify_sentiment(text):
    if text is None:
        return "neutral"
    text_lower = text.lower()
    if any(word in text_lower for word in positive_keywords):
        return "positive"
    elif any(word in text_lower for word in negative_keywords):
        return "negative"
    else:
        return "neutral"

sentiment_udf = udf(classify_sentiment, StringType())

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SpotifySentimentAnalysis").getOrCreate()

    df = spark.read.csv("s3://your-bucket-name/spotify_reviews.csv", header=True)

    df_with_sentiment = df.withColumn("sentiment", sentiment_udf(col("review_text")))

    result = df_with_sentiment.groupBy("sentiment").count()

    result.show()

    spark.stop()
