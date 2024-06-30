import dlt


@dlt.resource(standalone=True)
def filesystem(bucket_url=dlt.config.value):
    """list and yield files in `bucket_url`"""
    ...


pipeline = dlt.pipeline(
    pipeline_name=...,
    destination=...,
    dataset_name=...,
)
# `filesystem` must be called before it is extracted or used in any other way
pipeline.run(filesystem("s3://my-bucket/reports"), table_name="reports")
