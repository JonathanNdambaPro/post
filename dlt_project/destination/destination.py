import dlt
from dlt.destinations import postgres

# pass full credentials - together with the password (not recommended)
pipeline = dlt.pipeline(
    "pipeline",
    destination=postgres(
        credentials="postgresql://loader:loader@localhost:5432/dlt_data"
    ),
)

import dlt
from dlt.destinations import postgres

# pass credentials without password
# dlt will retrieve the password from ie. DESTINATION__POSTGRES__CREDENTIALS__PASSWORD
prod_postgres = postgres(credentials="postgresql://loader@localhost:5432/dlt_data")
pipeline = dlt.pipeline("pipeline", destination=prod_postgres)


import dlt
from dlt.destinations import filesystem
from dlt.sources.credentials import AzureCredentials

credentials = AzureCredentials()
# fill only the account name, leave key to be taken from secrets
credentials.azure_storage_account_name = "production_storage"
pipeline = dlt.pipeline(
    "pipeline", destination=filesystem("az://dlt-azure-bucket", credentials=credentials)
)

# https://dlthub.com/docs/general-usage/destination#configure-multiple-destinations-in-a-pipeline
