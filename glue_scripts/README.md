### 🔄 ETL Pipeline Script — `trending_etl_job.py`

This AWS Glue ETL script performs the following tasks:
- Reads trending video data from the AWS Glue Data Catalog (`db_youtube_raw.raw_statistics`)
- Filters for specific regions (`'ca'`, `'gb'`, `'us'`) using push-down predicate
- Maps and transforms the schema using `ApplyMapping`
- Resolves column type choices and removes null fields
- Writes the output as **partitioned Parquet** files to Amazon S3 in:



📁 **Input Table**: `de_youtube_raw.raw_statistics`  
📦 **Output Format**: Parquet  
🗃️ **Partition Key**: `region`  
🌐 **S3 Output Bucket**: `de-on-youtube-cleansed-useast1-dev`

> Script path: [`glue_scripts/trending_etl_job.py`](glue_scripts/trending_etl_job.py)
