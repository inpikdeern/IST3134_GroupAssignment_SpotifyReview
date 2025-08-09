# IST3134 – Big Data Analytics in Cloud  
## Sentiment Analysis of Spotify Google Reviews using Hadoop Streaming and PySpark

### Introduction  
Hi, we are from the **IST3134 Big Data Analytics in Cloud** of Sunway University.  
Our group members are:  
- **Inpik Deern**  
- **Lim Chun Yi**  
- **Teo Jia Le**  

---

### Our Project  
📖 The dataset used in this project was obtained from Kaggle:  
[Spotify Google Reviews Dataset – Kaggle](https://www.kaggle.com/datasets/ngchunyiu/spotify-google-reviews-dataset)  

- **Size:** ~625 MB  
- **Records:** ~3,400,000 reviews  
- **Format:** CSV  
- **Columns:**
  | Column Name          | Description |
  |----------------------|-------------|
  | review_id            | Unique review identifier |
  | pseudo_author_id     | Pseudonymized author ID |
  | author_name          | Reviewer’s display name |
  | review_text          | Full review text |
  | review_rating        | Rating given by the user |
  | review_likes         | Number of likes for the review |
  | author_app_version   | App version used during review |
  | review_timestamp     | Timestamp of review submission |

> ⚠️ Due to size restrictions, the dataset is **not included** in this repository.

## 🛠️ Technologies Used
- **Amazon S3** for distributed data storage
- **Hadoop Streaming** for MapReduce-based processing
- **PySpark** for DataFrame-based distributed analysis
- **AWS EMR** / Hadoop cluster for execution environment
 
## 📊 Comparison
We compared:
- **Sentiment Counts**: Minor differences due to keyword matching methods and tokenization handling

---
**Thank you for visiting our repository!** 🎵
