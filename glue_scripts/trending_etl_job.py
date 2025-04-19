# Import necessary libraries for Glue ETL operations
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

# Initialize Glue job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Create Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# ========== DATA EXTRACTION ========== #
# Define predicate pushdown to filter specific regions during data load
predicate_pushdown = "region in ('ca','gb','us')"

# Create DynamicFrame from Glue Data Catalog (Raw Data Source)
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="de_youtube_raw",
    table_name="raw_statistics",
    transformation_ctx="datasource0",
    push_down_predicate=predicate_pushdown  # Apply region filter at source
)

# ========== DATA TRANSFORMATION ========== #
# Apply schema mapping to standardize column names and data types
applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        # (current_name, current_type, new_name, new_type)
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "long", "category_id", "long"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "long", "views", "long"),
        ("likes", "long", "likes", "long"),
        ("dislikes", "long", "dislikes", "long"),
        ("comment_count", "long", "comment_count", "long"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "boolean", "comments_disabled", "boolean"),
        ("ratings_disabled", "boolean", "ratings_disabled", "boolean"),
        ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"),
        ("description", "string", "description", "string"),
        ("region", "string", "region", "string")  # Partition key
    ],
    transformation_ctx="applymapping1"
)

# Handle any data type conflicts in the dataset
resolvechoice2 = ResolveChoice.apply(
    frame=applymapping1,
    choice="make_struct",  # Convert ambiguous fields to struct type
    transformation_ctx="resolvechoice2"
)

# Remove records with null values in critical fields
dropnullfields3 = DropNullFields.apply(
    frame=resolvechoice2,
    transformation_ctx="dropnullfields3"
)

# ========== DATA LOADING ========== #
# Optimize file size by coalescing to 1 file per partition
# (Adjust based on actual data volume - 1 file for demo purposes)
datasink1 = dropnullfields3.toDF().coalesce(1)

# Convert back to DynamicFrame for Glue sink operations
df_final_output = DynamicFrame.fromDF(datasink1, glueContext, "df_final_output")

# Write processed data to S3 in Parquet format with region partitioning
datasink4 = glueContext.write_dynamic_frame.from_options(
    frame=df_final_output,
    connection_type="s3",
    connection_options={
        "path": "s3://de-on-youtube-cleansed-useast1-dev/youtube/raw_statistics/",
        "partitionKeys": ["region"]  # Partition by region for efficient querying
    },
    format="parquet",  # Columnar storage format for analytics
    transformation_ctx="datasink4"
)

# Finalize the Glue job execution
job.commit()
