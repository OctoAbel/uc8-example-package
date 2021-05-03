from dbxdemo.appendcol import with_status

source_data = [
  ("pete", "tamisin", "peter.tamisin@databricks.com"),
  ("jason", "baer", "jason.baer@databricks.com")
]
source_df = spark.createDataFrame(
    source_data,
    ["first_name", "last_name", "email"]
)

actual_df = with_status(source_df)
display(actual_df)

