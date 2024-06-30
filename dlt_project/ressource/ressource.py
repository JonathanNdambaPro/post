import dlt


@dlt.resource(name="table_name", write_disposition="replace")
def generate_rows():
    for i in range(10):
        yield {"id": i, "example_string": "abc"}


@dlt.source
def source_name():
    return generate_rows


for row in generate_rows():
    print(row)

for row in source_name().resources.get("table_name"):
    print(row)
