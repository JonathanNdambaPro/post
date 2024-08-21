import itertools
import random
import string
from datetime import datetime, timedelta
from pprint import pprint

import pandas as pd
import polars as pl
import pyarrow as pa
from deltalake import DeltaTable, write_deltalake

####### write first dataframe
df = pl.DataFrame({"num": [1, 2, 3], "letter": ["a", "b", "c"]})
df.write_delta("tmp/some-table", mode="overwrite")
print(df)
print("\n")
print("\n")

dt = DeltaTable("tmp/some-table")
print(f"Version: {dt.version()}")
print("\n")
print(f"Files: {dt.files()}")
print("\n")
print("\n")

####### append data
df = pl.DataFrame({"num": [8, 9, 5], "letter": ["dd", "ee", "zz"]})
df.write_delta("tmp/some-table", mode="append")


####### read data first version
dt = pl.read_delta("tmp/some-table", version=0)
print("version : 0")
print(dt)
print("\n")
print("\n")

####### read data second version
dt = pl.read_delta("tmp/some-table", version=1)
print("version : 1")
print(dt)
print("\n")
print("\n")

####### metadata
dt = DeltaTable("tmp/some-table")
print(dt.metadata())
print("\n")
print("\n")

####### schéma
print(dt.schema())
print("\n")
print(dt.schema().to_json())
print("\n")
print(dt.schema().to_pyarrow())
print("\n")
print("\n")

###### history
pprint(dt.history())
print("\n")
print("\n")

### Information sur les fichiers parquets
print(dt.get_add_actions(flatten=True).to_pandas())
print("\n")
print("\n")


### Remplacer les données sur un prédicat
df = pl.DataFrame({"num": [1], "letter": ["Z"]})
df.write_delta(
    "tmp/some-table",
    mode="overwrite",
    delta_write_options={"predicate": "num = 1", "engine": "rust"},
)


def record_observations(date: datetime) -> pa.Table:
    """Pulls data for a certain datetime"""
    nrows = 1000
    return pa.table(
        {
            "date": pa.array([date.date()] * nrows),
            "timestamp": pa.array([date] * nrows),
            "lettre_aleatoire": [
                random.choice(string.ascii_letters) for _ in range(1000)
            ],
        }
    )


hours_iter = (datetime(2021, 1, 1) + timedelta(hours=i) for i in itertools.count())

for timestamp in itertools.islice(hours_iter, 100):
    write_deltalake(
        "tmp/observation_data",
        record_observations(timestamp),
        partition_by=["date"],
        mode="append",
    )

### Compact les petit fichier petit fichier en un plus gros
dt = DeltaTable("tmp/observation_data")
pprint(dt.optimize.compact())
print("\n")
print("\n")

### Ordonner les données pour le saut de fichiers
dt = DeltaTable("tmp/observation_data")
pprint(dt.optimize.z_order(["lettre_aleatoire"]))
print("\n")
print("\n")


###### add constraint
df = pl.DataFrame({"num": [1, 2, 3]})
df.write_delta("tmp/some-table-constraint", mode="overwrite")

dt = DeltaTable("tmp/some-table-constraint")
dt.alter.add_constraint({"num_gt_0": "num > 0"})

df = pd.DataFrame({"num": [-1]})
write_deltalake(dt, df, mode="append", engine="rust")

## Cleaning des delta table
# dt.vacuum(retention_hours=0, enforce_retention_duration=False, dry_run=False)
