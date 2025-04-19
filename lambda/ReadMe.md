# 🔄 Lambda: JSON to Parquet Data Transformation Pipeline

This AWS Lambda function is triggered by an S3 `ObjectCreated` event. It ingests **semi-structured YouTube JSON data**, normalizes the nested structure using `pandas`, and stores the cleaned data as **partitioned Parquet** files into the **cleansed S3 layer**, while updating the AWS Glue Data Catalog for downstream analytics.

---


## ⚙️ Environment Variables Required

| Variable Name                  | Description                                            |
|-------------------------------|--------------------------------------------------------|
| `s3_cleansed_layer`           | S3 path to write cleansed Parquet files               |
| `glue_catalog_db_name`        | AWS Glue database name                                |
| `glue_catalog_table_name`     | AWS Glue table name                                   |
| `write_data_operation`        | Mode of write operation (`overwrite`, `append`, etc.) |

---

## 🧠 Key Features

- 📥 **Reads JSON from S3** (triggered via `ObjectCreated` event)
- 🧹 **Flattens nested JSON** using `pandas.json_normalize()`
- 💾 **Stores data in Parquet format** to `s3_cleansed_layer`
- 🗂️ **Updates Glue Catalog** via `awswrangler.s3.to_parquet()`
- 💡 Supports dynamic write operations (append/overwrite)

---

## 🧪 Sample IAM Permissions

Ensure your Lambda function has access to:
- S3 buckets (read from raw, write to cleansed)
- Glue Data Catalog
- CloudWatch Logs

Example policy snippet:

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "glue:UpdateTable",
    "glue:GetTable",
    "glue:CreateTable"
  ],
  "Resource": "*"
}
