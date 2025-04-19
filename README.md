# 🎬 TrendStream-YouTube-Data-Engineering

This project analyzes YouTube trending video data using a full-stack AWS data pipeline. It processes structured and semi-structured data from various regions, builds an ETL workflow, stores data in a central data lake, and visualizes key insights through Amazon QuickSight.

---

## 📌 Goals

- 🔽 **Data Ingestion**: Ingest YouTube trending data from Kaggle
- 🔄 **ETL System**: Clean and transform CSV and JSON files for querying
- 🧊 **Data Lake**: Centralize all raw and processed data in **Amazon S3**
- ⚙️ **Scalability**: Architect solution to scale for multi-region datasets
- ☁️ **Cloud**: Leverage **AWS services** to handle large-scale data
- 📊 **Reporting**: Create dashboards in **Amazon QuickSight**

---

## 🛠️ AWS Services Used

| Service       | Purpose                                                  |
|---------------|----------------------------------------------------------|
| **S3**        | Store raw and processed data                             |
| **AWS IAM**   | Secure access control and permissions                    |
| **AWS Glue**  | ETL jobs to clean and transform data                     |
| **AWS Lambda**| Trigger ETL pipelines automatically                      |
| **AWS Athena**| Run interactive queries directly on S3                   |
| **QuickSight**| Visualize and report key metrics and trends              |

---

## 🗃️ Dataset

- **Source**: [Kaggle - Trending YouTube Videos Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- **Description**: Contains daily trending video data across multiple countries
- **Format**: CSV & JSON

| Field | Description |
|-------|-------------|
| title | Video title |
| views | View count |
| likes | Like count |
| category_id | Category of the video |
| description | Video description |
| ... | and more |

---

## 📈 Key Features

- ✅ Multi-region support (e.g., US, IN, GB)
- ✅ Automated ETL using **Glue Jobs**
- ✅ Serverless orchestration using **Lambda**
- ✅ SQL queries with **Athena**
- ✅ Insightful dashboards via **QuickSight**

---

## 📂 Project Structure

```bash
data/                    # Raw & processed data
notebooks/               # EDA and data prep notebooks
lambda/                  # AWS Lambda functions
queries/                 # SQL scripts for Athena
dashboards/              # Dashboards & screenshots
README.md                # You're here!
requirements.txt         # Dependencies (boto3, pandas, etc.)
