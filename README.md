# IST3134 – Big Data Analytics in Cloud  
## Sentiment Analysis of Spotify Google Reviews using Hadoop Streaming and PySpark

### Introduction  
Hi, we are from the **IST3134 Big Data Analytics in Cloud** of Sunway University.  
Our group members are:  
- **Inpik Deern**  
- **Lim Chun Yi**  
- **Teo Jia Le**  

This GitHub repository contains the source codes, scripts, and related files for our sentiment analysis project on the **Spotify Google Reviews Dataset**.  
The project implements two big data processing approaches — **Hadoop Streaming** and **PySpark** — to compare their performance, processing methodologies, and sentiment classification outcomes. By exploring the dataset in a distributed computing environment, we aim to identify overall sentiment trends and user satisfaction levels from millions of user reviews.

---

### Our Project  
📖 The dataset used in this project was obtained from Kaggle:  
[Spotify Google Reviews Dataset – Kaggle](https://www.kaggle.com/datasets/ngchunyiu/spotify-google-reviews-dataset)  

Due to its large size (625MB, 3.4M reviews), the full dataset is not included in this repository.  

**Analysis Workflow:**  
1. **Data Storage:** Stored in Amazon S3 for scalable access.  
2. **Hadoop Streaming:** Implemented Python MapReduce jobs for sentiment classification.  
3. **PySpark:** Used Spark’s DataFrame API and MLlib for sentiment analysis.  
4. **Performance Comparison:** Compared methodologies and results between both frameworks.  

---

### Repository Structure  
